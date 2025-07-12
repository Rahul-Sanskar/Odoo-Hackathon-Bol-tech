import React, { useState } from "react";

const UserProfile = () => {
  const [user, setUser] = useState({
    name: "Marc Demo",
    location: "New York, USA",
    skillsOffered: ["JavaScript", "Python"],
    skillsWanted: ["Photoshop", "Graphic Design"],
    availability: "Weekends",
    profileStatus: "Public",
  });

  return (
    <div className="min-h-screen w-full flex flex-col top-0 absolute">
      {/* Background */}
      <div
        className="relative h-[98vh] bg-cover bg-center bg-no-repeat rounded-4xl m-2"
        style={{ backgroundImage: "url('./background1.jpg')" }}
      >
        {/* Overlay */}
        <div className="absolute inset-0 bg-black/30 rounded-4xl z-0" />

        {/* Profile Content */}
        <div className="relative z-10 mt-28 px-10 py-20">
          <div className="bg-white/20 backdrop-blur-lg rounded-3xl p-8 md:grid md:grid-cols-3 gap-12 text-white shadow-xl border border-white/30">
            
            {/* Left Details */}
            <div className="col-span-2 space-y-6">
              <div>
                <label className="block font-semibold text-sm opacity-80">Name</label>
                <p className="border-b border-white/30 pb-1">{user.name}</p>
              </div>

              <div>
                <label className="block font-semibold text-sm opacity-80">Location</label>
                <p className="border-b border-white/30 pb-1">{user.location}</p>
              </div>

              <div>
                <label className="block font-semibold text-sm opacity-80 mb-1">Skills Offered</label>
                <div className="flex gap-2 flex-wrap">
                  {user.skillsOffered.map((skill, idx) => (
                    <span
                      key={idx}
                      className="px-3 py-1 bg-white/20 rounded-full text-sm border border-white/30"
                    >
                      {skill}
                    </span>
                  ))}
                </div>
              </div>

              <div>
                <label className="block font-semibold text-sm opacity-80">Availability</label>
                <p className="border-b border-white/30 pb-1">{user.availability}</p>
              </div>

              <div>
                <label className="block font-semibold text-sm opacity-80">Profile</label>
                <p className="border-b border-white/30 pb-1">{user.profileStatus}</p>
              </div>
            </div>

            {/* Right Avatar & Skills Wanted */}
            <div className="flex flex-col items-center gap-6">
              <div className="relative w-32 h-32 rounded-full overflow-hidden border-4 border-white/40 shadow-md">
                <img
                  src="./avatar.png"
                  alt="User"
                  className="w-full h-full object-cover"
                />
              </div>
              <p className="text-sm text-red-300 hover:underline cursor-pointer">
                Upload / Remove
              </p>

              <div className="w-full">
                <label className="block font-semibold text-sm opacity-80 text-center mb-1">
                  Skills Wanted
                </label>
                <div className="flex gap-2 flex-wrap justify-center">
                  {user.skillsWanted.map((skill, idx) => (
                    <span
                      key={idx}
                      className="px-3 py-1 bg-white/20 rounded-full text-sm border border-white/30"
                    >
                      {skill}
                    </span>
                  ))}
                </div>
              </div>
            </div>

          </div>
        </div>
      </div>
    </div>
  );
};

export default UserProfile;
