import { useState } from "react";
import Display from "./components/Display";
import Button from "./components/Button";
import { calculate } from "./services/api";
import "./App.css";

const BUTTONS = [
  ["7", "8", "9", "/"],
  ["4", "5", "6", "*"],
  ["1", "2", "3", "-"],
  ["0", "(", ")", "+"],
  ["C", "⌫", ".", "="],
];

function App() {
  const [expression, setExpression] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  function handleButton(label) {
    setError(null);
    setResult(null);

    if (label === "C") {
      setExpression("");
      return;
    }

    if (label === "⌫") {
      setExpression((prev) => prev.slice(0, -1));
      return;
    }

    if (label === "=") {
      handleCalculate();
      return;
    }

    setExpression((prev) => prev + label);
  }

  async function handleCalculate() {
    try {
      const res = await calculate(expression);
      setResult(res);
    } catch (err) {
      setError(err.message);
    }
  }

  return (
    <div className="calculator">
      <Display expression={expression} result={result} error={error} />
      <div className="buttons">
        {BUTTONS.map((row, i) => (
          <div key={i} className="row">
            {row.map((label) => (
              <Button
                key={label}
                label={label}
                onClick={handleButton}
                variant={label === "=" ? "equals" : label === "C" ? "clear" : "default"}
              />
            ))}
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;