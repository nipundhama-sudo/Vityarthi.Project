class MultiCourseSystem:
    def __init__(self):
        # Database: { ID: {'name': 'Aditya', 'courses': ['Python', 'Robotics']} }
        self.students = {}
        
        # The University course list
        self.catalog = ["Python Data Science", "Robotics 101", "Web Development", "Cyber Security"]

    # Feature for viewing courses
    def view_courses(self):
        print("\n--- [R] COURSE CATALOG & STATISTICS ---")
        print(f"{'Course Name':<25} {'Enrolled Students'}")
        print("-" * 45)
        
        for course in self.catalog:
            # Calculate how many students have this course in their list
            count = 0
            for student_data in self.students.values():
                if course in student_data['courses']:
                    count += 1
            
            print(f"{course:<25} {count}")

    # Creating a new registration
    def register_student(self):
        print("\n--- [C] NEW REGISTRATION ---")
        s_id = input("Enter Student ID: ")
        
        if s_id in self.students:
            print("Error: ID already exists.")
            return

        name = input("Enter Student Name: ")
        
        # Show list for selection
        print("\nAvailable Courses:")
        for i, c in enumerate(self.catalog, 1):
            print(f"{i}. {c}")
        
        print("Type the exact name of the course to enroll (or 'skip'):")
        selection = input("Course Name: ").strip()

        enrolled_courses = []
        if selection in self.catalog:
            enrolled_courses.append(selection)
            print(f"Added {selection}.")
        elif selection.lower() != 'skip':
            print("Invalid course. Registered with 0 courses.")

        self.students[s_id] = {'name': name, 'courses': enrolled_courses}
        print(f"Success: Student {name} registered.")

    # Checking for the students enrolled in the courses
    def view_students(self):
        print("\n--- [R] STUDENT ENROLLMENTS ---")
        if not self.students:
            print("No students found.")
        else:
            print(f"{'ID':<10} {'Name':<15} {'Enrolled Courses'}")
            print("-" * 60)
            for s_id, data in self.students.items():
                course_str = ", ".join(data['courses']) if data['courses'] else "None"
                print(f"{s_id:<10} {data['name']:<15} {course_str}")

    # Add/Drop
    def update_enrollment(self):
        print("\n--- [U] ADD/DROP COURSES ---")
        s_id = input("Enter Student ID: ")
        
        if s_id in self.students:
            student = self.students[s_id]
            print(f"Student: {student['name']} | Courses: {student['courses']}")
            
            action = input("Do you want to (1) Add Course or (2) Drop Course? ")
            
            if action == '1':
                new_course = input("Enter exact course name to add: ")
                if new_course in self.catalog:
                    if new_course not in student['courses']:
                        student['courses'].append(new_course)
                        print("Success: Course added.")
                    else:
                        print("Error: Already enrolled.")
                else:
                    print("Error: Course not in catalog.")
            
            elif action == '2':
                drop_course = input("Enter exact course name to drop: ")
                if drop_course in student['courses']:
                    student['courses'].remove(drop_course)
                    print("Success: Course dropped.")
                else:
                    print("Error: Not enrolled in this course.")
        else:
            print("Error: ID not found.")

    # Deleting a profile
    def delete_student(self):
        print("\n--- [D] REMOVE STUDENT ---")
        s_id = input("Enter Student ID: ")
        if s_id in self.students:
            del self.students[s_id]
            print("Success: Student deleted.")
        else:
            print("Error: ID not found.")

# Main menu 
def main():
    system = MultiCourseSystem()
    
    while True:
        print("\n=== UNIVERSITY MANAGER ===")
        print("1. Register Student")
        print("2. View Available Courses")  # <-- NEW OPTION
        print("3. View All Students")
        print("4. Add/Drop Courses")
        print("5. Remove Student")
        print("6. Exit")
        
        choice = input("Select Option (1-6): ")

        if choice == '1':
            system.register_student()
        elif choice == '2':
            system.view_courses()  # <-- CALLS NEW FUNCTION
        elif choice == '3':
            system.view_students()
        elif choice == '4':
            system.update_enrollment()
        elif choice == '5':
            system.delete_student()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()