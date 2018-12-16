import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import N64AllAPI from './API';
import * as serviceWorker from './serviceWorker';

const apiInstance = new N64AllAPI();


ReactDOM.render(<App api={apiInstance}/>, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
serviceWorker.unregister();
