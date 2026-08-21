function Display({ expression, result, error }) {
  return (
    <div className="display">
      <div className="expression">{expression || "0"}</div>
      {error && <div className="error">{error}</div>}
      {result !== null && !error && (
        <div className="result">= {result}</div>
      )}
    </div>
  );
}

export default Display;