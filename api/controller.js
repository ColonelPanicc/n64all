class Controller { 

    constructor() {
        
        // enum for allowable button strings
        this.buttons = {
            "LEFT_ANALOG": Analog(),
            "RIGHT_ANALOG": Analog(),
            "A_BUTTON": Input(),
            "B_BUTTON": Input(),
            "UP_ARROW": Input(),
            "RIGHT_ARROW": Input(),
            "LEFT_ARROW": Input(),
            "RIGHT_ARROW": Input(),
            "RIGHT_TRIGGER": Input(),
            "LEFT_TRIGGER": Input(),
            "START": Input()
        };
    }

    getState() {
        return Object.assign({}, this.buttons);
    }

    getInput(inputID) {
        if (inputID in self.buttons) {
            return this.buttons.inputID;
        }
    }
}

class Input {

    constructor() {
        this.holdTime = 0;
        this.active = false;
    }

    toggle() {
        this.active = !this.active;
    }

    getHeldTime(){
        return this.heldTime;
    }

    set(active) {
        this.active = active;
    }

    setHoldTime(newHoldTime) {
        this.holdTime = newHoldTime;
    }

}

class Analog extends Input {

    constructor(){
        this.angle = 0;
        this.oomph = 0;
    }

    getAngle() {
        return this.angle;
    }

    getOomph() {
        return this.oomph;
    }
    
    setAngle(angle) {
        this.angle = angle;
    }

    setOopmh (oomph) {
        this.oomph = oomph;
    }
}
