var express = require('express');
var path = require('path');
var bodyParser = require('body-parser');
var request = require('request'); 
var app = express();

// Constants. These should add to 1.0
const decayRate = 0.9;
const includeRate = 0.1;

app.use(bodyParser.json()); // support json encoded bodies
app.use(bodyParser.urlencoded({
    extended: true
}));

var currentDirectory = (process.env.PORT) ? process.cwd() : __dirname;
app.set("port", process.env.PORT || 3000);
state = {0: {}, 1: {}, 2: {}, 3: {}};

// initialise the array
for(let key in state) {
    state[key] = {
        "ANALOG": [0,0],
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
function getNewValue(oldValue, updatedValue) {
    return oldValue*decayRate + updatedValue*includeRate;
}

app.post("/api/add_options", function(req, res) {
    let details = req.body();
    let playerId = details['player'];

    // Analogue sticks
    state[playerId]["ANALOG"][0] = getNewValue(state[playerId]["ANALOG"][0], details["state"]["ANALOG"][0]);
    state[playerId]["ANALOG"][1] = getNewValue(state[playerId]["ANALOG"][1], details["state"]["ANALOG"][1]);

    // Now deal with more consistent things.
    Object.keys(state[playerId]).forEach((key) => {
        if(key !== "ANALOG") {
            state[player][key] = getNewValue(state[player][key], details["state"][key]);
        }
    });
    // Done!
    res.send({success: "Done!"})
});

function sendDataDownstream() {
    // Now send state.s
    for(let player in state) {
        request.post('http://localhost:8000/update', state[player]);
    }
}
// 40 frames per second.
setTimeout(sendDataDownstream, 25);

app.use('/', express.static(path.join(currentDirectory, 'client')));
app.get("*", function(req, res) {
    res.status(404).send("File not found");
});

app.listen(app.get("port"), function() {
    console.log("Server started on port " + app.get("port"));
});