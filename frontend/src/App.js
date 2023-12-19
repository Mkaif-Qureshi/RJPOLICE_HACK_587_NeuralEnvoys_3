import React from "react";
import "./App.css";
import { BrowserRouter, Routes, Route, Switch } from "react-router-dom";
import Footer from "./Components/Footer/Footer";
import Navbar from "./Components/Navbar/Navbar";
import Slider from "./Components/Slider/Slider";
import Home from "./Components/Pages/Home";
import Admin from "./Components/Pages/Admin";
import Login from "./Components/Pages/Login";

function App() {
  return (
    <div>
      <BrowserRouter>
        

        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/cameraList" element={<Home view="" />} />
          <Route path="/emergency" element={<Home view="" />} />
          <Route path="/alert" element={<Home view="" />} />
          <Route path="/admin" element={<Admin view="" />} />
          <Route path="/login" element={<Login />} />
          <Route path="/submit" element={<Login />} />
        </Routes>
        <Footer />
      </BrowserRouter>
    </div>
  );
}

export default App;
