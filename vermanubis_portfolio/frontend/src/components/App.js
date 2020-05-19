import React, { Component, Fragment } from "react";
import ReactDOM from "react-dom";
import "./App.css";

import Header from "./layout/Header";
import Parallax from "./music/Parallax";
import About from "./music/About";

import { Provider } from "react-redux";
import store from "../store";

class App extends React.Component {
  render() {
    return (
      <Provider store={store}>
        <Fragment>
          <Header />
          <div className="container-fluid">
            <Parallax />
            <About />
          </div>
        </Fragment>
      </Provider>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("app"));
