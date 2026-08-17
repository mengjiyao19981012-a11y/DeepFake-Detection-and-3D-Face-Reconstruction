<template>
  <div class="detect-page">
    <div class="detect-container">
      <h1 class="page-title">Single Image Detection</h1>
      <p class="page-sub">Upload an image to detect faces and classify authenticity with YOLOv8 + ResNet50</p>

      <!-- Upload Area -->
      <div class="upload-section">
        <el-upload
          class="upload-area"
          drag
          :auto-upload="false"
          :show-file-list="false"
          :on-change="handleFileChange"
          accept="image/jpeg,image/png,image/bmp"
        >
          <div v-if="!previewUrl" class="upload-placeholder">
            <el-icon :size="48" color="#5ed29c"><UploadFilled /></el-icon>
            <p class="upload-text">Drop image here or click to browse</p>
            <p class="upload-hint">JPG / PNG / BMP, max 500 MB</p>
          </div>
          <img v-else :src="previewUrl" class="preview-img" alt="Preview" />
        </el-upload>
      </div>

      <!-- Detect Button -->
      <div class="action-bar" v-if="selectedFile">
        <el-button
          type="primary"
          size="large"
          :loading="loading"
          @click="runDetection"
          :disabled="loading"
        >
          {{ loading ? 'Detecting...' : 'Run Detection' }}
        </el-button>
      </div>

      <!-- Error -->
      <el-alert v-if="errorMsg" :title="errorMsg" type="error" show-icon closable @close="errorMsg=''" class="error-alert" />

      <!-- Results -->
      <div v-if="result" class="results">
        <!-- Summary Cards -->
        <div class="summary-row">
          <div class="stat-card">
            <span class="stat-value">{{ result.face_count }}</span>
            <span class="stat-label">Faces Detected</span>
          </div>
          <div class="stat-card" :class="{ danger: result.has_fake }">
            <span class="stat-value">{{ result.summary.fake_count }}</span>
            <span class="stat-label">Fake Faces</span>
          </div>
          <div class="stat-card">
            <span class="stat-value">{{ result.summary.avg_fake_score.toFixed(2) }}</span>
            <span class="stat-label">Avg Risk Score</span>
          </div>
          <div class="stat-card">
            <span class="stat-value">{{ result.summary.max_fake_score.toFixed(2) }}</span>
            <span class="stat-label">Max Risk Score</span>
          </div>
        </div>

        <!-- Annotated Image -->
        <div v-if="result.annotated_path" class="annotated-section">
          <h3 class="section-heading">Annotated Result</h3>
          <img :src="annotatedUrl" class="annotated-img" alt="Annotated" />
        </div>

        <!-- Per-Face Details -->
        <div v-if="result.faces.length" class="faces-section">
          <h3 class="section-heading">Face Details</h3>
          <div class="faces-list">
            <div v-for="(face, i) in result.faces" :key="i" class="face-item" :class="{ 'face-fake': !face.is_real }">
              <div class="face-header">
                <el-tag :type="face.is_real ? 'success' : 'danger'" size="small">
                  {{ face.is_real ? 'REAL' : 'FAKE' }}
                </el-tag>
                <span class="face-label-text">{{ face.label.replace('_', ' ').toUpperCase() }}</span>
              </div>
              <div class="face-meta">
                <div class="meta-row">
                  <span class="meta-key">Fake Score</span>
                  <span class="meta-val" :class="{ 'text-danger': face.fake_score > 0.5 }">{{ face.fake_score.toFixed(4) }}</span>
                </div>
                <div class="meta-row">
                  <span class="meta-key">BBox</span>
                  <span class="meta-val">{{ face.bbox.join(', ') }}</span>
                </div>
                <div class="meta-row">
                  <span class="meta-key">YOLO Conf</span>
                  <span class="meta-val">{{ face.yolo_conf.toFixed(4) }}</span>
                </div>
                <div class="prob-bars">
                  <div class="prob-bar">
                    <span class="prob-label">Real</span>
                    <div class="prob-track"><div class="prob-fill real" :style="{ width: (face.probs.real * 100) + '%' }"></div></div>
                    <span class="prob-val">{{ (face.probs.real * 100).toFixed(1) }}%</span>
                  </div>
                  <div class="prob-bar">
                    <span class="prob-label">2D Fake</span>
                    <div class="prob-track"><div class="prob-fill fake2d" :style="{ width: (face.probs['2d_deepfake'] * 100) + '%' }"></div></div>
                    <span class="prob-val">{{ (face.probs['2d_deepfake'] * 100).toFixed(1) }}%</span>
                  </div>
                  <div class="prob-bar">
                    <span class="prob-label">3D Synthetic</span>
                    <div class="prob-track"><div class="prob-fill fake3d" :style="{ width: (face.probs['3d_synthetic'] * 100) + '%' }"></div></div>
                    <span class="prob-val">{{ (face.probs['3d_synthetic'] * 100).toFixed(1) }}%</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { detectImage } from '../api/detect'

