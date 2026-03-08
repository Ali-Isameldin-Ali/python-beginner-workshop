# Grade Classification

score = float(input("Enter your score (0-100): "))

if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score <= 89:
    print("Grade: B")
elif 70 <= score <= 79:
    print("Grade: C")
elif 60 <= score <= 69:
    print("Grade: D")
elif 0 <= score < 60:
    print("Grade: F")
else:
    print("Invalid score")


# Even or Odd Checker

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")



# Simple ATM Withdrawal Validator

balance = 1000  # Fixed balance

print("Current Balance:", balance)

amount = float(input("Enter amount to withdraw: "))

if amount <= 0:
    print("Invalid amount")
elif amount > balance:
    print("Insufficient funds")
else:
    balance -= amount
    print("Withdrawal successful")
    print("Remaining balance:", balance)