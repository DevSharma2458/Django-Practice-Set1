# #new.py is related to this inheritance example.
# Create a new file named new.py and add the following code to it:
# class Studnet():
#     name = "John"
#     age = 20
#     gender = "Male"
# from new import Student 

# class Person(Student):
#     pass

# p1 = Person()
# print(p1.name) 

# ----------------------------------------------------------------------------

# class Parent:
#     def __init__(self):
#         print("I am the parent class")

#     def greet(self):
#         print("Hello from Parent")

# class Child(Parent): 
#     def __init__(self): 
#         super().__init__()  # Calls parent constructor
#         print("I am the child class")

#     def greet(self):  # Method overriding
#         print("Hello from Child") 

# c = Child() # Creates an instance of Child
# c.greet()  # Calls the overridden method

# --------------------------------------------------------------



# "Pehle neeche se input lega → Student class me jaayega → waha se parent class ko call karega → waha name and age set honge → fir grade set hoga → fir show_info() se sab print hoga."
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print("Name:", self.name, ", Age:", self.age)

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def show_info(self):
        super().show_info()
        print("Grade:", self.grade)

#Taking input from the user

name = input("Enter your name: ")
age = int(input("Enter your age: "))
grade = input("Enter your grade: ")

student = Student(name, age, grade)
student.show_info() # This will call the overridden method in Student class
# This will print the name, age, and grade of the student














































