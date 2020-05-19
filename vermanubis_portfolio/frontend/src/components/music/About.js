import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getAbout } from "../../actions/about";

/**
 * About will build the "About" section of Music
 */
export class About extends Component {
  static propTypes = {
    about: PropTypes.string.isRequired,
  };

  componentDidMount() {
    this.props.getAbout();
  }

  render() {
    return (
      <Fragment>
        <div className="content container justify-content-center align-self-center text-center">
          <h1>ABOUT</h1>
          <p>{this.props.about}</p>
        </div>
      </Fragment>
    );
  }
}

const mapStateToProps = (state) => ({
  about: state.music.about,
});

export default connect(mapStateToProps, { getAbout })(About);
