import React, { useState } from "react";

const dummyRequests = [
  {
    id: 1,
    name: "Marc Demo",
    rating: "3.8/5",
    offered: ["JavaScript", "React"],
    wanted: ["Photoshop", "Figma"],
    status: "pending",
    profilePic: "./avatar.png",
  },
  {
    id: 2,
    name: "Michell",
    rating: "3.5/5",
    offered: ["HTML", "CSS"],
    wanted: ["UI Design"],
    status: "rejected",
    profilePic: "./avatar.png",
  },
];

const SwapRequests = () => {
  const [filter, setFilter] = useState("pending");

  const handleStatusUpdate = (id, newStatus) => {
    console.log(`Request ${id} marked as ${newStatus}`);
    // backend update logic
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

        {/* Content */}
        <div className="relative z-10 px-6 py-10 mt-28">
          {/* Filter Section */}
          <div className="flex flex-col sm:flex-row justify-between gap-4 mb-6">
            <select
              value={filter}
              onChange={(e) => setFilter(e.target.value)}
              className="bg-white/20 text-white border border-white/30 rounded-md p-2 backdrop-blur-md"
            >
              <option value="pending">Pending</option>
              <option value="accepted">Accepted</option>
              <option value="rejected">Rejected</option>
            </select>

            <input
              type="text"
              placeholder="Search..."
              className="bg-white/20 text-white placeholder-white border border-white/30 rounded-md px-4 py-2 backdrop-blur-md w-full sm:w-1/3"
            />
          </div>

          {/* Request Cards */}
          <div className="space-y-6">
            {dummyRequests
              .filter((req) => req.status === filter)
              .map((req) => (
                <div
                  key={req.id}
                  className="bg-white/20 text-white border border-white/30 backdrop-blur-md p-6 rounded-2xl shadow-lg flex justify-between items-center"
                >
                  {/* Left: User Info */}
                  <div className="flex gap-4 items-start">
                    <img
                      src={req.profilePic}
                      alt="Profile"
                      className="h-16 w-16 rounded-full border-2 border-white object-cover"
                    />
                    <div>
                      <h2 className="text-xl font-bold">{req.name}</h2>
                      <p className="text-sm text-white/80 mb-2">Rating: {req.rating}</p>
                      <div className="text-sm mb-1">
                        <strong className="text-green-300">Offered:</strong>{" "}
                        {req.offered.map((skill) => (
                          <span
                            key={skill}
                            className="bg-green-100 text-black rounded-full px-2 py-1 mx-1 text-xs"
                          >
                            {skill}
                          </span>
                        ))}
                      </div>
                      <div className="text-sm">
                        <strong className="text-blue-300">Wanted:</strong>{" "}
                        {req.wanted.map((skill) => (
                          <span
                            key={skill}
                            className="bg-blue-100 text-black rounded-full px-2 py-1 mx-1 text-xs"
                          >
                            {skill}
                          </span>
                        ))}
                      </div>
                    </div>
                  </div>

                  {/* Right: Status + Action */}
                  <div className="text-right space-y-2">
                    <p className="font-semibold">
                      Status:{" "}
                      <span
                        className={
                          req.status === "pending"
                            ? "text-yellow-300"
                            : req.status === "accepted"
                            ? "text-green-300"
                            : "text-red-300"
                        }
                      >
                        {req.status.charAt(0).toUpperCase() + req.status.slice(1)}
                      </span>
                    </p>

                    {req.status === "pending" && (
                      <div className="flex gap-2 justify-end">
                        <button
                          onClick={() => handleStatusUpdate(req.id, "accepted")}
                          className="bg-green-500 hover:bg-green-600 text-white text-xs px-3 py-1 rounded-md"
                        >
                          Accept
                        </button>
                        <button
                          onClick={() => handleStatusUpdate(req.id, "rejected")}
                          className="bg-red-500 hover:bg-red-600 text-white text-xs px-3 py-1 rounded-md"
                        >
                          Reject
                        </button>
                      </div>
                    )}
                  </div>
                </div>
              ))}
          </div>

          {/* Pagination */}
          <div className="flex justify-center mt-8 gap-2">
            {[1, 2, 3].map((page) => (
              <button
                key={page}
                className="px-3 py-1 bg-white/10 text-white border border-white/30 rounded-md hover:bg-white/20"
              >
                {page}
              </button>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default SwapRequests;
