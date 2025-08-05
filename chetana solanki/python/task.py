# class Calculator:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
     
# class Add(Calculator):
#     def add (self):
#         return self.a+self.b
# a=Add(4,3)
# print(a.add())





# Base class
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



# class Calculator:
#     def add (self,a,b):
#         return a+b
    
# c=Calculator()
# result=c.add(4,3)
# print(result)




# class Calculator:
#     def add (self,a,b):
#         return a+b,a-b,a*b
    
# c=Calculator()
# result=c.add(8,3)
# print(result)





# calculater :-

# class Calculator:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b

# class Add(Calculator):
#     def addition(self):
#         print("addition of a and b is:",self.a+self.b)


# class Sub(Calculator):
#     def subtraction(self):
#         print("subtraction of a and b is:",self.a-self.b)


# class Mul(Calculator):
#     def multiplication(self):
#         print("multiplication of a and b is:",self.a*self.b)



# class Div(Calculator):
#     def division(self):
#         print("division of a and b is:",self.a/self.b)


# a=Add(10,2)
# a.addition()

# s=Sub(12,5)
# s.subtraction()

# m=Mul(5,2)
# m.multiplication()

# d=Div(10,5)
# d.division()


# class Fullcalculator(Add,Sub,Mul,Div):
#     def __init__(self, a, b):
#         super().__init__(a, b)


# x=int(input("Enter First number:"))
# y=int(input("Enter Second number:"))


# c=Fullcalculator(x,y)

# c.addition()
# c.subtraction()
# c.multiplication()
# c.division()












# class Calculator:
#     def __init__(self, a, b):
#         self.a=a
#         self.b=b
    
#     def show_result(self):
#         print(self.a + self.b)

#     def select_operator(self):



# while True:
#     a=int(input("Enter first number:"))
#     b=int(input("Enter second number:"))
#     obj = Calculator(a, b)
#     operator = input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division")
#     if operator == '1':
#         print(a+b)
#     elif operator == '2':
#         print(a-b)
#     elif operator == '3':
#         print(a*b)
#     elif operator == '4':
#         print(a/b)
#     else:
#         print("Wrong operator")
#     flag=input("Enter Y to continue")
    
#     if flag != 'Y':
#         print("Thanks for using calculatoe=r, exiting now")
#         break




class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        print(self.a + self.b)

    def subtract(self):
        print(self.a - self.b)

    def multiply(self):
        print(self.a * self.b)

    def divide(self):
        if self.b != 0:
            print(self.a / self.b)
        else:
            print("Error: Division by zero")



while True:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")

    calc = Calculator(a, b)

    if operator == "+":
        calc.add()
    elif operator == "-":
        calc.subtract()
    elif operator == "*":
        calc.multiply()
    elif operator == "/":
        calc.divide()
    else:
        print("Invalid operator!")

    choice = input("Do you want to continue? (yes/no): ").lower()
    if choice != "yes":
        print("Exiting calculator. Goodbye!")
        break




