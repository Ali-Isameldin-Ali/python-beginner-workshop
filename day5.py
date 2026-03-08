# 1) Counting from 1 to 20

print("=== Counting 1 to 20 ===")

for i in range(1, 21):
    print(i)

# 2) Multiplication Table

print("\n=== Multiplication Table ===")

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# 3) Repeat Until Correct

print("\n=== Password Check ===")

password = input("Enter password: ")

while password != "1234":
    password = input("Wrong password. Try again: ")

print("Access Granted")


# Challenge: Limited Attempts

print("\n=== Secure Login ===")

correct_password = "1234"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter password: ")

    if password == correct_password:
        print("Access Granted")
        break
    else:
        attempts += 1
        print("Wrong password")

if attempts == max_attempts:
    print("Locked")