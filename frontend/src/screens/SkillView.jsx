import React, { useState } from "react";

const SkillView = () => {
  const [showRequestModal, setShowRequestModal] = useState(false);
  const [offeredSkill, setOfferedSkill] = useState("");
  const [wantedSkill, setWantedSkill] = useState("");
  const [message, setMessage] = useState("");

  const user = {
    name: "Marc Demo",
    photo: "./avatar.png",
    rating: 4.3,
    offeredSkills: ["JavaScript", "React", "Node.js"],
    wantedSkills: ["Photoshop", "Figma", "Graphic Design"],
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log({ offeredSkill, wantedSkill, message });
    setShowRequestModal(false);
  };

  return (
    <div className="min-h-screen w-full flex flex-col top-0 absolute">
      {/* Background Section */}
      <div
        className="relative h-[98vh] bg-cover bg-center bg-no-repeat rounded-4xl m-2"
        style={{ backgroundImage: "url('./background1.jpg')" }}
      >
        {/* Overlay */}
        <div className="absolute inset-0 bg-black/30 rounded-4xl z-0" />

        {/* Skill View Content */}
        <div className="relative z-10 px-6 py-10 mt-28">
          {/* Skill Card */}
          <div className="bg-white/20 backdrop-blur-md border border-white/30 text-white p-8 rounded-3xl shadow-xl flex justify-between items-center mb-8">
            {/* Left Info */}
            <div className="space-y-4">
              <h2 className="text-3xl font-bold">{user.name}</h2>

              <div>
                <p className="font-semibold text-green-200 mb-1">Skills Offered:</p>
                <div className="flex gap-2 flex-wrap">
                  {user.offeredSkills.map((skill) => (
                    <span key={skill} className="bg-green-100 text-black text-sm px-3 py-1 rounded-full">
                      {skill}
                    </span>
                  ))}
                </div>
              </div>

              <div>
                <p className="font-semibold text-blue-200 mt-2 mb-1">Skills Wanted:</p>
                <div className="flex gap-2 flex-wrap">
                  {user.wantedSkills.map((skill) => (
                    <span key={skill} className="bg-blue-100 text-black text-sm px-3 py-1 rounded-full">
                      {skill}
                    </span>
                  ))}
                </div>
              </div>

              <p className="text-sm opacity-80">Rating: {user.rating} / 5</p>
            </div>

            {/* Right Profile Image + Button */}
            <div className="flex flex-col items-center gap-4">
              <img
                src={user.photo}
                alt="Profile"
                className="w-28 h-28 rounded-full border-2 border-white object-cover"
              />
              <button
                onClick={() => setShowRequestModal(true)}
                className="bg-white text-black font-semibold px-6 py-2 rounded-xl hover:bg-gray-100"
              >
                Request
              </button>
            </div>
          </div>

          {/* Feedback Placeholder */}
          <div className="bg-white/20 text-white backdrop-blur-md border border-white/30 p-6 rounded-3xl shadow-md">
            <h3 className="font-semibold text-lg mb-2">Rating and Feedback</h3>
            <p className="text-sm text-white/80 italic">No feedback yet.</p>
          </div>
        </div>

        {/* Modal */}
        {showRequestModal && (
          <div className="fixed inset-0 bg-black/40 flex justify-center items-center z-20">
            <div className="bg-white/20 backdrop-blur-md text-white border border-white/30 p-6 rounded-3xl shadow-xl w-[90%] max-w-md relative">
              <h2 className="text-xl font-bold mb-4">Send Swap Request</h2>
              <form onSubmit={handleSubmit} className="flex flex-col gap-4">
                <div>
                  <label className="text-sm font-medium mb-1 block">
                    Choose one of your offered skills:
                  </label>
                  <select
                    required
                    value={offeredSkill}
                    onChange={(e) => setOfferedSkill(e.target.value)}
                    className="bg-white text-black px-4 py-2 rounded-md w-full"
                  >
                    <option value="">-- Select --</option>
                    {["JavaScript", "HTML", "CSS"].map((skill) => (
                      <option key={skill} value={skill}>
                        {skill}
                      </option>
                    ))}
                  </select>
                </div>

                <div>
                  <label className="text-sm font-medium mb-1 block">
                    Choose one of their wanted skills:
                  </label>
                  <select
                    required
                    value={wantedSkill}
                    onChange={(e) => setWantedSkill(e.target.value)}
                    className="bg-white text-black px-4 py-2 rounded-md w-full"
                  >
                    <option value="">-- Select --</option>
                    {user.wantedSkills.map((skill) => (
                      <option key={skill} value={skill}>
                        {skill}
                      </option>
                    ))}
                  </select>
                </div>

                <div>
                  <label className="text-sm font-medium mb-1 block">Message</label>
                  <textarea
                    value={message}
                    onChange={(e) => setMessage(e.target.value)}
                    className="w-full px-4 py-2 rounded-md bg-white text-black"
                    placeholder="Write a short message..."
                    rows={4}
                  ></textarea>
                </div>

                <div className="flex justify-between mt-2">
                  <button
                    type="button"
                    onClick={() => setShowRequestModal(false)}
                    className="text-red-300 hover:underline"
                  >
                    Cancel
                  </button>
                  <button
                    type="submit"
                    className="bg-white text-black font-semibold px-6 py-2 rounded-md"
                  >
                    Submit
                  </button>
                </div>
              </form>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default SkillView;
