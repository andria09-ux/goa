import React from 'react'
import { Route, Routes } from 'react-router'
import Home from './pages/home'
import about from './pages/about'
import footer from './pages/footer'

export default function App() {
  return (
    <div>
      <Routes>
      <Route path="/home" element={<Home />} />
    </Routes>

    <Routes>
      <Route path="/about" element={<About />} />
    </Routes>

    <Routes>
      <Route path="/footer" element={<footer />} />
    </Routes>
    </div>
  )
}
