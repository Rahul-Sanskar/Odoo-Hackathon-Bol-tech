import React from 'react';

const Login = () => {
  return (
    <div className="min-h-screen flex items-center justify-center bg-yellow-500 bg-cover bg-center">
      <div className="bg-white/10 backdrop-blur-md border border-white/30 rounded-3xl p-10 w-full max-w-md text-white shadow-lg">
        <h2 className="text-3xl font-extrabold text-center mb-6">Log In to SkillSwap</h2>
        <form className="space-y-4">
          <input
            type="email"
            placeholder="Email"
            className="w-full p-3 rounded-xl bg-white/10 border border-white/30 placeholder-white text-white focus:outline-none"
          />
          <input
            type="password"
            placeholder="Password"
            className="w-full p-3 rounded-xl bg-white/10 border border-white/30 placeholder-white text-white focus:outline-none"
          />
          <button
            type="submit"
            className="w-full py-3 bg-white text-yellow-700 font-semibold rounded-xl hover:bg-yellow-100 transition"
          >
            Log In
          </button>
        </form>
        <p className="text-sm text-center mt-4">
          Don't have an account? <a href="/register" className="underline">Sign Up</a>
        </p>
      </div>
    </div>
  );
};

export default Login;
