import { useState } from 'react'
import { useNavigate, Link } from 'react-router-dom'

import api from '../utils/api'
import { toast } from 'react-toastify'

export default function Register() {
  const navigate = useNavigate()
  const [formData, setFormData] = useState({
    email: '',
    username: '',
    password: '',
    full_name: '',
  })
  const [loading, setLoading] = useState(false)

  const handleChange = (e) => {
    setFormData(prev => ({ ...prev, [e.target.name]: e.target.value }))
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    try {
      console.log('Sending registration data:', formData)
      const response = await api.post('/auth/register', formData)
      console.log('Registration response:', response.data)
      toast.success('Account created! Please login.')
      navigate('/login')
    } catch (error) {
      console.error('Registration error:', error)
      console.error('Error response:', error.response?.data)
      console.error('Error status:', error.response?.status)
      const errorMsg = error.response?.data?.detail || error.message || 'Registration failed'
      toast.error(errorMsg)
    } finally {
      setLoading(false)
    }
  }

  const styles = {
    container: {
      minHeight: '100vh',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      padding: '20px',
      background: 'linear-gradient(to bottom right, #fff8f3, #ffffff, rgba(255, 214, 232, 0.2))',
      fontFamily: "'Poppins', sans-serif",
    },
    card: {
      background: 'white',
      borderRadius: '30px',
      boxShadow: '0 20px 60px rgba(0, 0, 0, 0.1)',
      border: '2px solid rgba(255, 182, 193, 0.2)',
      padding: '40px',
      maxWidth: '420px',
      width: '100%',
    },
    header: {
      textAlign: 'center',
      marginBottom: '30px',
    },
    title: {
      fontSize: '32px',
      fontWeight: '700',
      background: 'linear-gradient(to right, #ec4899, #f43f5e)',
      WebkitBackgroundClip: 'text',
      WebkitTextFillColor: 'transparent',
      marginBottom: '10px',
    },
    subtitle: {
      fontSize: '22px',
      fontWeight: '600',
      color: '#1f2937',
      marginBottom: '8px',
    },
    description: {
      color: '#666',
      fontSize: '14px',
    },
    form: {
      display: 'flex',
      flexDirection: 'column',
      gap: '16px',
    },
    inputContainer: {
      position: 'relative',
    },
    input: {
      width: '100%',
      padding: '14px 14px 14px 45px',
      borderRadius: '12px',
      border: '2px solid rgba(255, 182, 193, 0.3)',
      fontSize: '15px',
      fontFamily: "'Poppins', sans-serif",
      fontWeight: '500',
      background: 'rgba(255, 214, 232, 0.5)',
      outline: 'none',
      transition: 'all 0.3s ease',
    },
    inputFocus: {
      borderColor: '#ec4899',
      boxShadow: '0 0 0 2px rgba(236, 72, 153, 0.2)',
    },
    icon: {
      position: 'absolute',
      left: '14px',
      top: '50%',
      transform: 'translateY(-50%)',
      color: '#f472b6',
      fontSize: '18px',
    },
    button: {
      marginTop: '12px',
      padding: '14px 24px',
      background: 'linear-gradient(to right, #f472b6, #f43f5e)',
      color: 'white',
      border: 'none',
      borderRadius: '12px',
      fontSize: '16px',
      fontWeight: '600',
      cursor: 'pointer',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      gap: '8px',
      transition: 'all 0.3s ease',
      opacity: loading ? 0.7 : 1,
    },
    divider: {
      display: 'flex',
      alignItems: 'center',
      gap: '12px',
      margin: '20px 0',
    },
    dividerLine: {
      flex: 1,
      height: '1px',
      background: '#ddd',
    },
    dividerText: {
      fontSize: '12px',
      color: '#999',
      textTransform: 'uppercase',
      fontWeight: '600',
      letterSpacing: '0.5px',
    },
    loginLink: {
      textAlign: 'center',
      fontSize: '14px',
      color: '#666',
    },
    link: {
      color: '#ec4899',
      fontWeight: '700',
      textDecoration: 'none',
      cursor: 'pointer',
      display: 'inline-flex',
      alignItems: 'center',
      gap: '4px',
      marginLeft: '4px',
      transition: 'color 0.3s ease',
    },
    features: {
      marginTop: '32px',
      display: 'grid',
      gridTemplateColumns: '1fr 1fr',
      gap: '16px',
    },
    feature: {
      padding: '16px',
      borderRadius: '12px',
      textAlign: 'center',
      border: '2px solid rgba(255, 214, 232, 0.2)',
      background: 'rgba(255, 214, 232, 0.1)',
      transition: 'all 0.3s ease',
      cursor: 'pointer',
    },
    featureIcon: {
      fontSize: '28px',
      marginBottom: '8px',
    },
    featureTitle: {
      fontWeight: '600',
      color: '#1f2937',
      fontSize: '14px',
      marginBottom: '4px',
    },
    featureDesc: {
      fontSize: '12px',
      color: '#999',
    },
  }

  return (
    <div style={styles.container}>
      <div style={styles.card}>
        {/* Header */}
        <div style={styles.header}>
          <h1 style={styles.title}>GlowGuard</h1>
          <h2 style={styles.subtitle}>Create Account</h2>
          <p style={styles.description}>Join to get AI-powered skin analysis</p>
        </div>

        {/* Form */}
        <form onSubmit={handleSubmit} style={styles.form}>
          <div style={styles.inputContainer}>
            <span style={styles.icon}>✉️</span>
            <input
              type="email"
              name="email"
              placeholder="Email address"
              value={formData.email}
              onChange={handleChange}
              required
              style={{...styles.input}}
              onFocus={(e) => Object.assign(e.target.style, styles.inputFocus)}
              onBlur={(e) => {
                e.target.style.borderColor = 'rgba(255, 182, 193, 0.3)'
                e.target.style.boxShadow = 'none'
              }}
            />
          </div>

          <div style={styles.inputContainer}>
            <span style={styles.icon}>👤</span>
            <input
              type="text"
              name="username"
              placeholder="Username"
              value={formData.username}
              onChange={handleChange}
              required
              style={{...styles.input}}
              onFocus={(e) => Object.assign(e.target.style, styles.inputFocus)}
              onBlur={(e) => {
                e.target.style.borderColor = 'rgba(255, 182, 193, 0.3)'
                e.target.style.boxShadow = 'none'
              }}
            />
          </div>

          <div style={styles.inputContainer}>
            <span style={styles.icon}>👤</span>
            <input
              type="text"
              name="full_name"
              placeholder="Full name"
              value={formData.full_name}
              onChange={handleChange}
              style={{...styles.input}}
              onFocus={(e) => Object.assign(e.target.style, styles.inputFocus)}
              onBlur={(e) => {
                e.target.style.borderColor = 'rgba(255, 182, 193, 0.3)'
                e.target.style.boxShadow = 'none'
              }}
            />
          </div>

          <div style={styles.inputContainer}>
            <span style={styles.icon}>🔒</span>
            <input
              type="password"
              name="password"
              placeholder="Password"
              value={formData.password}
              onChange={handleChange}
              required
              style={{...styles.input}}
              onFocus={(e) => Object.assign(e.target.style, styles.inputFocus)}
              onBlur={(e) => {
                e.target.style.borderColor = 'rgba(255, 182, 193, 0.3)'
                e.target.style.boxShadow = 'none'
              }}
            />
          </div>

          <button
            type="submit"
            disabled={loading}
            style={styles.button}
            onMouseOver={(e) => {
              if (!loading) e.target.style.transform = 'scale(1.02)'
            }}
            onMouseOut={(e) => {
              e.target.style.transform = 'scale(1)'
            }}
          >
            {loading ? 'Creating account...' : <>Sign Up →</>}
          </button>
        </form>

        {/* Divider */}
        <div style={styles.divider}>
          <div style={styles.dividerLine}></div>
          <span style={styles.dividerText}>or</span>
          <div style={styles.dividerLine}></div>
        </div>

        {/* Login Link */}
        <p style={styles.loginLink}>
          Already have an account?
          <Link to="/login" style={styles.link}>
            Login →
          </Link>
        </p>
      </div>

      {/* Features */}
      <div style={styles.features}>
        <div style={styles.feature} onMouseOver={(e) => e.currentTarget.style.boxShadow = '0 4px 12px rgba(0,0,0,0.08)'} onMouseOut={(e) => e.currentTarget.style.boxShadow = 'none'}>
          <div style={styles.featureIcon}>🔒</div>
          <div style={styles.featureTitle}>Secure</div>
          <div style={styles.featureDesc}>Encrypted data</div>
        </div>
        <div style={styles.feature} onMouseOver={(e) => e.currentTarget.style.boxShadow = '0 4px 12px rgba(0,0,0,0.08)'} onMouseOut={(e) => e.currentTarget.style.boxShadow = 'none'}>
          <div style={styles.featureIcon}>⚡</div>
          <div style={styles.featureTitle}>Fast</div>
          <div style={styles.featureDesc}>Instant results</div>
        </div>
      </div>
    </div>
  )
}

