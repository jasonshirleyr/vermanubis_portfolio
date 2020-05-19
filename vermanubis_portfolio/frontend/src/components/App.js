import React, { Component, Fragment } from "react";
import ReactDOM from "react-dom";
import "./App.css";

import Header from "./layout/Header";
import Parallax from "./music/Parallax";
import About from "./music/About";
import Music from "./music/Music";

import { Provider } from "react-redux";
import store from "../store";

class App extends React.Component {
  render() {
    return (
      <Provider store={store}>
        <Fragment>
          <Header />
          <div className="main container-fluid">
            <Parallax />
            <About />
            <Music />
          </div>
        </Fragment>
      </Provider>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("app"));
