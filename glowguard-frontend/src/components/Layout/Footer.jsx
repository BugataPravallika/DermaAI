import { Link } from 'react-router-dom'
import { FiFacebook, FiTwitter, FiInstagram, FiLinkedin } from 'react-icons/fi'

export default function Footer() {
  return (
    <footer className="bg-gradient-to-r from-pink-50 to-purple-50 border-t border-pink-200 mt-16">
      <div className="max-w-7xl mx-auto px-4 py-12">
        <div className="grid md:grid-cols-4 gap-8 mb-8">
          {/* Brand */}
          <div>
            <h3 className="text-lg font-bold text-pink-600 mb-4">GlowGuard</h3>
            <p className="text-gray-600 text-sm">
              AI-powered skin care disease prediction and personalized guidance platform.
            </p>
          </div>

          {/* Links */}
          <div>
            <h4 className="font-semibold text-gray-800 mb-4">Product</h4>
            <ul className="space-y-2 text-sm text-gray-600">
              <li><Link to="/" className="hover:text-pink-500">Home</Link></li>
              <li><Link to="/upload" className="hover:text-pink-500">Analyze</Link></li>
              <li><Link to="/blog" className="hover:text-pink-500">Blog</Link></li>
            </ul>
          </div>

          {/* Company */}
          <div>
            <h4 className="font-semibold text-gray-800 mb-4">Company</h4>
            <ul className="space-y-2 text-sm text-gray-600">
              <li><a href="#" className="hover:text-pink-500">About</a></li>
              <li><a href="#" className="hover:text-pink-500">Contact</a></li>
              <li><a href="#" className="hover:text-pink-500">Privacy</a></li>
            </ul>
          </div>

          {/* Social */}
          <div>
            <h4 className="font-semibold text-gray-800 mb-4">Follow Us</h4>
            <div className="flex gap-4 text-xl">
              <a href="#" className="text-pink-500 hover:text-pink-600 transition"><FiFacebook /></a>
              <a href="#" className="text-pink-500 hover:text-pink-600 transition"><FiTwitter /></a>
              <a href="#" className="text-pink-500 hover:text-pink-600 transition"><FiInstagram /></a>
              <a href="#" className="text-pink-500 hover:text-pink-600 transition"><FiLinkedin /></a>
            </div>
          </div>
        </div>

        {/* Disclaimer */}
        <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-4 mb-8">
          <p className="text-xs text-yellow-800">
            <strong>⚠️ Medical Disclaimer:</strong> GlowGuard provides AI-based predictions for educational purposes only. 
            This is NOT a medical diagnosis. Always consult with a qualified dermatologist for professional medical advice.
          </p>
        </div>

        {/* Bottom */}
        <div className="border-t border-pink-200 pt-8 text-center text-sm text-gray-600">
          <p>&copy; 2024 GlowGuard. All rights reserved.</p>
        </div>
      </div>
    </footer>
  )
}
