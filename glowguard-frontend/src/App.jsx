import './styles/globals.css'
import { BrowserRouter as Router, Routes, Route, useLocation } from 'react-router-dom'
import { ToastContainer } from 'react-toastify'
import 'react-toastify/dist/ReactToastify.css'

// Layout
import Header from './components/Layout/Header'
import Footer from './components/Layout/Footer'

// Pages
import Home from './pages/Home'
import Upload from './pages/Upload'
import Results from './pages/Results'
import Profile from './pages/Profile'
import Blog from './pages/Blog'
import Login from './pages/Login'
import Register from './pages/Register'
import BeforeAfter from './pages/BeforeAfter'
import NotFound from './pages/NotFound'

function AppContent() {
  const location = useLocation()
  
  // Hide header and footer on auth pages
  const hideLayout = ['/login', '/register'].includes(location.pathname)

  return (
    <div className="flex flex-col min-h-screen bg-gradient-to-br from-pastel-cream via-pastel-pink/10 to-pastel-lavender/10">
      {!hideLayout && <Header />}
      
      <main className={hideLayout ? "w-full" : "flex-grow"}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/upload" element={<Upload />} />
          <Route path="/results/:id" element={<Results />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/blog" element={<Blog />} />
          <Route path="/before-after" element={<BeforeAfter />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </main>

      {!hideLayout && <Footer />}
    </div>
  )
}

function App() {
  return (
    <Router future={{ v7_startTransition: true, v7_relativeSplatPath: true }}>
      <AppContent />
      
      <ToastContainer 
        position="bottom-right"
        autoClose={3000}
        hideProgressBar={false}
        theme="light"
      />
    </Router>
  )
}

export default App
