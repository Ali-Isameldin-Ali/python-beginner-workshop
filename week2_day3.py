# ==========================================
# Task 1: Create a Person Class
# ==========================================
class Person:
    # Use __init__ to initialize attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create 2 objects
person1 = Person("Ali", 21)
person2 = Person("Sami", 24)

# Print their details
print("--- Person Details ---")
print(f"Person 1: Name = {person1.name}, Age = {person1.age}")
print(f"Person 2: Name = {person2.name}, Age = {person2.age}")


# ==========================================
# Task 2: Student Profile System
# ==========================================
class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
    
    # A helpful method to print formatted info
    def print_info(self):
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Major: {self.major}")
        print("-" * 20)

# Create at least 2 students
student1 = Student("Ali", 21, "Software Engineering")
student2 = Student("Ahmed", 20, "Computer Science")

# Print their information in formatted style
print("\n--- Student Profiles ---")
student1.print_info()
student2.print_info()