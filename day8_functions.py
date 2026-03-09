# Calculator using functions

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


# Ask user for numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Call functions
print(f"Sum: {add(num1, num2)}")
print(f"Difference: {subtract(num1, num2)}")
print(f"Product: {multiply(num1, num2)}")
print(f"Division: {divide(num1, num2)}")


# Grade classification using function

def get_grade(score):

    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    else:
        return "F"


score = int(input("Enter your score: "))

grade = get_grade(score)

print(f"Your grade is: {grade}")