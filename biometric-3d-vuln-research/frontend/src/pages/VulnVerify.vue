<template>
  <div class="verify-page">
    <div class="verify-container">
      <h1 class="page-title">3D Face Reconstruction</h1>
      <p class="page-sub">Generate OBJ 3D face models from verified real faces using Deep3DFaceRecon</p>

      <el-alert
        type="warning"
        :closable="false"
        show-icon
        class="info-alert"
      >
        <template #title>
          Only faces classified as <strong>REAL</strong> are eligible for 3D reconstruction.
          Fake faces will be blocked.
        </template>
      </el-alert>

      <div class="upload-section">
        <el-upload
          class="upload-area"
          drag
          :auto-upload="false"
          :show-file-list="false"
          :on-change="handleFileChange"
          accept="image/jpeg,image/png"
        >
          <div v-if="!previewUrl" class="upload-placeholder">
            <el-icon :size="48" color="#5ed29c"><PictureFilled /></el-icon>
            <p class="upload-text">Drop a verified real-face image here</p>
            <p class="upload-hint">First run detection on /detect, then upload the real face</p>
          </div>
          <img v-else :src="previewUrl" class="preview-img" alt="Preview" />
        </el-upload>
      </div>

      <div class="action-bar" v-if="selectedFile">
        <el-button type="primary" size="large" :loading="loading" @click="runRecon">
          {{ loading ? 'Reconstructing...' : 'Generate 3D Model' }}
        </el-button>
      </div>

      <!-- Result -->
      <div v-if="result" class="result-section">
        <div v-if="result.obj_path" class="success-box">
          <h3>3D Model Generated</h3>
          <p>OBJ file: {{ result.obj_path }}</p>
          <!-- Three.js viewer placeholder -->
          <div class="viewer-placeholder">
            <p class="viewer-hint">3D viewer will be rendered here with Three.js</p>
          </div>
        </div>
        <el-alert v-else type="info" title="This face was classified as fake — 3D reconstruction blocked" show-icon />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { ElMessage } from 'element-plus'

const selectedFile = ref(null)
const previewUrl = ref(null)
const loading = ref(false)
const result = ref(null)

function handleFileChange(file) {
  selectedFile.value = file.raw
  previewUrl.value = URL.createObjectURL(file.raw)
  result.value = null
}

async function runRecon() {
  loading.value = true
  try {
    ElMessage.info('3D reconstruction endpoint not yet implemented')
    result.value = { status: 'pending' }
  } catch (e) {
    ElMessage.error(e.message)
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.verify-page {
  min-height: 100vh;
  padding: 48px 24px 80px;
}
.verify-container { max-width: 900px; margin: 0 auto; }
.page-title { font-size: 32px; font-weight: 800; margin-bottom: 8px; }
.page-sub { font-size: 14px; color: rgba(255,255,255,0.45); margin-bottom: 24px; }
.info-alert { margin-bottom: 24px; }

.upload-section { margin-bottom: 20px; }
.upload-area { width: 100%; }
.upload-placeholder { padding: 60px 20px; text-align: center; }
.upload-text { margin-top: 14px; font-size: 15px; color: rgba(255,255,255,0.6); }
.upload-hint { margin-top: 6px; font-size: 12px; color: rgba(255,255,255,0.25); }
.preview-img { max-height: 400px; object-fit: contain; border-radius: 12px; }
.action-bar { margin-bottom: 24px; }

.result-section { margin-top: 20px; }
.success-box {
  background: rgba(94,210,156,0.04);
  border: 1px solid rgba(94,210,156,0.2);
  border-radius: 16px;
  padding: 24px;
}
.success-box h3 { font-size: 18px; font-weight: 700; margin-bottom: 8px; }
.success-box p { font-size: 13px; color: rgba(255,255,255,0.5); }
.viewer-placeholder {
  margin-top: 16px;
  aspect-ratio: 16/10;
  background: rgba(0,0,0,0.3);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px dashed rgba(255,255,255,0.1);
}
.viewer-hint { font-size: 13px; color: rgba(255,255,255,0.2); }
</style>
