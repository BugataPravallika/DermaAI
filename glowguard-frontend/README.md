# Frontend - GlowGuard React Application

## Project Structure

```
src/
├── components/          # React components
│   └── Layout/         # Header, Footer, Layout
├── pages/              # Page components
├── styles/             # CSS files
├── utils/              # API client, store (Zustand)
├── assets/             # Images, fonts, static files
└── App.jsx             # Root component
```

## Key Technologies

- **React 18** - UI framework
- **Vite** - Build tool
- **Tailwind CSS** - Styling
- **React Router** - Navigation
- **Zustand** - State management
- **Axios** - HTTP client
- **Framer Motion** - Animations
- **React Icons** - Icon library
- **React Toastify** - Notifications
- **React Image Crop** - Image cropping

## Setup

1. Install dependencies:
   ```bash
   npm install
   ```

2. Start development server:
   ```bash
   npm run dev
   ```

3. Build for production:
   ```bash
   npm run build
   ```

## File Organization

### Components
- `Layout/Header.jsx` - Navigation header
- `Layout/Footer.jsx` - Footer with links
- `ImageUpload.jsx` - Image upload component

### Pages
- `Home.jsx` - Landing page
- `Upload.jsx` - Image analysis page
- `Results.jsx` - Prediction results page
- `Profile.jsx` - User profile page
- `Blog.jsx` - Blog/articles page
- `BeforeAfter.jsx` - Gallery showcase
- `Login.jsx` - Login page
- `Register.jsx` - Registration page
- `NotFound.jsx` - 404 page

### Utils
- `api.js` - Axios instance with interceptors
- `store.js` - Zustand stores (auth, predictions)

### Styles
- `globals.css` - Global styles and animations
- `index.css` - Entry CSS file

## Environment Variables

Create `.env.local`:
```
VITE_API_URL=http://localhost:8000/api
```

## Features Implemented

- ✅ User authentication (login/register)
- ✅ Image upload with drag-and-drop
- ✅ API integration
- ✅ Beautiful UI with Tailwind CSS
- ✅ Responsive design
- ✅ Pastel color theme
- ✅ Smooth animations
- ✅ Toast notifications
- ✅ Protected routes (with auth)

## Styling

### Color Palette
- Primary Pink: `from-pink-400 to-rose-400`
- Lavender: `from-purple-300`
- Pastel Theme: Used throughout

### Components
- Buttons: `.btn-primary`, `.btn-secondary`
- Cards: `.card`
- Animations: `.animate-float`, `.card-hover`

## State Management (Zustand)

```javascript
import { useAuthStore, usePredictionStore } from '@/utils/store'

// Auth store
const { user, token, logout } = useAuthStore()

// Prediction store
const { predictions, addPrediction } = usePredictionStore()
```

## API Integration

```javascript
import api from '@/utils/api'

// Example: Upload and analyze
const response = await api.post('/predictions/analyze', formData)
```

## Development Tips

1. **Hot Reload**: Changes automatically reload in browser
2. **Tailwind**: Add classes directly in JSX
3. **Icons**: Browse React Icons library - `<FiUpload />`
4. **State**: Use Zustand for global state
5. **API**: Use `api` instance for consistency

## Build Output

```bash
npm run build
```

Creates `dist/` folder ready for deployment on:
- Vercel
- Netlify
- GitHub Pages
- AWS S3 + CloudFront

---

For more documentation, see `../README.md`
