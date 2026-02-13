export default function BeforeAfter() {
  const gallery = [
    { before: '😔', after: '😊', title: 'Acne Treatment' },
    { before: '😓', after: '✨', title: 'Eczema Relief' },
    { before: '🤔', after: '😄', title: 'Skin Improvement' },
  ]

  return (
    <div className="min-h-screen py-12 px-4">
      <div className="max-w-6xl mx-auto">
        <h1 className="text-5xl font-bold text-center mb-4 bg-gradient-to-r from-pink-500 to-rose-500 bg-clip-text text-transparent">
          Before & After Gallery
        </h1>
        <p className="text-center text-gray-600 text-lg mb-12">
          See real results from GlowGuard users
        </p>

        <div className="grid md:grid-cols-3 gap-8">
          {gallery.map((item, i) => (
            <div key={i} className="card">
              <div className="grid grid-cols-2 gap-4">
                <div className="bg-red-50 rounded-lg p-8 flex flex-col items-center justify-center">
                  <div className="text-6xl mb-3">{item.before}</div>
                  <p className="font-semibold text-center">Before</p>
                </div>
                <div className="bg-green-50 rounded-lg p-8 flex flex-col items-center justify-center">
                  <div className="text-6xl mb-3">{item.after}</div>
                  <p className="font-semibold text-center">After</p>
                </div>
              </div>
              <h3 className="font-bold text-lg text-center mt-4">{item.title}</h3>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}
