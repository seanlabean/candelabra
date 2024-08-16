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
        <h1>Stock Prediction App</h1>
        <StockInput onSubmit={fetchData} />
        {results && <Results data={results} />}
    </div>
  );
}

export default App;
