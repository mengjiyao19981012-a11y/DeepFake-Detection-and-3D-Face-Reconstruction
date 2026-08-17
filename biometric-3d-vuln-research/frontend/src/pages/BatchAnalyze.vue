<template>
  <div class="batch-page">
    <div class="batch-container">
      <h1 class="page-title">Batch Video Analysis</h1>
      <p class="page-sub">Upload a video for frame-by-frame deepfake detection with risk score tracking</p>

      <div class="upload-section">
        <el-upload
          class="upload-area"
          drag
          :auto-upload="false"
          :show-file-list="true"
          :on-change="handleFileChange"
          accept="video/mp4,video/avi,video/mov,video/mkv"
        >
          <el-icon :size="48" color="#5ed29c"><VideoCameraFilled /></el-icon>
          <p class="upload-text">Drop video here or click to browse</p>
          <p class="upload-hint">MP4 / AVI / MOV / MKV, max 500 MB</p>
        </el-upload>
      </div>

      <div class="action-bar" v-if="selectedFile">
        <el-button type="primary" size="large" :loading="uploading" @click="startAnalysis">
          {{ uploading ? 'Uploading & Processing...' : 'Start Analysis' }}
        </el-button>
      </div>

      <!-- Task Status -->
      <div v-if="taskId" class="task-section">
        <div class="task-header">
          <h3>Task: {{ taskId }}</h3>
          <el-tag :type="taskStatus === 'done' ? 'success' : taskStatus === 'failed' ? 'danger' : 'warning'">
            {{ taskStatus }}
          </el-tag>
        </div>

        <div v-if="taskStatus === 'pending' || taskStatus === 'processing'" class="processing-hint">
          <el-progress :percentage="progress" :stroke-width="8" :color="'#5ed29c'" />
          <p class="hint-text">Processing frames... {{ progress }}% complete</p>
        </div>

        <!-- Results -->
        <div v-if="taskStatus === 'done' && stats" class="results">
          <div class="summary-row">
            <div class="stat-card">
              <span class="stat-value">{{ stats.total_frames }}</span>
              <span class="stat-label">Total Frames</span>
            </div>
            <div class="stat-card">
              <span class="stat-value">{{ stats.frames_with_faces }}</span>
              <span class="stat-label">Frames w/ Faces</span>
            </div>
            <div class="stat-card danger">
              <span class="stat-value">{{ stats.fake_frames }}</span>
              <span class="stat-label">Fake Frames</span>
            </div>
            <div class="stat-card" :class="{ danger: stats.fake_ratio > 0.3 }">
              <span class="stat-value">{{ (stats.fake_ratio * 100).toFixed(1) }}%</span>
              <span class="stat-label">Fake Ratio</span>
            </div>
          </div>

          <div class="summary-row">
            <div class="stat-card">
              <span class="stat-value">{{ stats.avg_fake_score.toFixed(4) }}</span>
              <span class="stat-label">Avg Risk Score</span>
            </div>
            <div class="stat-card">
              <span class="stat-value">{{ stats.max_fake_score.toFixed(4) }}</span>
              <span class="stat-label">Max Risk Score</span>
            </div>
          </div>

          <div class="export-section">
            <el-button @click="exportReport" :loading="exporting">
              <el-icon><Download /></el-icon> Export CSV Report
            </el-button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { detectVideo, getVideoTask } from '../api/detect'
import { exportCSV } from '../api/report'
import { ElMessage } from 'element-plus'

const selectedFile = ref(null)
const uploading = ref(false)
const taskId = ref(null)
const taskStatus = ref('pending')
const progress = ref(0)
const stats = ref(null)
const exporting = ref(false)

let pollTimer = null

function handleFileChange(file) {
  selectedFile.value = file.raw
}

async function startAnalysis() {
  if (!selectedFile.value) return
  uploading.value = true
  try {
    const data = await detectVideo(selectedFile.value)
    taskId.value = data.task_id
    taskStatus.value = data.status
    startPolling()
  } catch (e) {
    ElMessage.error(e.message || 'Upload failed')
  } finally {
    uploading.value = false
  }
}

function startPolling() {
  progress.value = 0
  pollTimer = setInterval(async () => {
    try {
      const data = await getVideoTask(taskId.value)
      taskStatus.value = data.status
      if (data.progress !== undefined) progress.value = data.progress
      if (data.status === 'done') {
        stats.value = data.stats || data
        clearInterval(pollTimer)
      }
      if (data.status === 'failed') {
        ElMessage.error(data.error_message || 'Processing failed')
        clearInterval(pollTimer)
      }
    } catch {
      // polling continues
    }
  }, 2000)
}

async function exportReport() {
  exporting.value = true
  try {
    const blob = await exportCSV(taskId.value)
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `detection_report_${taskId.value}.csv`
    a.click()
    URL.revokeObjectURL(url)
    ElMessage.success('Report downloaded')
  } catch (e) {
    ElMessage.error('Export failed')
  } finally {
    exporting.value = false
  }
}
</script>

<style scoped>
.batch-page {
  min-height: 100vh;
  padding: 48px 24px 80px;
}
.batch-container { max-width: 900px; margin: 0 auto; }
.page-title { font-size: 32px; font-weight: 800; margin-bottom: 8px; }
.page-sub { font-size: 14px; color: rgba(255,255,255,0.45); margin-bottom: 32px; }

.upload-section { margin-bottom: 20px; }
.upload-area { width: 100%; }
.upload-text { margin-top: 14px; font-size: 15px; color: rgba(255,255,255,0.6); }
.upload-hint { margin-top: 6px; font-size: 12px; color: rgba(255,255,255,0.25); }
.action-bar { margin-bottom: 24px; }

.task-section {
  background: rgba(255,255,255,0.02);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 16px;
  padding: 24px;
}
.task-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
}
.task-header h3 { font-size: 15px; font-weight: 600; }

.processing-hint { text-align: center; padding: 20px 0; }
.hint-text { margin-top: 10px; font-size: 13px; color: rgba(255,255,255,0.35); }

.summary-row {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 14px;
  margin-bottom: 14px;
}
.stat-card {
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 12px;
  padding: 16px;
  text-align: center;
}
.stat-card.danger { border-color: rgba(239,68,68,0.3); background: rgba(239,68,68,0.05); }
.stat-value { display: block; font-size: 26px; font-weight: 700; }
.stat-card.danger .stat-value { color: #ef4444; }
.stat-label { display: block; font-size: 11px; color: rgba(255,255,255,0.4); text-transform: uppercase; letter-spacing: 0.06em; margin-top: 4px; }

.export-section { margin-top: 20px; }

@media (max-width: 640px) {
  .summary-row { grid-template-columns: 1fr 1fr; }
}
</style>
