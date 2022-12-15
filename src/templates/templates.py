
class Templates:
  def api_client():
    return """
import axios from "axios";

const api_client = axios.create({
  baseURL: process.env.REACT_APP_API_URL,
  headers: {
    "Content-Type": "application/json",
    Accept: "application/json",
  },
});

api_client.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem("token");
    if (token) {
      config.headers["Authorization"] = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    Promise.reject(error);
  }
);

export default api_client;
  """

  def app_js():
    return """
import React from "react";

export default function App() {
  return (
    <div className="flex w-full h-screen flex-col items-center justify-center">
      <h1 className="text-xl font-bold text-center text-gray-800">
        This app was created by DevSetup CLI 🎉
      </h1>
    </div>
  );
}"""
  
  def index_js():
    return """
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import ApplicationRoutes from './routes/ApplicationRoutes';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <ApplicationRoutes />
  </React.StrictMode>
);
  """

  def index_css():
    return """
  @tailwind base;
  @tailwind components;
  @tailwind utilities;
  """
  
  def tailwind_config():
    return """
  module.exports = {
    content: ["./src/**/*.{js,jsx,ts,tsx}"],
    darkMode: "class",
    theme: {
      screens: {
        sm: "320px",
        md: "768px",
      },
      extend: {
        colors: {
          dark: {
            background: {
              base: "",
              neutral: "",
              primary: "",
              secondary: "",
              light: "",
            },
            typography: {
              base: "",
              primary: "",
              secondary: "",
              light: "",
              danger: "",
            },
          },
          background: {
            base: "",
            neutral: "",
            primary: "",
            secondary: "",
            light: "",
          },
          typography: {
            base: "",
            primary: "",
            secondary: "",
            light: "",
            danger: "",
          },
      },
      keyframes: {
        "slide-in": {
          "0%": { transform: "translateX(-100%)" },
          "100%": { transform: "translateX(0)" },
        },
        "slide-up": {
          "0%": { transform: "translateY(100%)" },
          "100%": { transform: "translateY(0)" },
        },
        "fade-in": {
          "0%": { opacity: 0 },
          "100%": { opacity: 1 },
        },
        "spin": {
          "0%": { transform: "rotate(0deg)" },
          "100%": { transform: "rotate(360deg)" },
        },
      },
      animation: {
        "slide-in": "slide-in 0.7s cubic-bezier(0.230, 1.000, 0.320, 1.000) both",
        "slide-up": "slide-up 0.7s cubic-bezier(0.230, 1.000, 0.320, 1.000) both",
        "fade-in": "fade-in 0.2s cubic-bezier(0.230, 1.000, 0.320, 1.000) both",
        "spin": "spin 1s linear infinite",
      },
    },
    plugins: [],
  }
}"""
  
  def application_routes():
    return """
import React, { createContext, useState, useEffect } from 'react'
import { Toaster } from 'react-hot-toast';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'

//pages
import Auth from '../pages/Auth';

//routes
import AuthenticatedRoutes from "./AuthenticatedRoutes";

//context
export const ThemeContext = createContext();

export default function ApplicationRoutes() {
  const [isDarkTheme, setIsDarkTheme] = useState(false)

  useEffect(() => {
    const theme = localStorage.getItem('theme')
    if (theme === 'dark') {
      setIsDarkTheme(true)
    }
  }, [])

  useEffect(() => {
    (isDarkTheme) ? localStorage.setItem('theme', 'dark') : localStorage.setItem('theme', 'light')
  }, [isDarkTheme])

  return (
    <ThemeContext.Provider value={{ isDarkTheme, switchTheme: () => setIsDarkTheme(!isDarkTheme) }}>
      <Router>
        <div className={isDarkTheme ? "dark" : ""}>
          <Routes>
            <Route path="/home/*" element={<AuthenticatedRoutes />} />
            <Route path="/login" element={<Auth is_login />} />
            <Route path="/signup" element={<Auth />} />
            <Route path="/*" element={<Auth is_login />} />
          </Routes>
        </div>
        <Toaster position="top-right" />
      </Router>
    </ThemeContext.Provider>
  );
}
  """
  
  def authenticated_routes():
    return """
import React from 'react'
import { Routes, Route } from "react-router-dom";

//pages
import Home from '../pages/Home';

export default function AuthenticatedRoutes() {
  return (
    <Routes>
      <Route path="/*" element={<Home />} />
    </Routes>
  )
}
"""

  def auth_index_js():
    return """
import React from 'react'

export default function Auth({ is_login }) {
  return (
    <div className='w-full h-screen flex items-center justify-center'>
      <div className="flex flex-col items-center justify-center gap-2">
        <p>
          {is_login ? 'Login' : 'Signup'}
        </p>
        <input type="email" placeholder="email" />
        <input type="password" placeholder="Password" />
        <button className='px-2 py-1 bg-[#ddd] border-[2px] border-[#000] rounded-md'>{is_login ? 'Login' : 'Signup'}</button>
      </div>
    </div>
  )
}
"""
  
  def home_index_js():
    return """
import React from "react";

export default function App() {
  return (
    <div className="flex w-full h-screen flex-col items-center justify-center">
      <h1 className="text-xl font-bold text-center text-gray-800">
        This app was created by DevSetup CLI 🎉
      </h1>
    </div>
  );
}"""