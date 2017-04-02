import React from 'react';
import ReactDOM from 'react-dom';

import Config from './Config'
import App from './App'

const appContainer = document.getElementById(Config.App.ID)

ReactDOM.render(<App/>, appContainer)
