# ==========================================
# Task 1: Calculator Refactor
# ==========================================

# Define the functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# Ask the user for two numbers
print("--- Basic Calculator ---")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Call the functions and print the results
print(f"Addition: {add(num1, num2)}")
print(f"Subtraction: {subtract(num1, num2)}")
print(f"Multiplication: {multiply(num1, num2)}")
print(f"Division: {divide(num1, num2)}")

# ==========================================
# Task 2: Grade Classification Using Function
# ==========================================

# Define the function
def determine_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Ask the user for a score
print("\n--- Grade Classifier ---")
user_score = float(input("Enter a score (0-100): "))

# Call the function and save the result in a variable
final_grade = determine_grade(user_score)

# Print the result
print(f"Your grade is: {final_grade}")