import React, { Component } from 'react';
import './App.css';

class N64Button extends Component {
  render() {
    console.log(this.props)
    return (
      <div className="n64-button-default" onClick={this.props.onClick}>
        {this.props.text}
      </div>
    )
  }
}

export default N64Button;
