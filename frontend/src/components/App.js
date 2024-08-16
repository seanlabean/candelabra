import React, { useState } from 'react';
import StockInput from './StockInput';
import Results from './Results';
import logo from '../assets/logo.svg';
import '../App.css';

function App() {
  const [results, setResults] = useState(null);

  const fetchData = async (symbol) => {
    const response = await fetch('/api/stock', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ symbol })
    });
    const data = await response.json();
    setResults(data);
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
      <div className="App">
        <h1>Stock Prediction App</h1>
        <StockInput onSubmit={fetchData} />
        {results && <Results data={results} />}
      </div>
    </div>
  );
}

export default App;