const selectedFile = ref(null)
const previewUrl = ref(null)
const loading = ref(false)
const errorMsg = ref('')
const result = ref(null)

const annotatedUrl = computed(() => {
  if (!result.value?.annotated_path) return null
  return '/api' + result.value.annotated_path
})

function handleFileChange(file) {
  selectedFile.value = file.raw
  previewUrl.value = URL.createObjectURL(file.raw)
  result.value = null
  errorMsg.value = ''
}

async function runDetection() {
  if (!selectedFile.value) return
  loading.value = true
  errorMsg.value = ''
  result.value = null
  try {
    const data = await detectImage(selectedFile.value)
    result.value = data
  } catch (e) {
    errorMsg.value = e.message || 'Detection failed'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.detect-page {
  min-height: 100vh;
  padding: 48px 24px 80px;
}
.detect-container {
  max-width: 900px;
  margin: 0 auto;
}
.page-title {
  font-size: 32px;
  font-weight: 800;
  margin-bottom: 8px;
}
.page-sub {
  font-size: 14px;
  color: rgba(255,255,255,0.45);
  margin-bottom: 32px;
}

/* Upload */
.upload-section {
  margin-bottom: 20px;
}
.upload-area {
  width: 100%;
}
.upload-placeholder {
  padding: 60px 20px;
  text-align: center;
}
.upload-text {
  margin-top: 14px;
  font-size: 15px;
  color: rgba(255,255,255,0.6);
}
.upload-hint {
  margin-top: 6px;
  font-size: 12px;
  color: rgba(255,255,255,0.25);
}
.preview-img {
  max-height: 400px;
  object-fit: contain;
  border-radius: 12px;
}

/* Action */
.action-bar {
  margin-bottom: 24px;
}

/* Error */
.error-alert {
  margin-bottom: 20px;
}

/* Summary */
.summary-row {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  margin-bottom: 28px;
}
.stat-card {
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 12px;
  padding: 20px;
  text-align: center;
}
.stat-card.danger {
  border-color: rgba(239, 68, 68, 0.3);
  background: rgba(239, 68, 68, 0.05);
}
.stat-value {
  display: block;
  font-size: 28px;
  font-weight: 700;
}
.stat-card.danger .stat-value { color: #ef4444; }
.stat-label {
  display: block;
  font-size: 11px;
  color: rgba(255,255,255,0.4);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  margin-top: 4px;
}

/* Annotated image */
.annotated-section { margin-bottom: 28px; }
.section-heading {
  font-size: 17px;
  font-weight: 700;
  margin-bottom: 12px;
}
.annotated-img {
  width: 100%;
  border-radius: 12px;
  border: 1px solid rgba(255,255,255,0.1);
}

/* Faces list */
.faces-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.face-item {
  background: rgba(255,255,255,0.02);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 12px;
  padding: 18px;
}
.face-item.face-fake {
  border-color: rgba(239, 68, 68, 0.25);
  background: rgba(239, 68, 68, 0.03);
}
.face-header {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 12px;
}
.face-label-text {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.08em;
  color: rgba(255,255,255,0.5);
}

.face-meta { display: flex; flex-direction: column; gap: 6px; }
.meta-row {
  display: flex;
  justify-content: space-between;
  font-size: 13px;
}
.meta-key { color: rgba(255,255,255,0.35); }
.meta-val { font-weight: 600; }
.text-danger { color: #ef4444; }

/* Prob bars */
.prob-bars {
  margin-top: 10px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.prob-bar {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 12px;
}
.prob-label {
  width: 80px;
  text-align: right;
  color: rgba(255,255,255,0.35);
  flex-shrink: 0;
}
.prob-track {
  flex: 1;
  height: 6px;
  background: rgba(255,255,255,0.06);
  border-radius: 3px;
  overflow: hidden;
}
.prob-fill {
  height: 100%;
  border-radius: 3px;
  transition: width 0.5s;
}
.prob-fill.real { background: #5ed29c; }
.prob-fill.fake2d { background: #f59e0b; }
.prob-fill.fake3d { background: #ef4444; }
.prob-val {
  width: 40px;
  color: rgba(255,255,255,0.5);
  flex-shrink: 0;
}

@media (max-width: 640px) {
  .summary-row { grid-template-columns: 1fr 1fr; }
}
</style>
