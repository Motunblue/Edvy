import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Header from './header';
import Home from './home';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Header />
    <Home />
  </React.StrictMode>
);
