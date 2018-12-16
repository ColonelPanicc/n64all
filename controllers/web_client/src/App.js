import React, { Component } from 'react';
import './App.css';
import N64Button from './N64Button';

class App extends Component {
  constructor(props) {
    super(props);

    // now set the state
    this.state = {
      playerNumber: -1
    }

    this.onButtonPressed = this.onButtonPressed.bind(this);
  }

  componentDidMount() {
    // Join using the passed in API, and update UI to show player number.
    this.props.api.join().then((id) => {
      this.setState({playerNumber: id});
    })
  }
  componentWillUnmount() {
    // Leave.
    this.props.api.leave();
    
    // Reset player number.
    this.setState({playerNumber: -1});
  }
  onButtonPressed(btn) {
    // TODO: trigger internal state change.
    this.props.api.update()
  }
  render() {
    return (
      <div className="App">
        <div className="left-half">
          <div className="half-container">
            Player {this.state.playerNumber}
          </div>
        </div>
        <div className="right-half">
          <div className="half-container">
            <N64Button text="A" onClick={this.onButtonPressed}></N64Button>
            <N64Button text="B"></N64Button>
            <N64Button text="C"></N64Button>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
