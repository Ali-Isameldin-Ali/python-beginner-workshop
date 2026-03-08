# 1) Student Dictionary

student = {
    "Name": "Ahmed",
    "Age": 20,
    "Major": "Computer Engineering"
}

print("Student Profile")
print("Name:", student["Name"])
print("Age:", student["Age"])
print("Major:", student["Major"])

# 2) Subjects and Grades

grades = {
    "Math": "A",
    "Physics": "B",
    "Programming": "A"
}

print("\nSubjects and Grades:")

for subject, grade in grades.items():
    print(subject, ":", grade)


# Grade Lookup System

grades = {
    "Math": "A",
    "Physics": "B",
    "Programming": "A"
}

subject = input("Enter subject name: ")

if subject in grades:
    print("Grade:", grades[subject])
else:
    print("Subject not found")




# Mini Contact Book

contacts = {}

name1 = input("Enter name: ")
phone1 = input("Enter phone: ")

contacts[name1] = phone1

name2 = input("Enter another name: ")
phone2 = input("Enter another phone: ")

contacts[name2] = phone2

print("\nContact List:")

for name, phone in contacts.items():
    print(name, ":", phone)