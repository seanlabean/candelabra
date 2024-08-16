import React from 'react';

function Results({ data }) {
    return (
        <div className="results">
            <h2>Stock Data</h2>
            <pre>{JSON.stringify(data, null, 2)}</pre>
        </div>
    );
}

export default Results;