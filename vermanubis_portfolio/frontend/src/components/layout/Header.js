import React, { Component } from "react";

export class Header extends Component {
  render() {
    return (
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <div className="container">
          <a className="navbar-brand" href="#">
            Vermanubis Portfolio
          </a>
          <button
            className="navbar-toggler"
            type="button"
            data-toggle="collapse"
            data-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          {/* Navbar Dropdown For Music */}
          <div className="collapse navbar-collapse" id="navbarSupportedContent">
            <ul className="navbar-nav mr-auto">
              <li className="nav-item dropdown">
                <a
                  className="nav-link dropdown-toggle"
                  href="#"
                  id="navbarDropdown"
                  role="button"
                  data-toggle="dropdown"
                  aria-haspopup="true"
                  aria-expanded="false"
                >
                  Music
                </a>
                <div
                  className="dropdown-menu text-dark bg-dark"
                  aria-labelledby="navbarDropdown"
                >
                  <a className="dropdown-item badge-dark" href="#">
                    About
                  </a>
                  <a className="dropdown-item badge-dark" href="#">
                    Music
                  </a>
                  <div className="dropdown-divider badge-dark"></div>
                  <a className="dropdown-item badge-dark" href="#">
                    Contact
                  </a>
                </div>
              </li>
              <li className="nav-item"></li>
              <li className="nav-item"></li>
            </ul>
          </div>
        </div>
      </nav>
    );
  }
}

export default Header;
