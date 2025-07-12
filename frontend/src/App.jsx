import React from "react";
import Home from "./screens/Home";
import { Routes, Route } from "react-router-dom";
import Layout from "./layout/Layout";
import Login from "./screens/Login";
import Register from "./screens/Register";
import SkillSwapList from "./components/SkillSwapList";
import UserProfile from "./screens/Profile";
import SwapRequests from "./screens/SwapRequests";
import SkillView from "./screens/SkillView";

const App = () => {
  return (
    <Routes>
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register/>} />
      <Route element={<Layout />}>
        <Route path="/" element={<Home/>} />
        <Route path="/skilllist" element={<SkillSwapList/>} />
        <Route path="/profile" element={<UserProfile/>} />
        <Route path="/requests" element={<SwapRequests/>} />
        <Route path="/view" element={<SkillView/>} />
      </Route>
    </Routes>
  );
};

export default App;
