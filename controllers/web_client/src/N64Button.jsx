import React, { Component } from 'react';
import './App.css';

class N64Button extends Component {
  render() {
    return (
      <div className="n64-button-default" onClick={() => this.props.onClick(this.props.stateLabel)}>
        {this.props.text}
      </div>
    )
  }
}

export default N64Button;
