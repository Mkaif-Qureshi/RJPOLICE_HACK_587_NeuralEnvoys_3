import React from "react";
import emblem from "../Assets/photos/Emblem.png";
import policeLogo from "../Assets/photos/Police_Logo.png";
import rajMap from "../Assets/photos/rajasthan.gif";
import "./CSS/Login.css";
import Slider from "../Slider/Slider";
import { Link } from "react-router-dom";

function Login() {
  /*  function direct(){

    }
 */
  return (
    <div>
      <nav className="App-nav">
        <div className="navImages left">
          <img src={emblem} alt="emblem logo" />
          <img src={policeLogo} alt="police logo" />
        </div>
        <h1>Rajasthan Police</h1>
        <div className="navImages right">
          <img src={rajMap} alt="rajasthan map" />
        </div>
      </nav>

      <Slider />

      <div className="continue display"></div>
      <div className="image-box">
        {/*         <img src={comp} alt="comp images" />
         */}{" "}
        <div className="login">
          <div className="login-top">
            <h3>LOGIN</h3>
          </div>
          <div className="login-content">
            <p>District</p>
            <input></input>
            <p>Username</p>
            <input></input>
            <p>Password</p>
            <input></input>
            <div className="login-bottom">
              <a>go to Admin </a>
              <button>
                <Link to="/">submit</Link>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Login;
