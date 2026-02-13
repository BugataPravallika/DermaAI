import { Link, useNavigate } from 'react-router-dom'
import { useAuthStore } from '../../utils/store'
import { FiMenu, FiX, FiLogOut } from 'react-icons/fi'
import { useState } from 'react'

export default function Header() {
  const [isMenuOpen, setIsMenuOpen] = useState(false)
  const { user, logout } = useAuthStore()
  const navigate = useNavigate()

  const handleLogout = () => {
    logout()
    navigate('/')
  }

  return (
    <header className="bg-white/80 backdrop-blur-md shadow-md sticky top-0 z-50">
      <nav className="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
        {/* Logo */}
        <Link to="/" className="flex items-center gap-2">
          <div className="w-10 h-10 bg-gradient-to-r from-pink-400 to-rose-400 rounded-full flex items-center justify-center">
            <span className="text-white font-bold text-lg">G</span>
          </div>
          <h1 className="font-bold text-2xl bg-gradient-to-r from-pink-500 to-rose-500 bg-clip-text text-transparent">
            GlowGuard
          </h1>
        </Link>

        {/* Desktop Menu */}
        <div className="hidden md:flex items-center gap-8">
          <Link to="/" className="text-gray-700 hover:text-pink-500 transition">Home</Link>
          <Link to="/upload" className="text-gray-700 hover:text-pink-500 transition">Analyze</Link>
          <Link to="/before-after" className="text-gray-700 hover:text-pink-500 transition">Gallery</Link>
          <Link to="/blog" className="text-gray-700 hover:text-pink-500 transition">Blog</Link>

          {user ? (
            <div className="flex items-center gap-4">
              <Link to="/profile" className="text-gray-700 hover:text-pink-500 transition">
                {user.full_name}
              </Link>
              <button
                onClick={handleLogout}
                className="btn-primary"
              >
                <FiLogOut className="inline mr-2" /> Logout
              </button>
            </div>
          ) : (
            <div className="flex gap-3">
              <Link to="/login" className="btn-secondary">Login</Link>
              <Link to="/register" className="btn-primary">Sign Up</Link>
            </div>
          )}
        </div>

        {/* Mobile Menu Button */}
        <button
          onClick={() => setIsMenuOpen(!isMenuOpen)}
          className="md:hidden text-2xl"
        >
          {isMenuOpen ? <FiX /> : <FiMenu />}
        </button>
      </nav>

      {/* Mobile Menu */}
      {isMenuOpen && (
        <div className="md:hidden bg-white border-t border-pink-200 p-4 space-y-3 animate-slideUp">
          <Link to="/" className="block text-gray-700 hover:text-pink-500">Home</Link>
          <Link to="/upload" className="block text-gray-700 hover:text-pink-500">Analyze</Link>
          <Link to="/before-after" className="block text-gray-700 hover:text-pink-500">Gallery</Link>
          <Link to="/blog" className="block text-gray-700 hover:text-pink-500">Blog</Link>
          
          {user ? (
            <>
              <Link to="/profile" className="block text-gray-700 hover:text-pink-500">{user.full_name}</Link>
              <button onClick={handleLogout} className="btn-primary w-full">Logout</button>
            </>
          ) : (
            <>
              <Link to="/login" className="btn-secondary block text-center">Login</Link>
              <Link to="/register" className="btn-primary block text-center">Sign Up</Link>
            </>
          )}
        </div>
      )}
    </header>
  )
}
