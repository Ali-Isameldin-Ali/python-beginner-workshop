import random

# 1. Function to generate the random number
def generate_number():
    return random.randint(1, 100)

# 2. Function to get the user's guess (with Bonus: Input Validation)
def get_guess():
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            return guess
        except ValueError:
            print("Invalid input! Please enter a whole number.")

# 3. Function to check the guess
def check_guess(guess, secret_number):
    if guess < secret_number:
        print("Too low!")
        return False
    elif guess > secret_number:
        print("Too high!")
        return False
    else:
        print("Correct! You guessed the secret number!")
        return True

# 4. Main function to control the program flow
def main():
    print("\n--- Welcome to the Guess the Number Game ---")
    secret_number = generate_number()
    attempts = 0
    is_correct = False

    # Loop until the user guesses correctly
    while not is_correct:
        guess = get_guess()
        attempts += 1 # Count the attempts
        is_correct = check_guess(guess, secret_number)

    print(f"Awesome! It took you {attempts} attempts to win.")

    # Bonus: Play again option
    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again == 'y':
        main()
    else:
        print("Thanks for playing! Goodbye.")

# 5. Call main() at the bottom of the program
if __name__ == "__main__":
    main()