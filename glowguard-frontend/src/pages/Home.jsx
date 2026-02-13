import { Link } from 'react-router-dom'
import { motion } from 'framer-motion'
import { FiArrowRight, FiCheck } from 'react-icons/fi'

export default function Home() {
  const features = [
    { icon: '🔍', title: 'AI Analysis', desc: 'Advanced computer vision detects skin conditions' },
    { icon: '💊', title: 'Smart Recommendations', desc: 'Personalized remedies, products & diet advice' },
    { icon: '🌿', title: 'Natural Solutions', desc: 'Safe home remedies and holistic guidance' },
    { icon: '📊', title: 'Track Progress', desc: 'Monitor improvements with before/after photos' },
  ]

  return (
    <div className="space-y-20">
      {/* Hero Section */}
      <section className="min-h-[90vh] flex items-center px-4">
        <div className="max-w-7xl mx-auto w-full grid md:grid-cols-2 gap-12 items-center">
          {/* Left */}
          <motion.div
            initial={{ opacity: 0, x: -50 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.8 }}
            className="space-y-6"
          >
            <h1 className="text-5xl md:text-6xl font-bold leading-tight">
              Understand Your
              <span className="block text-transparent bg-clip-text bg-gradient-to-r from-pink-500 to-rose-500">
                Skin Better
              </span>
            </h1>
            <p className="text-xl text-gray-600 leading-relaxed">
              Get instant AI-powered skin analysis with personalized care recommendations. 
              Upload a photo and discover what your skin needs.
            </p>
            <div className="flex flex-col sm:flex-row gap-4">
              <Link to="/upload" className="btn-primary text-lg">
                Start Analysis <FiArrowRight className="inline ml-2" />
              </Link>
              <Link to="/blog" className="btn-secondary text-lg">
                Learn More
              </Link>
            </div>
          </motion.div>

          {/* Right - Hero Image */}
          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.8, delay: 0.2 }}
            className="relative"
          >
            <div className="absolute -inset-4 bg-gradient-to-r from-pink-300 to-purple-300 rounded-3xl blur-2xl opacity-30"></div>
            <div className="relative bg-gradient-to-br from-pastel-pink/30 to-pastel-lavender/30 rounded-3xl h-96 border border-white/50 backdrop-blur-sm flex items-center justify-center">
              <div className="text-center">
                <div className="text-6xl mb-4">✨</div>
                <p className="text-gray-600">Beautiful, Healthy Skin Starts Here</p>
              </div>
            </div>
          </motion.div>
        </div>
      </section>

      {/* Features Section */}
      <section className="px-4 py-20 bg-gradient-to-r from-pastel-pink/10 to-pastel-lavender/10 rounded-3xl">
        <div className="max-w-7xl mx-auto">
          <h2 className="text-4xl font-bold text-center mb-16">Why Choose GlowGuard?</h2>
          <div className="grid md:grid-cols-4 gap-6">
            {features.map((feature, i) => (
              <motion.div
                key={i}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ delay: i * 0.1 }}
                className="card text-center"
              >
                <div className="text-4xl mb-3">{feature.icon}</div>
                <h3 className="font-semibold text-lg mb-2">{feature.title}</h3>
                <p className="text-gray-600 text-sm">{feature.desc}</p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* How It Works */}
      <section className="px-4 py-20">
        <div className="max-w-5xl mx-auto">
          <h2 className="text-4xl font-bold text-center mb-16">How It Works</h2>
          <div className="grid md:grid-cols-4 gap-4">
            {[
              { step: '1', title: 'Upload', desc: 'Clear photo of affected area' },
              { step: '2', title: 'Analyze', desc: 'AI processes image instantly' },
              { step: '3', title: 'Discover', desc: 'Get detailed predictions' },
              { step: '4', title: 'Act', desc: 'Follow personalized advice' },
            ].map((item, i) => (
              <div key={i} className="text-center">
                <div className="w-16 h-16 mx-auto bg-gradient-to-r from-pink-400 to-rose-400 rounded-full flex items-center justify-center text-white font-bold text-xl mb-4 shadow-lg">
                  {item.step}
                </div>
                <h3 className="font-semibold mb-2">{item.title}</h3>
                <p className="text-sm text-gray-600">{item.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="px-4 py-20">
        <div className="max-w-4xl mx-auto bg-gradient-to-r from-pink-300 to-rose-300 rounded-3xl p-12 text-center text-white">
          <h2 className="text-4xl font-bold mb-4">Ready to Glow?</h2>
          <p className="text-lg mb-8 text-white/90">
            Take the first step toward healthier, more radiant skin with AI-powered insights.
          </p>
          <Link to="/upload" className="inline-block bg-white text-pink-500 px-8 py-3 rounded-full font-semibold hover:shadow-lg transition-all">
            Get Started Now
          </Link>
        </div>
      </section>
    </div>
  )
}
