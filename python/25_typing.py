# Type hint :- It is a way to specify the expected data type of a variable, function parameter, or return value in Python. It helps improve code readability and allows for better static analysis and error checking.

# Python Don't enforce the type of the variable
 
from typing import List, Dict, Tuple

def add(a: int, b: int) -> int:
    return a + b

result = add(12, 23)
print(result)

# Why we need this
# - Team Memeber
# - Editor
# - You 

# - mypy --> checking type before running the code ( pip install mypy )
# - pydantic ---> checking type at runtime

# uv run file_name

# uv run mypy file_name


# Typing Types

# 1. Basic Variable Type Hint

name: str = "Ansh"
age: int = 12
price: float = 99.50
is_active: bool = True

# You can declare without value

username: str # no value yet we will assign later

# 2. Function Type Hint

def calculate_bill(item: str, price: float, quantity: int) -> float:
    """Calcuate total bill for an item.""" # Doc String
    return price * quantity

result = calculate_bill("Car", 20000.00, 10)
print(result)

# 3. Collection Type Hint

# List 
scores = List[int] = [98, 97, 34]

# Dictionary 
stock = Dict[str, int] = {"Pen": 20, "Notebook": 30}

# Tuple
coordinates: Tuple[float, float] = (28.61, 77.23)

# Set 
tags: set[str] = { "Python", "Backend", "api" }

# Nested 
students: list[dict[str, int]] = [
    { "math": 76, "science": 26 },
    { "math": 78, "science": 92 }
]

