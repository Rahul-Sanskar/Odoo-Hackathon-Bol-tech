import React from 'react';

const users = [
  {
    name: 'Marc Demo',
    skillsOffered: ['JavaScript', 'Python'],
    skillsWanted: ['Photoshop', 'Graphic Designer'],
    rating: 3.5,
  },
  {
    name: 'Michell',
    skillsOffered: ['JavaScript', 'Python'],
    skillsWanted: ['Photoshop', 'Graphic Designer'],
    rating: 2.5,
  },
  {
    name: 'Joe Wills',
    skillsOffered: ['JavaScript', 'Python'],
    skillsWanted: ['Photoshop', 'Graphic Designer'],
    rating: 4.0,
  },
];

const SkillCard = ({ user }) => (
  <div className="bg-white/10 backdrop-blur-lg border border-white/20 rounded-3xl p-6 mb-2 shadow-md flex items-start gap-6">
    <div className="w-24 h-24 rounded-full bg-gray-300 flex items-center justify-center text-lg font-bold">
      Photo
    </div>
    <div className="flex-1">
      <h3 className="text-xl font-bold text-white mb-2">{user.name}</h3>
      <p className="text-green-800 font-semibold">Skills Offered : {user.skillsOffered.join(', ')}</p>
      <p className="text-blue-900 font-semibold mb-2">Skill Wanted : {user.skillsWanted.join(', ')}</p>
      <p className="text-white">Rating: {user.rating}/5</p>
    </div>
    <div className="flex items-center">
      <button className="bg-blue-400 text-white font-bold px-4 py-2 rounded-lg hover:bg-blue-500">Request</button>
    </div>
  </div>
);

const SkillSwapList = () => {
  return (
    <div className="min-h-screen w-full flex flex-col top-0 absolute">
       
     <div
        className="relative h-[98vh] bg-cover bg-center bg-no-repeat rounded-4xl m-2 "
        style={{ backgroundImage: "url('./background1.jpg')" }}
      >
        <div className="absolute inset-0 bg-black/20 rounded-4xl z-0" />
      <div className="relative max-w-4xl mx-auto mt-25">
        <div className="flex items-center justify-between mb-6">
          <select className="bg-white/20 text-white p-2 rounded-xl">
            <option>Availability</option>
          </select>
          <input
            type="text"
            placeholder="Search"
            className="bg-white/20 text-white px-4 py-2 rounded-xl ml-2 focus:outline-none"
          />
        </div>
        {users.map((user, index) => (
          <SkillCard key={index} user={user} />
        ))}
        <div className="flex justify-center mt-6 gap-2 text-black">
          {[1, 2, 3, 4, 5, 6, 7].map((page) => (
            <button
              key={page}
              className="bg-white px-3 py-1 rounded-lg hover:bg-gray-300"
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

export default SkillSwapList;
