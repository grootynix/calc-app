def calculate(expression: str) -> float:
    allowed = set("0123456789+-*/(). ")

    if not expression:
        raise ValueError("Expression cannot be empty")

    if not all(char in allowed for char in expression):
        raise ValueError(f"Invalid characters in expression")

    try:
        result = eval(expression)
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero")
    except Exception:
        raise ValueError("Invalid expression")

    return float(result)