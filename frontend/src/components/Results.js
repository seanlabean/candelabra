import React from 'react';
import Plot from './Plot';

function Results({ data }) {
    const yKs = ["Close"];
    return (
        <div className="results">
            <h2>Stock Data</h2>
            <Plot data={data} xKey="Date" yKeys={yKs} title="Closing Prices" />
        </div>
    );
}

export default Results;