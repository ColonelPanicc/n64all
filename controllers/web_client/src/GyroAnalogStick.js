import React, { Component } from 'react';
import './App.css';

class GyroAnalogStick extends Component {
    constructor(props) {
        super(props);
        this.state = {
            fb: 0,
            lr: 0
        }
        this.handleDeviceMotion = this.handleDeviceMotion.bind(this);
    }

    componentDidMount() {
        window.addEventListener("devicemotion", this.handleDeviceMotion);
    }

    handleDeviceMotion(motion) {
        
        let acceleration = motion.accelerationIncludingGravity;
       
        // Take values of each variable, round to nearest 10, and range between 127 and -127.

        // forwards/backwards +ve -> forwards -ve -> backwards
        let fb = Math.ceil((Math.floor((12.7)*(acceleration.z)) + 1)/10) * 10;
        
        // left/right -ve -> left +ve -> right
        let lr = Math.ceil((Math.floor(12.7 * acceleration.y) + 1) / 10) * 10;
        
        this.setState({
            fb: fb,
            lr: lr
        })

        this.props.onUpdate([fb, lr]);
    }
    render() {
        return (
        <div>
            {/* ({this.state.fb}, {this.state.lr}) */}
        </div>
        )
    }
}

export default GyroAnalogStick;
