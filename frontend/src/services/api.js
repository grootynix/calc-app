const API_URL = process.env.REACT_APP_API_URL || "http://localhost:8000";

export async function calculate(expression) {
  const response = await fetch(`${API_URL}/calculate`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ expression }),
  });

  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.detail || "Calculation failed");
  }

  const data = await response.json();
  return data.result;
}