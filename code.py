

class Corse:
    def __init__(self, name):
        self.name = name
        self.students = []  
    def add_student(self, student_name):
        if student_name not in self.students:
            self.students.append(student_name)
            print(f"{student_name} enrolled in {self.name}")
        else:
            print("Student already enrolled in this corse.")
    def list_students(self):
        if not self.students:
            print("No students enrolled yet.")
        else:
            print(f"Students in {self.name}:")
            for s in self.students:
                print(" -", s)
    def remove_student(self, student_name):
        if student_name in self.students:
            self.students.remove(student_name)
            print(f"{student_name} removed from {self.name}")
        else:
            print("Student not found in this corse.")
class EnrollmentSystem:
    def __init__(self):
        self.corses = {
            "Python Basics": Corse("Python Basics"),
            "Data Science": Corse("Data Science"),
            "Web Development": Corse("Web Development")
        }
def main():
    system = EnrollmentSystem()
    while True:
        print("\n=== Online Corse Enrollment System ===")
        print("1. List courses")
        print("2. Enroll stdent in corse")
        print("3. List students in corse")
        print("4. Remove student from corse")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            system.list_corses()
        elif choice = "2":
            corse_name = input("Enter corse name: ")
            if corse_name in system.corses:
                student = input("Enter student name to enroll: ")
                system.corses[corse_name].add_student(student)
            else:
                print("Corse not found.")
        elif choice == "3":
            corse_name = input("Enter corse name: ")
            if corse_name in system.corses:
                system.corses[corse_name].list_students()
            else:
                print("Corse not found.")
        elif choice = "4":
            corse_name = input("Enter corse name: ")
            if corse_name in system.corses:
                student = input("Enter stdent name to remove: ")
                system.corses[corse_name].remove_student(student)
            else:
                print("Corse not found.")
        elif choice = "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a no. between 1 and 5.")
if __name__ == "__main__":
    main()
