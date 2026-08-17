import request from './request'

/**
 * Export CSV detection report for a video task.
 */
export function exportCSV(taskId) {
  return request.get(`/report/export/${taskId}`, {
    responseType: 'blob',
  })
}
