import axios from 'axios'

const request = axios.create({
  baseURL: '/api',
  timeout: 120000, // 2 min for video uploads
  headers: { 'Content-Type': 'application/json' },
})

// Response interceptor
request.interceptors.response.use(
  (res) => res.data,
  (err) => {
    const msg = err.response?.data?.detail || err.message || 'Request failed'
    console.error('[API Error]', msg)
    return Promise.reject(new Error(msg))
  }
)

export default request
