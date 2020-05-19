import React, { Component } from "react";

export class Music extends Component {
  render() {
    return (
      <div className="container justify-content-center align-self-center text-center">
        <h3>MUSIC</h3>
        <iframe
          className="music"
          src="https://bandcamp.com/EmbeddedPlayer/track=785165219/size=small/bgcol=ffffff/linkcol=0687f5/transparent=true/"
          seamless
        >
          <a href="http://nevisumbra.bandcamp.com/track/words-of-grief-and-psalms-of-new-life">
            Words of Grief and Psalms of New Life by Vermanubis
          </a>
        </iframe>
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
