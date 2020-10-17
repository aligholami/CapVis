import React from 'react';
import logo from './logo.svg';
import './App.css';
const glob = require('glob');
const captioning_experiments = '/Users/hexph/Desktop/CapVis/data/captioning_experiments/';

function App() {

  return (
    <div className="App">
      {
        glob(captioning_experiments, {}, (err, files) => {
          console.log(files)
        })
      }
    </div>
  );
}

export default App;
