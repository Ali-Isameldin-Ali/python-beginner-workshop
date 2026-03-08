# Basic Calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nResults:")
print("1. Sum:", num1 + num2)
print("2. Difference:", num1 - num2)
print("3. Product:", num1 * num2)

# Avoid division by zero
if num2 != 0:
    print("4. Division result:", num1 / num2)
    print("5. Integer division result:", num1 // num2)
    print("6. Remainder:", num1 % num2)
else:
    print("4. Division result: Cannot divide by zero")
    print("5. Integer division result: Cannot divide by zero")
    print("6. Remainder: Cannot divide by zero")


    # Convert Minutes Program

total_minutes = int(input("Enter total minutes: "))

hours = total_minutes // 60
remaining_minutes = total_minutes % 60

print("\nConverted Time:")
print("Hours:", hours)
print("Remaining Minutes:", remaining_minutes)