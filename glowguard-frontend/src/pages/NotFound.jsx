export default function NotFound() {
  return (
    <div className="min-h-screen flex items-center justify-center px-4">
      <div className="text-center">
        <h1 className="text-6xl font-bold mb-4">404</h1>
        <p className="text-2xl text-gray-600 mb-8">Page not found</p>
        <a href="/" className="btn-primary inline-block">Go Home</a>
      </div>
    </div>
  )
}
