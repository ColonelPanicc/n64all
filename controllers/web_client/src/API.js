import axios from "axios";

class N64AllAPI {
    constructor(baseURL) {
        this.baseURL = baseURL;
        this.playerNumber = null;
        this.playerState = {
            "ANALOG": [0, 127],
            "A_BTN": 0,
            "B_BTN": 0,
            "Z_BTN": 0,
            "C_UP_ARROW": 0,
            "C_LEFT_ARROW": 0,
            "C_RIGHT_ARROW": 0,
            "C_DOWN_ARROW": 0,
            "L_TRIGGER": 0,
            "R_TRIGGER": 0,
            "START": 0,
        }
    }
    join() {
        // first, make post request to join.
        return new Promise((resolve, reject) => {
            axios.get(this.baseURL + "/join")
            .then((resp) => {
                if(resp && resp.data.success !== undefined) {
                    this.playerNumber = resp.data.success;
                    resolve(resp.data.success)
                }
                reject({err: "Server can't join."});
            })
            .catch((err) => {
                reject(err);
            });
        });
    }
    update(field, value) {
        // Update a single field
        this.playerState[field] = value;
    }
    sendChangesToServer() {
        // Get values
        const playerNum = this.playerNumber;
        let playerState = this.playerState;

        // Create an output object, and assign state
        let out = {};        
        out[playerNum] = playerState;

        // send to server. Result not needed.
        return axios.post(this.baseURL + "/update", out);
    }
    leave() {
        const leaveToken = {"player_id": this.playerNumber}
        return axios.post(this.baseURL + "/leave", leaveToken);
    }

}

export default N64AllAPI;