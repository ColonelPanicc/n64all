import axios from "axios";
class N64AllAPI {
    constructor() {
        this.playerNumber = null;
    }
    join() {
        // first, make post request to join.
        return new Promise((resolve, reject) => {
            axios.get(this.baseURL + "/join")
            .then((resp) => {
                if(resp && resp.success !== undefined) {
                    this.playerNumber = resp.success;
                    resolve(resp.success)
                }
                reject({err: "Server can't join."});
            })
            .catch((err) => {
                reject(err);
            });
        });
    }

    leave() {
        return axios.post(this.baseURL + "/leave", {"player_id": this.playerNumber});
    }

}

export default N64AllAPI;