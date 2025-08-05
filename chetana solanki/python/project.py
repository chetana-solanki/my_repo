class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks  # dictionary of subjects and marks

    def display(self):
        print(f"Roll No: {self.roll_no}, Name: {self.name}, Marks: {self.marks}")
        print(f"Average Marks: {self.get_average():.2f}")

    def get_average(self):
        return sum(self.marks.values()) / len(self.marks)

    def update_marks(self, subject, new_mark):
        self.marks[subject] = new_mark


class StudentRecordSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_all(self):
        if len(self.students) == 0:
            print("No student found")
        for student in self.students:
            student.display()
            print('-' * 40)

    def search_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                return student
        return None

    def delete_student(self, roll_no):
        student = self.search_student(roll_no)
        if student:
            self.students.remove(student)
            return True
        return False



system = StudentRecordSystem()

while True:
    print("\n--- Student Record System Menu ---")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student by Roll No")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        marks = {}
        for sub in ['Math', 'Science', 'English']:
            marks[sub] = int(input(f"Enter marks for {sub}: "))
        student = Student(roll, name, marks)
        system.add_student(student)
        print("Student added successfully.")

    elif choice == '2':
        system.display_all()

    elif choice == '3':
        roll = input("Enter Roll No to search: ")
        student = system.search_student(roll)
        if student:
            student.display()
        else:
            print("Student not found.")

    elif choice == '4':
        roll = input("Enter Roll No to update marks: ")
        student = system.search_student(roll)
        if student:
            subject = input("Enter subject to update: ")
            new_mark = int(input("Enter new mark: "))
            student.update_marks(subject, new_mark)
            print("Marks updated successfully.")
        else:
            print("Student not found.")

    elif choice == '5':
        roll = input("Enter Roll No to delete: ")
        if system.delete_student(roll):
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    elif choice == '6':
        print("Exiting the system.")
        break

    else:
        print("Invalid choice. Try again.")
