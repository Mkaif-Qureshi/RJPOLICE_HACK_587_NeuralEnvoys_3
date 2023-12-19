import React from "react";
import video from "../Assets/video/video.mp4";
import "./CSS/Home.css";
import Navbar from "../Navbar/Navbar";
import Slider from "../Slider/Slider";

function Home() {
  return (
    <>
      <Navbar />
      <Slider />
      <div className="footage">
        <video controls loop autoplay src={video}></video>
        <video controls loop autoplay src={video}></video>
        <video controls loop autoplay src={video}></video>
        <video controls loop autoplay src={video}></video>
        <video controls loop autoplay src={video}></video>
        <video controls loop autoplay src={video}></video>
        <video controls loop autoplay src={video}></video>
        <video controls loop autoplay src={video}></video>

        <div className="chatbox">
          <div></div>
        </div>
      </div>
    </>
  );
}

export default Home;
