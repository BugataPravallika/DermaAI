import { create } from 'zustand'

export const useAuthStore = create((set) => ({
  user: null,
  token: localStorage.getItem('access_token') || null,
  loading: false,

  setUser: (user) => set({ user }),
  setToken: (token) => {
    localStorage.setItem('access_token', token)
    set({ token })
  },
  setLoading: (loading) => set({ loading }),

  logout: () => {
    localStorage.removeItem('access_token')
    set({ user: null, token: null })
  },

  isAuthenticated: () => !!localStorage.getItem('access_token'),
}))

export const usePredictionStore = create((set) => ({
  predictions: [],
  currentPrediction: null,
  loading: false,

  setPredictions: (predictions) => set({ predictions }),
  setCurrentPrediction: (prediction) => set({ currentPrediction: prediction }),
  setLoading: (loading) => set({ loading }),

  addPrediction: (prediction) => set((state) => ({
    predictions: [prediction, ...state.predictions]
  })),
}))
