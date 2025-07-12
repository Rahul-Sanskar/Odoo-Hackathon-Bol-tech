import React from "react";
import { FiArrowDown } from "react-icons/fi";
import SkillSwapList from "../components/SkillSwapList";
import { Navigate, useNavigate } from "react-router-dom";

const Home = () => {
  const navigate =useNavigate();
  return (
    <div className="min-h-screen w-full flex flex-col top-0 absolute">
      {/* Background Image */}
      <div
        className="relative h-[98vh] bg-cover bg-center bg-no-repeat rounded-4xl m-2"
        style={{ backgroundImage: "url('./background1.jpg')" }}
      >
        {/* Dark Overlay */}
        <div className="absolute inset-0 bg-black/20 rounded-4xl z-0" />

        {/* Hero Content */}
        <div className="relative z-10 flex flex-col h-full justify-between py-10 items-center text-white px-6 mt-5">
          {/* <h4 className="text-xl font-semibold mb-2">SkillSwap</h4> */}
          <div></div>
          <div className="flex flex-col justify-center items-center">

          <h1 className="text-[12rem] leading-none font-extrabold text-center font-sans ">skill-swap</h1>
          <p className="mt-4 max-w-xl text-center text-lg font-medium">
            SkillSwap is a platform where you exchange skills—not money. Share what you know, learn what you need, and grow together.
          </p>
          </div>

          {/* Buttons + Arrow */}
          <div className="flex justify-between items-end w-full px-10 mt-10 ">
            {/* Left glass card */}
            <div className="flex">

            <div className="bg-white/10 backdrop-blur-md text-white p-6 rounded-3xl max-w-xs border border-white/30 w-60">
              <h3 className="text-3xl font-bold mb-2">100+ Skills</h3>
              <p className="text-sm">We help people swap knowledge to grow together.</p>
            </div>
            <div className="bg-white/10 backdrop-blur-md text-white p-6 rounded-3xl max-w-xs border border-white/30">
               <div className="flex flex-col items-center -space-y-5">
                <img src="https://images-cdn.openxcell.com/wp-content/uploads/2024/07/25085005/reactjs-inner.svg" alt="img1" className="w-14 h-14 rounded-full border-2 border-white object-cover" />
                <img src="./jsskill.png" alt="img2" className="w-14 h-14 rounded-full border-2 border-white object-cover" />
                <img src="./htm.png" alt="img3" className="w-14 h-14 rounded-full border-2 border-white object-cover" />
               </div>
            </div>
            </div>

            {/* Arrow & CTA */}
            <div className="flex flex-col items-end gap-6 ">
              <button  className="w-16 h-16 border-2 border-white rounded-full flex items-center justify-center">
                <FiArrowDown className="text-3xl" strokeWidth={1.5} />
              </button>
              <button onClick={()=>navigate("/skilllist")} className="bg-white text-black font-semibold px-6 py-3 rounded-2xl border border-black w-60 h-22">
                Explore Skills
              </button>
            </div>
          </div>
        </div>
      </div>

    
    </div>
  );
};

export default Home;
