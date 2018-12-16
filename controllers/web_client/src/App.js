import React, { Component } from 'react';
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);

    // now set the state
    this.state = {
      playerNumber: -1
    }
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
            <div className="n64-button-default">A</div>
            <div className="n64-button-default">B</div>
            <div className="n64-button-default"></div>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
