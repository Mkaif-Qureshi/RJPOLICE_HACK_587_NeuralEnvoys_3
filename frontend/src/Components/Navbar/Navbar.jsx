import React from "react";
import "./Navbar.css";
import emblem from "../Assets/photos/Emblem.png";
import pLogo from "../Assets/photos/Police_Logo.png";
import rajMap from "../Assets/photos/rajasthan.gif";
import { Link } from "react-router-dom";

function Navbar() {
  const [value, setValue] = React.useState("");

  return (
    <div>
      <div>
        <nav className="App-nav">
          <img src={pLogo} alt="police logo" />
          <ul>
            <Link
              to="/"
              onClick={() => {
                return setValue("home");
              }}
            >
              Home
              {value == "home" ? <hr /> : <></>}
            </Link>

            <Link
              to="/admin"
              onClick={() => {
                return setValue("admin");
              }}
            >
              Admin
              {value == "admin" ? <hr /> : <></>}
            </Link>
            <Link
              to="/cameraList"
              onClick={() => {
                return setValue("cameraList");
              }}
            >
              Camera List
              {value == "cameraList" ? <hr /> : <></>}
            </Link>
            <Link
              to="/emergency"
              onClick={() => {
                return setValue("emergeny");
              }}
            >
              Emergency
              {value == "emergeny" ? <hr /> : <></>}
            </Link>
            <Link
              to="/alert"
              onClick={() => {
                return setValue("alert");
              }}
            >
              Alert
              {value == "alert" ? <hr /> : <></>}
            </Link>
          </ul>
          <div className="btns">
            <button>
              <Link to="/login">Login</Link>
            </button>
            <button>Lang / भाषा</button>
          </div>
        </nav>
      </div>
    </div>
  );
}

export default Navbar;
