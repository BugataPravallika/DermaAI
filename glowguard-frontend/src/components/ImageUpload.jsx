import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { FiUpload, FiLoader } from 'react-icons/fi'
import api from '../../utils/api'
import { toast } from 'react-toastify'
import { useAuthStore } from '../../utils/store'
import { usePredictionStore } from '../../utils/store'

export default function ImageUpload() {
  const [file, setFile] = useState(null)
  const [preview, setPreview] = useState(null)
  const [loading, setLoading] = useState(false)
  const [dragActive, setDragActive] = useState(false)
  const navigate = useNavigate()
  const { token } = useAuthStore()
  const { addPrediction } = usePredictionStore()

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0]
    if (selectedFile) {
      processFile(selectedFile)
    }
  }

  const processFile = (selectedFile) => {
    if (!selectedFile.type.startsWith('image/')) {
      toast.error('Please select an image file')
      return
    }

    if (selectedFile.size > 5 * 1024 * 1024) {
      toast.error('File size must be less than 5MB')
      return
    }

    setFile(selectedFile)
    const reader = new FileReader()
    reader.onloadend = () => {
      setPreview(reader.result)
    }
    reader.readAsDataURL(selectedFile)
  }

  const handleDrag = (e) => {
    e.preventDefault()
    e.stopPropagation()
    if (e.type === 'dragenter' || e.type === 'dragover') {
      setDragActive(true)
    } else if (e.type === 'dragleave') {
      setDragActive(false)
    }
  }

  const handleDrop = (e) => {
    e.preventDefault()
    e.stopPropagation()
    setDragActive(false)
    
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      processFile(e.dataTransfer.files[0])
    }
  }

  const handleAnalyze = async () => {
    if (!token) {
      toast.error('Please login first')
      navigate('/login')
      return
    }

    if (!file) {
      toast.error('Please select an image')
      return
    }

    setLoading(true)
    try {
      const formData = new FormData()
      formData.append('file', file)

      const response = await api.post('/predictions/analyze', formData, {
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'multipart/form-data'
        }
      })

      addPrediction(response.data)
      toast.success('Analysis complete!')
      navigate(`/results/${response.data.prediction.id}`)
    } catch (error) {
      console.error('Error analyzing image:', error)
      toast.error(error.response?.data?.detail || 'Error analyzing image')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="w-full max-w-2xl mx-auto">
      <div
        onDragEnter={handleDrag}
        onDragLeave={handleDrag}
        onDragOver={handleDrag}
        onDrop={handleDrop}
        className={`relative rounded-2xl border-3 border-dashed transition-all p-8 ${
          dragActive
            ? 'border-pink-500 bg-pink-50'
            : 'border-pastel-pink/50 bg-white hover:border-pink-400'
        }`}
      >
        <input
          type="file"
          onChange={handleFileChange}
          accept="image/*"
          className="hidden"
          id="file-input"
        />

        {!preview ? (
          <label htmlFor="file-input" className="cursor-pointer">
            <div className="flex flex-col items-center justify-center gap-4">
              <div className="text-5xl text-pink-300">
                <FiUpload />
              </div>
              <div className="text-center">
                <h3 className="text-xl font-semibold text-gray-800 mb-2">
                  Upload a clear photo of your skin
                </h3>
                <p className="text-gray-600 mb-2">
                  Drag and drop your image here or click to browse
                </p>
                <p className="text-sm text-gray-500">
                  Supported: JPG, PNG, WebP • Max 5MB
                </p>
              </div>
            </div>
          </label>
        ) : (
          <div className="space-y-4">
            <img
              src={preview}
              alt="Preview"
              className="w-full h-64 object-cover rounded-xl"
            />
            <button
              onClick={() => {
                setFile(null)
                setPreview(null)
              }}
              className="btn-secondary w-full"
            >
              Choose Different Image
            </button>
          </div>
        )}
      </div>

      {preview && (
        <button
          onClick={handleAnalyze}
          disabled={loading}
          className="btn-primary w-full mt-6 flex items-center justify-center gap-2"
        >
          {loading ? (
            <>
              <FiLoader className="animate-spin" />
              Analyzing...
            </>
          ) : (
            'Analyze Skin'
          )}
        </button>
      )}
    </div>
  )
}
