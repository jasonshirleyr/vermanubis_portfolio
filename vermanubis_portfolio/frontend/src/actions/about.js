import axios from "axios";

import { GET_ABOUT } from "./types";

// GET_ABOUT
export const getAbout = () => (dispatch) => {
  // axios rest call to get the information on the about section from the database
  axios
    .get("/api/about/")
    .then((res) => {
      dispatch({
        type: GET_ABOUT,
        payload: res.data,
      });
    })
    .catch((err) => console.log(err));
};
