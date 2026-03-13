# ==========================================
# Main Task: Interactive Bank System
# ==========================================

# 1. Define the Class (from Day 4)
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"\n✅ Successfully deposited ${amount:.2f}")
        else:
            print("\n❌ Invalid amount. Deposit must be greater than 0.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"\n❌ Insufficient funds! Your balance is only ${self.balance:.2f}")
        elif amount <= 0:
            print("\n❌ Invalid amount. Withdrawal must be greater than 0.")
        else:
            self.balance -= amount
            print(f"\n✅ Successfully withdrew ${amount:.2f}")

    def show_balance(self):
        print(f"\n💰 Current Balance for {self.owner}: ${self.balance:.2f}")


# 2. Build the Interactive System
def main():
    print("Welcome to the Python Bank!")
    # Create one BankAccount object
    name = input("Please enter your name to open an account: ")
    my_account = BankAccount(name, 0.0) # Starting with $0 balance

    # Use a while loop to display a menu
    while True:
        print("\n" + "="*25)
        print("       BANK MENU")
        print("="*25)
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Show Balance")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        # 3. Based on user choice, call the correct method
        if choice == '1':
            amount = float(input("Enter amount to deposit: $"))
            my_account.deposit(amount)
            
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: $"))
            my_account.withdraw(amount)
            
        elif choice == '3':
            my_account.show_balance()
            
        elif choice == '4':
            print(f"\nThank you for banking with us, {my_account.owner}. Goodbye! 👋\n")
            break # This stops the while loop!
            
        else:
            print("\n❌ Invalid choice. Please enter 1, 2, 3, or 4.")

# Run the program
if __name__ == "__main__":
    main()