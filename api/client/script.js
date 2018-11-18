var state = {
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
let right = 0;
const xTolerance = 15
var myId = -1;
fetch('http://10.245.8.174:8000/join', 
    {
        headers: {
        "Content-Type": "application/json",
    }
})
.then(res => res.json())
.then(r_json => {
    console.log(r_json)

    if(r_json.success !== undefined) {
        myId = r_json.success; 
        alert("Given id " + myId)
        window.addEventListener("devicemotion", handleMotion, true);
    }

});


function update() {
    if (myId > -1) {
        console.table(state)
        data = {}
        data[myId] = state
        console.log(data)
        fetch("http://10.245.8.174:8000/update", {
            method: 'POST', // or 'PUT'
            body: JSON.stringify(data), // data can be `string` or {object}!
        });
    }
}

window.addEventListener("beforeunload", function() {
    if (myId > -1) {
        fetch("http://10.245.8.174:8000/leave", {
            method: 'POST', // or 'PUT',
            body: JSON.stringify({"player_id": my_id}),
            headers:{
            'Content-Type': 'application/json'
            }
        });
    }
});

function handleMotion(event) {

    rot = event.rotationRate;
    let rt = rot.alpha;
    if(-xTolerance <= rt && rt <= xTolerance) {
        rt = 0;
    }
    right += rt* 0.05 
    right = Math.min(127, Math.max(-127, right));
    state["ANALOG"][0] = right
    update()
}

function inverseButton(lookup) {
    if(state[lookup] === 0) {
        state[lookup] = 1;
    }
    else {
        state[lookup] = 0;
    }
}

function pressA() {
    inverseButton("A_BTN")
    update()
}

function pressB() {
    inverseButton("B_BTN")
    update()
}

function pressZ() {
    inverseButton("Z_BTN")
    update()
}

function pressStart(){
    inverseButton("START")
    update()
}
