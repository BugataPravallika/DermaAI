import { useState } from 'react'
import { useAuthStore } from '../utils/store'
import { useNavigate } from 'react-router-dom'
import api from '../utils/api'
import { toast } from 'react-toastify'

export default function Profile() {
  const { user, setUser } = useAuthStore()
  const navigate = useNavigate()
  const [isEditing, setIsEditing] = useState(false)
  const [formData, setFormData] = useState({
    full_name: user?.full_name || '',
    age: user?.age || '',
    skin_type: user?.skin_type || '',
  })

  const handleChange = (e) => {
    const { name, value } = e.target
    setFormData(prev => ({ ...prev, [name]: value }))
  }

  const handleSave = async () => {
    try {
      const response = await api.put('/users/profile', formData)
      setUser(response.data)
      setIsEditing(false)
      toast.success('Profile updated!')
    } catch (error) {
      toast.error('Failed to update profile')
    }
  }

  if (!user) {
    return <div className="min-h-screen flex items-center justify-center">Loading...</div>
  }

  return (
    <div className="min-h-screen py-12 px-4">
      <div className="max-w-2xl mx-auto">
        <h1 className="text-4xl font-bold mb-8 bg-gradient-to-r from-pink-500 to-rose-500 bg-clip-text text-transparent">
          My Profile
        </h1>

        <div className="card">
          <div className="mb-6">
            <h2 className="text-2xl font-bold mb-4">{user.full_name || 'User'}</h2>
            <p className="text-gray-600">{user.email}</p>
          </div>

          {isEditing ? (
            <div className="space-y-4">
              <input
                type="text"
                name="full_name"
                placeholder="Full Name"
                value={formData.full_name}
                onChange={handleChange}
              />
              <input
                type="number"
                name="age"
                placeholder="Age"
                value={formData.age}
                onChange={handleChange}
              />
              <select
                name="skin_type"
                value={formData.skin_type}
                onChange={handleChange}
              >
                <option value="">Select Skin Type</option>
                <option value="oily">Oily</option>
                <option value="dry">Dry</option>
                <option value="combination">Combination</option>
                <option value="normal">Normal</option>
              </select>
              <div className="flex gap-3">
                <button onClick={handleSave} className="btn-primary flex-1">Save</button>
                <button onClick={() => setIsEditing(false)} className="btn-secondary flex-1">Cancel</button>
              </div>
            </div>
          ) : (
            <div className="space-y-4">
              <div>
                <label className="font-semibold">Full Name</label>
                <p className="text-gray-600">{formData.full_name || 'Not set'}</p>
              </div>
              <div>
                <label className="font-semibold">Age</label>
                <p className="text-gray-600">{formData.age || 'Not set'}</p>
              </div>
              <div>
                <label className="font-semibold">Skin Type</label>
                <p className="text-gray-600 capitalize">{formData.skin_type || 'Not set'}</p>
              </div>
              <button onClick={() => setIsEditing(true)} className="btn-primary">Edit Profile</button>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}
