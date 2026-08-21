function Button({ label, onClick, variant }) {
  return (
    <button
      className={`btn btn-${variant || "default"}`}
      onClick={() => onClick(label)}
    >
      {label}
    </button>
  );
}

export default Button;