import random

# ==========================================
# Week 3 Final Project: Quiz Engine
# ==========================================

class QuizEngine:
    def __init__(self):
        # Extra Feature: Question bank list using dictionaries
        self.question_bank = [
            {"question": "What is the capital of France?", "options": ["A) London", "B) Paris", "C) Rome"], "answer": "B"},
            {"question": "Which data type is used to store True or False?", "options": ["A) Integer", "B) String", "C) Boolean"], "answer": "C"},
            {"question": "What keyword is used to define a function in Python?", "options": ["A) func", "B) def", "C) class"], "answer": "B"},
            {"question": "Which of these is a mutable data structure?", "options": ["A) Tuple", "B) List", "C) Integer"], "answer": "B"},
            {"question": "What keyword refers to the object itself in a class?", "options": ["A) self", "B) this", "C) me"], "answer": "A"}
        ]
        self.score = 0

    def ask_questions(self):
        self.score = 0 # Reset score for replay
        
        # Extra Feature: Random order
        random.shuffle(self.question_bank) 
        
        print("\n" + "="*30)
        print("  🧠 WELCOME TO THE QUIZ 🧠  ")
        print("="*30)

        # Loop through questions
        for idx, q in enumerate(self.question_bank):
            print(f"\nQuestion {idx + 1}: {q['question']}")
            for option in q['options']:
                print(option)
            
            # Get user answer and validate
            user_answer = input("Your answer (A/B/C): ").upper()
            
            # Condition to check answer
            if user_answer == q['answer']:
                print("✅ Correct!")
                self.score += 1
            else:
                print(f"❌ Wrong! The correct answer was {q['answer']}.")

    def show_result(self):
        print("\n" + "="*30)
        print("         QUIZ FINISHED!       ")
        print("="*30)
        print(f"Your final score is: {self.score} / {len(self.question_bank)}")
        
        if self.score == len(self.question_bank):
            print("🏆 Perfect Score! You are a Python Master!")
        elif self.score >= len(self.question_bank) // 2:
            print("👍 Good job! You passed.")
        else:
            print("📚 Keep studying! You'll get it next time.")

    def replay(self):
        # Extra Feature: Replay option
        while True:
            choice = input("\nWould you like to play again? (Y/N): ").upper()
            if choice == 'Y':
                self.ask_questions()
                self.show_result()
            elif choice == 'N':
                print("Thanks for playing! Goodbye. 👋")
                break
            else:
                print("Invalid input. Please type Y or N.")

def main():
    # Create the Quiz Object
    my_quiz = QuizEngine()
    
    # Run the methods
    my_quiz.ask_questions()
    my_quiz.show_result()
    my_quiz.replay()

if __name__ == "__main__":
    main()