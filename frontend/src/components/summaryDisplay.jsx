import React from 'react';
export default function SummaryDisplay({ summary }) {
  return (
    <div style={{ marginTop: 20 }}>
      <h3>Summary</h3>
      <p>{summary}</p>
    </div>
  );
}
