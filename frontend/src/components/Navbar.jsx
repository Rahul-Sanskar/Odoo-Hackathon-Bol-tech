import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom';



const Navbar = () => {
  const [isLoggedIn,setIsLoggedIn]=useState(false);
   const navigate = useNavigate();
  return (
    <div className='backdrop-blur-md bg-white/10 dark:bg-gray-900/10 border-b border-white/20 dark:border-gray-700 h-18 flex justify-between sticky top-0 z-50 shadow-md px-10 rounded-3xl m-4 mt-5'>
      {/* logo and sidebar collapse icon */}
      <div className="  flex items-center justify-start gap-3 px-2">
        <span className=' font-extrabold'>skill-swap</span>
      </div>
      <div className=" flex items-center justify-end gap-0 px-4">
        {isLoggedIn?
        <div className="bg-gray-300 h-10 w-10 rounded-full overflow-hidden">
          <img
            src="./vite.svg"
            alt="img"
            className="object-cover w-full h-full"
          />
        </div>:
        <>
        <button onClick={()=>navigate("/login")} className="w-33 px-3 py-2 border text-dark font-bold rounded-4xl">Log in</button>
        <button onClick={()=>navigate("/register")} className="w-33 px-3 py-2 border text-dark font-bold rounded-4xl">Sign up</button>
        </>
        }
      </div>
    </div>
  )
}

export default Navbar