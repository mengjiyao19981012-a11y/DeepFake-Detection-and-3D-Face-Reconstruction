<template>
  <div class="samples-page">
    <div class="samples-container">
      <h1 class="page-title">Sample Library</h1>
      <p class="page-sub">Browse and manage detection samples — real faces vs. deepfake samples</p>

      <div class="samples-grid">
        <div class="sample-card" v-for="i in 4" :key="i">
          <div class="sample-preview">
            <span class="sample-placeholder">Sample #{{ i }}</span>
          </div>
          <div class="sample-info">
            <span class="sample-name">sample_{{ i }}.jpg</span>
            <el-tag :type="i <= 2 ? 'success' : 'danger'" size="small">
              {{ i <= 2 ? 'REAL' : 'FAKE' }}
            </el-tag>
          </div>
        </div>
      </div>

      <div class="empty-hint" v-if="false">
        <p>No samples uploaded yet. Upload images via the detection page to populate the library.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.samples-page {
  min-height: 100vh;
  padding: 48px 24px 80px;
}
.samples-container { max-width: 1200px; margin: 0 auto; }
.page-title { font-size: 32px; font-weight: 800; margin-bottom: 8px; }
.page-sub { font-size: 14px; color: rgba(255,255,255,0.45); margin-bottom: 32px; }

.samples-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 20px;
}
.sample-card {
  background: rgba(255,255,255,0.02);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 14px;
  overflow: hidden;
  transition: border-color 0.3s;
}
.sample-card:hover { border-color: rgba(94,210,156,0.25); }
.sample-preview {
  aspect-ratio: 4/3;
  background: rgba(0,0,0,0.3);
  display: flex;
  align-items: center;
  justify-content: center;
}
.sample-placeholder {
  font-size: 13px;
  color: rgba(255,255,255,0.15);
}
.sample-info {
  padding: 12px 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.sample-name {
  font-size: 13px;
  color: rgba(255,255,255,0.5);
}

.empty-hint {
  text-align: center;
  padding: 60px 20px;
  color: rgba(255,255,255,0.2);
}
</style>
