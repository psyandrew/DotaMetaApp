import React from 'react';
import ReactDOM from 'react-dom/client';
import {createBrowserRouter, RouterProvider} from 'react-router-dom';


import HomePage from './pages/HomePage/HomePage';
import Profile from './pages/ProfilePage/ProfilePage';


const router = createBrowserRouter([

  { 
    path: '/',
    element: <HomePage />
  },
  { 
    path: '/hero/:heroid', 
    element: <Profile />
  }

  ]);

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
);
