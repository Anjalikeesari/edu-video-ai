import React from 'react';
import { Link } from 'react-router-dom';
export default function Navbar() {
  return (
    <nav style={{ padding: 10, borderBottom: '1px solid #eee' }}>
      <Link to="/">Home</Link> | <Link to="/profile">Profile</Link>
    </nav>
  );
}
