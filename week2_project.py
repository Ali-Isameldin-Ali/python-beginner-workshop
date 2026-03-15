# ==========================================
# Week 2 Mini OOP Project: Simple Budget Tracker
# ==========================================

# 1. Create the Class
class BudgetTracker:
    def __init__(self):
        # Attribute: balance
        self.balance = 0.0

    # Method 1: add_income
    def add_income(self, amount):
        # Condition inside method
        if amount > 0:
            self.balance += amount
            print(f"✅ Income added successfully: +${amount:.2f}")
        else:
            print("❌ Invalid amount. Income must be greater than 0.")

    # Method 2: add_expense
    def add_expense(self, amount):
        # Conditions inside method
        if amount <= 0:
            print("❌ Invalid amount. Expense must be greater than 0.")
        elif amount > self.balance:
            print(f"⚠️ Insufficient funds! You only have ${self.balance:.2f} available.")
        else:
            self.balance -= amount
            print(f"✅ Expense recorded successfully: -${amount:.2f}")

    # Method 3: show_balance
    def show_balance(self):
        print(f"\n💰 Current Available Balance: ${self.balance:.2f}")


# 2. Main function to handle the interactive loop
def main():
    print("=== Welcome to the Simple Budget Tracker ===")
    
    # Create the object
    my_budget = BudgetTracker()

    # Loop for interaction
    while True:
        print("\n" + "-"*20)
        print("        MENU")
        print("-"*20)
        print("1. Add income")
        print("2. Add expense")
        print("3. Show balance")
        print("4. Exit")
        
        choice = input("Please select an option (1-4): ")

        if choice == '1':
            amount = float(input("Enter income amount: $"))
            my_budget.add_income(amount)
            
        elif choice == '2':
            amount = float(input("Enter expense amount: $"))
            my_budget.add_expense(amount)
            
        elif choice == '3':
            my_budget.show_balance()
            
        elif choice == '4':
            print("\nExiting the Budget Tracker. Have a great day! 👋")
            break  # Exit the loop
            
        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")

# Clean structure: Run the main function
if __name__ == "__main__":
    main()