# classes:-classes is an blueprint and template for creating an object.
# object:-objects is an instance of a class.
# class Person:
#     name= "chetana"
#     age=20

# a=Person()
# print(a.name)
# print(a.age)


# self parameter:- reference to the current object of  class.used to access variable that belongs to the class.

# class Student:
#     def __init__(self, name, grade):
#         self.name = name       # 'self.name' is an instance variable
#         self.grade = grade     # 'self.grade' is an instance variable

#     def display_info(self):
#         print(f"Name: {self.name}, Grade: {self.grade}")

# # Creating objects
# student1 = Student("Alice", "A")
# student2 = Student("Bob", "B")

# # Calling method
# student1.display_info()  # Output: Name: Alice, Grade: A
# student2.display_info()  # Output: Name: Bob, Grade: B











# constructors:-constructor is a special method used to initialize an object of a class.

# parameterized constructor:-
# class Student:
#     def __init__ (self,name,age):
#         self.name= name
#         self.age = age

# a=Student("chetana",28)
# print(a.name,a.age)
# print(f"my Name is {a.name} and I am {a.age} years old.")



# Default constructor:-
# class Details:
#     def __init__ (self):
#         print(f"hello,my name is chetana")

# a=Details()





# class Animal:
#     def sound(self):
#         print("animal make a sound")

# class Dog (Animal):
#     def bark(self):
#         print("dog barks.")

# p1=Dog()
# p1.sound()
# p1.bark()







# class Animal:
#     def __init__(self,name):
#        self.name=name
# class Dog (Animal):
#     def bark(self):
#         print(f"My Amimal Name is {self.name}.")
#         print("dog barks.")



# p1=Dog("Tomi")
# p1.bark()







# INHERITANCE:-

# single inheritance:- child class inherite all the properties from single parent class.

# method 1 :-
# # Parent class
# class Animal:
#     def sound(self):
#         print("Animals make sounds")

# # Child class (inherits from Animal)
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")

# # Creating object of Dog
# d = Dog()
# d.sound()  # Inherited method
# d.bark()   # Dog's own method

  

# # real life Example :-
# class Person:
#     def show(self):
#         print("I am a person")

# class Student(Person):
#     def study(self):
#         print("I am studying")

# s = Student()
# s.show()    # Output: I am a person
# s.study()   # Output: I am studying



# method 2:-
# with constructor:-
# class Animal:
#     def __init__(self):
#         print("Animal is created")

# class Dog(Animal):
#     def __init__(self):
#         super().__init__()  # Calls parent constructor
#         print("Dog is created")

# d = Dog()







# # multipal inheritance:-child class inherite all properties and methods from more then one parent class.

# class Parent1:
#     def show1(self):
#         print("This is Parent1")

# class Parent2:
#     def show2(self):
#         print("This is Parent2")

# class Child(Parent1, Parent2):  # Inheriting from both
#     def show_child(self):
#         print("This is Child")

# c = Child()
# c.show1()
# c.show2()
# c.show_child()




# # method 2 :-

# class A:
#     def __init__(self):
#         print("A constructor")

# class B:
#     def __init__(self):
#         print("B constructor")

# class C(A, B):  # Inherits A first
#     def __init__(self):
#         super().__init__()  # Calls A's constructor
#         print("C constructor")

# c = C()






#multilevel inheritance:-
# methos:-1
# Base class (Grandparent)
# class Animal:
#     def speak(self):
#         print("Animal speaks")

# # Derived class (Parent)
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")

# # Further derived class (Child)
# class Puppy(Dog):
#     def weep(self):
#         print("Puppy weeps")

# # Creating an object of the Puppy class
# p = Puppy()

# # Accessing methods from all three classes
# p.speak()  # Inherited from Animal
# p.bark()   # Inherited from Dog
# p.weep()   # Defined in Puppy






# method:-2
# Base class (Grandparent)
# class Animal:
#     def __init__(self):
#         print("Animal is created")

#     def speak(self):
#         print("Animal speaks")

# Derived class (Parent)
# class Dog(Animal):
#     def __init__(self):
#         super().__init__()  # Calls Animal's constructor
#         print("Dog is created")

#     def bark(self):
#         print("Dog barks")

# # Further derived class (Child)
# class Puppy(Dog):
#     def __init__(self):
#         super().__init__()  # Calls Dog's constructor
#         print("Puppy is created")

#     def weep(self):
#         print("Puppy weeps")

# # Create object of Puppy
# p = Puppy()

# # Call methods
# p.speak()  # From Animal
# p.bark()   # From Dog
# p.weep()   # From Puppy






# hierarchical inheritance
# method:-1
# Parent class
# class Animal:
#     def sound(self):
#         print("Animal makes a sound")

# # Child class 1
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")

# # Child class 2
# class Cat(Animal):
#     def meow(self):
#         print("Cat meows")

# # Child class 3
# class Cow(Animal):
#     def moo(self):
#         print("Cow moos")

# # Creating objects
# d = Dog()
# c = Cat()
# cw = Cow()

# # Each child can use the parent method
# d.sound()
# d.bark()

# c.sound()
# c.meow()

# cw.sound()
# cw.moo()





# method:-2

# class Animal:
#     def __init__(self):
#         print("Animal created")

#     def sound(self):
#         print("Animal makes sound")

# class Dog(Animal):
#     def __init__(self):
#         super().__init__()
#         print("Dog created")

#     def bark(self):
#         print("Dog barks")

# class Cat(Animal):
#     def __init__(self):
#         super().__init__()
#         print("Cat created")

#     def meow(self):
#         print("Cat meows")

# # Create objects
# dog = Dog()
# cat = Cat()




# Hybrad inheritance
# # Base class
# class Person:
#     def show_person(self):
#         print("I am a person")

# # First derived class
# class Student(Person):
#     def show_student(self):
#         print("I am a student")

# # Second derived class
# class Employee(Person):
#     def show_employee(self):
#         print("I am an employee")

# # Derived from both Student and Employee
# class WorkingStudent(Student, Employee):
#     def show_working_student(self):
#         print("I am a working student")

# # Create object
# ws = WorkingStudent()

# # Access methods from all classes
# ws.show_person()         # From Person
# ws.show_student()        # From Student
# ws.show_employee()       # From Employee
# ws.show_working_student()  # Own method






# # Base class
# class Calculator:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

# # Derived class for addition
# class Add(Calculator):
#     def addition(self):
#         return self.a + self.b

# # Derived class for subtraction
# class Subtract(Calculator):
#     def subtraction(self):
#         return self.a - self.b

# # Derived class for multiplication
# class Multiply(Calculator):
#     def multiplication(self):
#         return self.a * self.b

# # Derived class for division
# class Divide(Calculator):
#     def division(self):
#         if self.b != 0:
#             return self.a / self.b
#         else:
#             return "Cannot divide by zero"











# return use:-
#  What is the return Statement in Python?
# The return statement is used inside a function to send back a value to the place where the function was called. What is the return Statement in Python?
# def function_name():
#     return value

# def multiply(x, y):
#     return x * y

# Call the function
# ans = multiply(4, 5)
# print("Multiplication is:", ans)
# def multiply(x, y):
#     return x * y

# # Call the function
# ans = multiply(4, 5)
# print("Multiplication is:", ans)
