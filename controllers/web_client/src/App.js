import React, { Component } from 'react';
import './App.css';
import N64Button from './N64Button';

class App extends Component {
  constructor(props) {
    super(props);

    // now set the state
    this.state = {
      playerNumber: -1,
      timer: null
    }

    this.onButtonPressed = this.onButtonPressed.bind(this);
    this.onPageClose = this.onPageClose.bind(this);
  }

  onPageClose() {
    this.props.api.leave();
    
    // Reset player number.
    this.setState({playerNumber: -1});
  }
  componentDidMount() {
    // Join using the passed in API, and update UI to show player number.
    this.props.api.join().then((id) => {
      this.setState({playerNumber: id});

      // set up the timer to send values to server. In this case, every 30 frames (ish).
      let t = window.setInterval(() => this.props.api.sendChangesToServer(), 30);
      this.setState({timer: t});
    });

    window.addEventListener('beforeunload', this.onPageClose);
    
   
  }

  componentWillUnmount() {
    window.removeEventListener('beforeunload', this.onPageClose);

    if(this.state.timer !== null) {
      window.clearInterval(this.state.timer);
    }
  }

  onButtonPressed(btn) {
    // TODO: trigger internal state change.
    const api = this.props.api;
    // 1 -> 0; 0 -> 1. Just toggle
    // TODO: don't toggle, but set value ONCE, and reset after update.
    const newVal = api.playerState[btn] === 0 ? 1 : 0;
    console.log(btn, newVal);
    api.update(btn, newVal)
  }

  render() {
    return (
      <div className="App">
        <div className="left-half">
          <div className="half-container">
            Player {this.state.playerNumber + 1}
          </div>
        </div>
        <div className="right-half">
          <div className="half-container">
            <N64Button text="A" stateLabel="A_BTN" onClick={this.onButtonPressed}></N64Button>
            <N64Button text="B" stateLabel="B_BTN" onClick={this.onButtonPressed}></N64Button>
            <N64Button text="Z" stateLabel="Z_BTN" onClick={this.onButtonPressed}></N64Button>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
