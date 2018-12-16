import axios from "axios";
class N64AllAPI {
    constructor(baseURL) {
        this.baseURL = baseURL;
        this.playerNumber = null;
    }
    join() {
        // first, make post request to join.
        return new Promise((resolve, reject) => {
            axios.get(this.baseURL + "/join")
            .then((resp) => {
                console.log(resp.data)
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

    leave() {
        return axios.post(this.baseURL + "/leave", {"player_id": this.playerNumber});
    }

}

export default N64AllAPI;