# Type hint :- It is a way to specify the expected data type of a variable, function parameter, or return value in Python. It helps improve code readability and allows for better static analysis and error checking.

# Python Don't enforce the type of the variable
 
from typing import List, Dict, Tuple, Optional, Literal, TypedDict, Callable, TypeAlias, NoReturn

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

# 4. Optional - Value or None

def find_user(user_id: int) -> Optional[str]:
    """Find the user based on the user id. Return None if not found."""
    users = { 1: 'Aman', 2: 'Vansh' }
    return users.get(user_id)

# Python 3.10+ --> use | instead of Optional
def find_user_v2(user_id: int) -> str | None:
    users = { 1: 'Aman', 2: 'Vansh' }
    return users.get(user_id)


# 5: Union - Accept more than one type

# Python 3.10+ syntax
def format_id(value: int | str) -> str:
    if (isinstance(value, int)):
        return f"ID-{value:05d}"
    return f"ID-{value.upper()}"

print(format_id(42))    # ID-00042
print(format_id("abc")) # ID-ABC

# Literal - Only Allow specific values
def set_role(role: Literal["admin", "teacher", "student"]) -> str:
    return f"Role assigned: {role}"

set_role('admin')
# set_role('hacker') # mypy error - not an allowed value

# 7. TypeDict - Define the exact shape of a dictionary

class Student(TypedDict):
    name: str
    age: int
    marks: list[int]

def get_average(student: Student) -> float:
    return sum(student['marks']) / len(student['marks'])

ansh:Student = {'name': 'Ansh', 'age': 12, 'marks': [12, 13, 14, 15]}

print(get_average(ansh))


# 8. Callable
# - Callable[[input_types], return_type]

def apply_operation(
    a: int,
    b: int,
    operation: Callable[[int, int], int]
):
    return operation(a, b)

def add(x: int, y: int) -> int:
    return x + y

def multiply(x: int, y: int) -> int:
    return x * y

print(apply_operation(12, 15, add))
print(apply_operation(12, 15, multiply))


#9. Type Alias - Gives a name to complex types

UserId: TypeAlias = int
JsonResponse: TypeAlias = dict[str, list[dict[str, str | int]]]

def fetch_user(uid: UserId) -> JsonResponse:
    return {"data": [{'name': "aman", 'age': 12}]}

# 10. Type Narrowing - Type check using isinstance()
# This is Python's version of typescript's typeof guard

def process(value: str | int | list[str]) -> str:
    if isinstance(value, str):
        return value.upper()
    
    if isinstance(value, int):
        return str(value * 2)
    
    return ", ".join(value)

print(process("hello")) # HELLO
print(process(21)) # 42
print(process(["a", "b", "c"])) # a, b, c


# 11. None Return vs No Return 

# None return - function does its job but returns nothing
def save_log(msg: str) -> None:
    print(msg)
    
# NoReturn - function NEVER returns (crash / infinite loop)
def raise_error(msg: str) -> NoReturn:
    raise RuntimeError(msg)