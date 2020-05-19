import { GET_ABOUT } from "../actions/types.js";

const initialState = {
  about: "",
};

export default function (state = initialState, action) {
  switch (action.type) {
    // get the information on the "about" section of the music page from the database
    case GET_ABOUT:
      var lastElement = action.payload[action.payload.length - 1]; // get the last inserted 'about' info from the database
      var payload = lastElement.about;
      return {
        ...state,
        about: payload,
      };
    default:
      return state;
  }
}
