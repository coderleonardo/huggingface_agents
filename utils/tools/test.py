from template import tool

@tool
def calculator(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b

print(calculator.to_string())
# >>> Tool Name: calculator, Description: Multiply two integers., Arguments: a: int, b: int, Outputs: int