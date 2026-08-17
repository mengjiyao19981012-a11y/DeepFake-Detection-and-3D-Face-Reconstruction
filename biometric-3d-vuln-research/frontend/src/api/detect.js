import request from './request'

/**
 * Upload a single image for face detection + classification.
 */
export function detectImage(file) {
  const formData = new FormData()
  formData.append('file', file)
  return request.post('/detect/image', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  })
}

/**
 * Upload a video for async detection processing.
 */
export function detectVideo(file) {
  const formData = new FormData()
  formData.append('file', file)
  return request.post('/detect/video', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  })
}

/**
 * Query video task status and results.
 */
export function getVideoTask(taskId) {
  return request.get(`/video/task/${taskId}`)
}
