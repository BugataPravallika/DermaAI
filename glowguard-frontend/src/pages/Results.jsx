import { useParams } from 'react-router-dom'
import { useEffect, useState } from 'react'
import api from '../utils/api'
import { toast } from 'react-toastify'
import { FiBarChart2, FiAlertCircle, FiBook } from 'react-icons/fi'

export default function Results() {
  const { id } = useParams()
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const fetchResults = async () => {
      try {
        console.log('Fetching results for ID:', id)
        const response = await api.get(`/predictions/${id}`)
        console.log('Results response:', response.data)
        setResult(response.data)
      } catch (error) {
        console.error('Failed to fetch results:', error)
        console.error('Error details:', error.response?.data)
        toast.error(error.response?.data?.detail || 'Failed to load results')
      } finally {
        setLoading(false)
      }
    }

    if (id) {
      fetchResults()
    } else {
      setLoading(false)
    }
  }, [id])

  if (loading) {
    return <div className="min-h-screen flex items-center justify-center"><div className="animate-spin text-4xl">✨</div></div>
  }

  if (!result) {
    return <div className="min-h-screen flex items-center justify-center">No results found</div>
  }

  const { prediction, analysis, recommendations } = result

  return (
    <div className="min-h-screen py-12 px-4">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-12">
          <h1 className="text-4xl font-bold mb-4">Your Skin Analysis Results</h1>
          <p className="text-gray-600">Get personalized recommendations for your skin</p>
        </div>

        {/* Main Result Card */}
        <div className="card mb-8 border-2 border-pink-300">
          <div className="grid md:grid-cols-2 gap-8">
            {/* Image */}
            <div>
              <img
                src={prediction.image_path}
                alt="Analyzed skin"
                className="w-full h-64 object-cover rounded-xl"
              />
            </div>

            {/* Analysis */}
            <div className="space-y-6">
              <div>
                <h2 className="text-3xl font-bold text-pink-600 mb-2">
                  {analysis.disease_name}
                </h2>
                <p className="text-gray-600">{analysis.description}</p>
              </div>

              {/* Confidence Bar */}
              <div>
                <div className="flex justify-between mb-2">
                  <span className="font-semibold">Confidence Level</span>
                  <span className="text-pink-600">{(analysis.confidence * 100).toFixed(1)}%</span>
                </div>
                <div className="w-full bg-gray-200 rounded-full h-3">
                  <div
                    className="bg-gradient-to-r from-pink-400 to-rose-400 h-3 rounded-full"
                    style={{ width: `${analysis.confidence * 100}%` }}
                  />
                </div>
              </div>

              {/* Severity */}
              <div className={`p-4 rounded-lg ${
                analysis.severity === 'mild' ? 'bg-green-50 border border-green-300' :
                analysis.severity === 'moderate' ? 'bg-yellow-50 border border-yellow-300' :
                'bg-red-50 border border-red-300'
              }`}>
                <div className="font-semibold flex items-center gap-2">
                  <FiBarChart2 />
                  Severity: <span className="capitalize">{analysis.severity}</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Causes */}
        <div className="card mb-8">
          <h3 className="text-2xl font-bold mb-4 flex items-center gap-2">
            <FiAlertCircle /> Possible Causes
          </h3>
          <div className="grid md:grid-cols-2 gap-4">
            {analysis.causes.map((cause, i) => (
              <div key={i} className="flex items-start gap-3 p-3 bg-pink-50 rounded-lg">
                <span className="text-pink-500 mt-1">•</span>
                <span>{cause}</span>
              </div>
            ))}
          </div>
        </div>

        {/* Remedies */}
        <div className="grid md:grid-cols-2 gap-8 mb-8">
          {/* Natural Remedies */}
          <div className="card">
            <h3 className="text-xl font-bold mb-4">🌿 Natural Remedies</h3>
            <ul className="space-y-3">
              {analysis.remedies.slice(0, 3).map((remedy, i) => (
                <li key={i} className="text-sm text-gray-700">
                  <strong>•</strong> {remedy}
                </li>
              ))}
            </ul>
          </div>

          {/* Diet Advice */}
          <div className="card">
            <h3 className="text-xl font-bold mb-4">🥗 Diet Advice</h3>
            <div className="space-y-3 text-sm">
              <div>
                <strong className="text-green-600">✓ Eat:</strong>
                <ul className="mt-1 space-y-1">
                  {analysis.diet_advice.eat.slice(0, 2).map((food, i) => (
                    <li key={i}>• {food}</li>
                  ))}
                </ul>
              </div>
              <div>
                <strong className="text-red-600">✗ Avoid:</strong>
                <ul className="mt-1 space-y-1">
                  {analysis.diet_advice.avoid.slice(0, 2).map((food, i) => (
                    <li key={i}>• {food}</li>
                  ))}
                </ul>
              </div>
            </div>
          </div>
        </div>

        {/* Precautions */}
        <div className="card mb-8 bg-yellow-50 border border-yellow-300">
          <h3 className="text-xl font-bold mb-4 flex items-center gap-2">
            ⚠️ Important Precautions
          </h3>
          <ul className="grid md:grid-cols-2 gap-3">
            {analysis.precautions.slice(0, 4).map((precaution, i) => (
              <li key={i} className="text-sm text-gray-700">
                {precaution}
              </li>
            ))}
          </ul>
        </div>

        {/* Recommended Products */}
        {analysis.products.length > 0 && (
          <div className="card">
            <h3 className="text-2xl font-bold mb-6">💄 Recommended Products</h3>
            <div className="grid md:grid-cols-3 gap-6">
              {analysis.products.map((product) => (
                <div key={product.id} className="border border-pink-200 rounded-lg overflow-hidden hover:shadow-lg transition">
                  <div className="h-40 bg-gray-200 flex items-center justify-center">
                    {product.image_url ? (
                      <img src={product.image_url} alt={product.name} className="w-full h-full object-cover" />
                    ) : (
                      <span>No image</span>
                    )}
                  </div>
                  <div className="p-4">
                    <h4 className="font-bold text-sm mb-1">{product.name}</h4>
                    <p className="text-xs text-gray-600 mb-2">{product.brand}</p>
                    <p className="text-xs text-pink-600 font-semibold mb-3">{product.price_range}</p>
                    <a
                      href={product.purchase_link}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="btn-primary text-xs inline-block"
                    >
                      View Product
                    </a>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Dermatologist Note */}
        <div className="mt-12 p-6 bg-blue-50 border-l-4 border-blue-500 rounded">
          <h4 className="font-bold flex items-center gap-2 mb-2">
            👨‍⚕️ When to See a Dermatologist
          </h4>
          <p className="text-sm text-gray-700">
            While GlowGuard provides helpful insights, please consult a dermatologist if symptoms persist, 
            worsen, or affect your quality of life. This analysis is for informational purposes only.
          </p>
        </div>
      </div>
    </div>
  )
}
