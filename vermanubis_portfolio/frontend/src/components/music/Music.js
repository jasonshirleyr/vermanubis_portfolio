import React, { Component } from "react";

export class Music extends Component {
  render() {
    return (
      <div className="container justify-content-center align-self-center text-center">
        <h3>MUSIC</h3>
        <iframe
          width="560"
          height="315"
          src="https://www.youtube.com/embed/iwmR72iFGm4"
          frameborder="0"
          allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen
        ></iframe>
        <iframe
          className="music"
          src="https://bandcamp.com/EmbeddedPlayer/track=909623317/size=small/bgcol=ffffff/linkcol=0687f5/transparent=true/"
          seamless
        >
          <a href="http://nevisumbra.bandcamp.com/track/grief-my-sword">
            Grief, My Sword by Vermanubis
          </a>
        </iframe>
      </div>
    );
  }
}

export default Music;
