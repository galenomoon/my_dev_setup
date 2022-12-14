
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
      <div className="flex w-full s-screen flex-col items-center justify-center">
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
  import App from './App';

  const root = ReactDOM.createRoot(document.getElementById('root'));
  root.render(
    <React.StrictMode>
      <App />
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
    content: [
      "./src/**/*.{js,jsx,ts,tsx}",
    ],
    theme: {
      extend: {},
    },
    plugins: [],
  }"""