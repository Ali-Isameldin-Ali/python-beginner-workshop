# 1) Basic List Operations

numbers = [10, 20, 30, 40, 50]

print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Length of list:", len(numbers))

# 2) Store Names in a List

names = []

for i in range(3):
    name = input("Enter a name: ")
    names.append(name)

print("\nNames entered:")

for name in names:
    print(name)

# Challenge

numbers = []

for i in range(5):
    num = float(input("Enter a number: "))
    numbers.append(num)

maximum = max(numbers)
minimum = min(numbers)
average = sum(numbers) / len(numbers)

print("\nResults:")
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Average:", average)