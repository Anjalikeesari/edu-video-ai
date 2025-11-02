import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Summary from './pages/Summary';
import Quiz from './pages/Quiz';
import Navbar from './components/Navbar';

export default function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <div style={{ padding: 20 }}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/summary/:id" element={<Summary />} />
          <Route path="/quiz/:id" element={<Quiz />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}
