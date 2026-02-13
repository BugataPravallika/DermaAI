export default function Blog() {
  const articles = [
    {
      id: 1,
      title: 'Understanding Acne: Causes and Natural Remedies',
      excerpt: 'Learn what causes acne and discover effective natural remedies to treat it...',
      date: 'Feb 10, 2024',
      image: '🧴',
    },
    {
      id: 2,
      title: 'Skincare Routine for Different Skin Types',
      excerpt: 'Tailored skincare routines for oily, dry, and combination skin types...',
      date: 'Feb 8, 2024',
      image: '✨',
    },
    {
      id: 3,
      title: 'The Role of Diet in Skin Health',
      excerpt: 'Discover which foods support healthy skin and which ones to avoid...',
      date: 'Feb 5, 2024',
      image: '🥗',
    },
  ]

  return (
    <div className="min-h-screen py-12 px-4">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-5xl font-bold text-center mb-4 bg-gradient-to-r from-pink-500 to-rose-500 bg-clip-text text-transparent">
          Skincare Blog
        </h1>
        <p className="text-center text-gray-600 text-lg mb-12">
          Expert tips and advice for beautiful, healthy skin
        </p>

        <div className="grid md:grid-cols-1 gap-8">
          {articles.map((article) => (
            <div key={article.id} className="card hover:shadow-xl transition cursor-pointer">
              <div className="flex gap-6">
                <div className="text-6xl">{article.image}</div>
                <div className="flex-1">
                  <p className="text-sm text-gray-500 mb-2">{article.date}</p>
                  <h3 className="text-2xl font-bold mb-3">{article.title}</h3>
                  <p className="text-gray-600 mb-4">{article.excerpt}</p>
                  <button className="text-pink-500 font-semibold hover:text-pink-600">
                    Read More →
                  </button>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}
