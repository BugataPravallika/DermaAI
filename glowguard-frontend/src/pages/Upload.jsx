import ImageUpload from '../components/ImageUpload'

export default function Upload() {
  return (
    <div className="min-h-screen py-16 px-4">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-5xl font-bold text-center mb-4 bg-gradient-to-r from-pink-500 to-rose-500 bg-clip-text text-transparent">
          Analyze Your Skin
        </h1>
        <p className="text-center text-gray-600 text-lg mb-12">
          Upload a clear photo of your skin and get an instant AI analysis with personalized recommendations
        </p>

        <ImageUpload />

        {/* Tips */}
        <div className="mt-12 grid md:grid-cols-3 gap-6">
          {[
            { title: 'Good Lighting', desc: 'Use natural daylight for accurate analysis' },
            { title: 'Clear Photo', desc: 'Avoid makeup for better detection' },
            { title: 'Affected Area', desc: 'Focus on the area of concern' },
          ].map((tip, i) => (
            <div key={i} className="card">
              <div className="text-3xl mb-3">{['💡', '📸', '🎯'][i]}</div>
              <h3 className="font-semibold mb-2">{tip.title}</h3>
              <p className="text-sm text-gray-600">{tip.desc}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}
