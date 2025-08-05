class Student1:
    def __init__(self, name, address,phone):
        self.name = name
        self.address=address
        self.phone= phone
    def display(self):
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Phone: {self.phone}")
    


# class Student2:
#     def __init__(self, name, address, phone):
#         self.name = name
#         self.address = address
#         self.phone = phone

#     def display(self):
#         print(f"Name: {self.name}")
#         print(f"Address: {self.address}")
#         print(f"Phone: {self.phone}")


student1 = Student1("Alice", "123 Main St", "123-456-7890")
student2 = Student1("Bob", "456 Elm St", "987-654-3210")

student1.display()  
student2.display()  


if student1==student2:
    print("Both students are the same.")
else:
    print("The students are different.")    
