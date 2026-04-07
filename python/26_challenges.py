"""
PYTHON CHALLENGES - BEGINNER + LEVEL
====================================
Concepts: Variables, Data Types, Operators, Conditionals, Loops, Functions, 
Lists, Dicts, String Operations, File Handling, Basic OOP

================================================================================
CHALLENGE 1: Simple Shopping Bill Calculator
================================================================================
Problem:
A customer buys multiple items. Calculate total bill with 10% discount if 
total exceeds Rs.1000.

What to do:
- Take prices of items as input
- Calculate total
- Apply discount if applicable
- Show final amount

Example: prices = [450, 350, 300] -> Total = 1100, Discount = 110, Final = 990

"""
def calculate_bill(prices):
    total = sum(prices)
    discount = total * 0.10 if total > 1000 else 0
    final_amount = total - discount
    return total, discount, final_amount

"""

================================================================================
CHALLENGE 2: Grade Calculator
================================================================================
Problem:
Read marks (out of 100) from user for 5 subjects, calculate average, and 
assign grades (A: 90+, B: 80+, C: 70+, D: 60+, F: <60).

What to do:
- Take 5 marks as input
- Calculate average
- Assign letter grade
- Show result with grade

Example: [95, 87, 76, 88, 92] -> Average = 87.6, Grade = B
"""
def calculate_grade(marks):
    avg = sum(marks) / len(marks)
    if avg >= 90:
        grade = 'A'
    elif avg >= 80:
        grade = 'B'
    elif avg >= 70:
        grade = 'C'
    elif avg >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return avg, grade

"""

================================================================================
CHALLENGE 3: Password Validator
================================================================================
Problem:
Create a function to check if a password is strong. Strong password must have:
- At least 8 characters
- At least 1 uppercase letter
- At least 1 number

What to do:
- Check length
- Check uppercase presence
- Check number presence
- Return True/False with reason

Example: "Pass123" -> Strong, "pass123" -> Weak (no uppercase)
"""

def validate_password(password):
    if len(password) < 8:
        return False
    
    if not any(char.isupper() for char in password):
        return False
    
    if not any(char.isdigit() for char in password):
        return False
    
    return True
        

"""

================================================================================
CHALLENGE 4: Simple Inventory System
================================================================================
Problem:
A store has products with prices and quantities. Users can add items to cart,
view cart, and see total.

What to do:
- Store product list (name, price, quantity available)
- Add items to cart
- View cart items
- Calculate total price

Example: Products = {"Apple": 30, "Banana": 20}, Cart = {"Apple": 2, "Banana": 3}
Total = 30*2 + 20*3 = 120

"""

def calculate_cart_total(products, cart):
    total = 0
    for item, quantity in cart.items():
        if item in products:
            total += products[item] * quantity
    return total
            


"""

================================================================================
CHALLENGE 5: File Word Counter
================================================================================
Problem:
Read a text file and find how many times each word appears. Show top 3 words.

What to do:
- Read file content
- Count each word
- Sort by frequency
- Show top 3 words with counts

Example: File has "hello world hello" -> hello: 2, world: 1

================================================================================
CHALLENGE 6: Temperature Converter
================================================================================
Problem:
Convert temperatures between Celsius and Fahrenheit. Take list of Celsius 
values and convert them. Also identify extreme values (< 0 or > 40).

What to do:
- Take Celsius values
- Convert to Fahrenheit (F = C * 9/5 + 32)
- Find minimum and maximum
- Mark extreme temperatures

Example: [0, 25, 45, -5] -> [32, 77, 113, 23], Extreme: 45°C, -5°C

================================================================================
CHALLENGE 7: Movie Database
================================================================================
Problem:
Create a dictionary of movies (title, year, rating). User can search by title,
filter by rating (>= 8), or list all movies.

What to do:
- Store movie data (use dict or list of dicts)
- Search by movie name
- Filter by rating threshold
- Display formatted results

Example: Movies = {"Inception": {"year": 2010, "rating": 8.8}}
Search "Inception" -> Show movie details

================================================================================
CHALLENGE 8: Simple Todo List
================================================================================
Problem:
Build a todo app where users can add tasks, mark as done, and delete tasks.
Save tasks to a file.

What to do:
- Add task with description
- Mark task complete (store with status)
- Delete task
- Save tasks to file before exit
- Load tasks from file on start

Example: [{"task": "Buy milk", "done": False}, {"task": "Code", "done": True}]

================================================================================
CHALLENGE 9: String Formatter
================================================================================
Problem:
Take a sentence and perform transformations: uppercase, lowercase, 
reverse word order, remove extra spaces.

What to do:
- Accept input string
- Show uppercase version
- Show lowercase version
- Show reversed word order
- Show without extra spaces

Example: "  Hello   World  " -> 
UPPERCASE: "  HELLO   WORLD  "
NO SPACES: "Hello World"
REVERSE: "World Hello"

================================================================================
CHALLENGE 10: Student Report Generator
================================================================================
Problem:
Read student data from a file (name, marks in 3 subjects), calculate average,
and save a report with pass/fail status.

What to do:
- Read student data from file
- Calculate average for each student
- Determine pass (avg >= 50) or fail
- Save report to new file with formatting
- Show summary (total students, passed, failed)

File Format:
name,subject1,subject2,subject3
Raaj,45,67,89
Priya,78,82,91

Output: Student names with average, status, and summary

================================================================================

TIPS:
1. Start simple - just solve the main problem
2. Use lists and dicts when needed
3. Add a few print statements for testing
4. Focus on solving in 5 minutes
"""
