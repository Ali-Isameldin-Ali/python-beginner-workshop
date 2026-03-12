# ==========================================
# Task 1: Improve the Person Class
# ==========================================

class Person:
    # Initialize the attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    # Add the greet method
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

print("--- Person Greeting ---")
# Create 2 objects
person1 = Person("Ali", 21)
person2 = Person("Sami", 24)

# Call the greet() method on both objects
person1.greet()
person2.greet()

print("\n") # Just adding an empty line for clean output

# ==========================================
# Task 2: Bank Account System
# ==========================================

class BankAccount:
    # Initialize attributes (owner and starting balance)
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    # Method to deposit money
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance is ${self.balance}.")

    # Method to withdraw money with validation
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrawal successful! Withdrew ${amount}.")

    # Method to show the current balance
    def show_balance(self):
        print(f"Account Owner: {self.owner} | Current Balance: ${self.balance}")

print("--- Bank Account System ---")
# Let's create an account for you and test it out!
my_account = BankAccount("Ali", 1000) # Starting with $1000

# Testing the methods
my_account.show_balance()

# Try depositing money
my_account.deposit(500)

# Try withdrawing too much money (should print "Insufficient funds")
my_account.withdraw(2000)

# Try a valid withdrawal
my_account.withdraw(300)

# Show final balance
my_account.show_balance()