import React from 'react'
import { Outlet } from "react-router-dom";
import Navbar from '../components/Navbar';

const Layout = () => {
  return (
    <div className="app ">
      <main className="content">
        <Navbar/>
        <Outlet />
      </main>
    </div>
  )
}

export default Layout