class MultiCourseSystem:
    def __init__(self):
        self.students = {}
        
       
        self.catalog = ["Data Science", "Robotics ", "Web Development", "Cyber Security"]

   
    def view_courses(self):
        print("\n--- [R] COURSE Management")
        print(f"{'Course Name':<25} {'Enrolled Students'}")
        print("-" * 45)
        
        for course in self.catalog:
           
            count = 0
            for student_data in self.students.values():
                if course in student_data['courses']:
                    count += 1
            
            print(f"{course:<25} {count}")

    
    def register_student(self):
        print("\n--- [C] New Student---")
        s_id = input("Enter Student ID: ")
        
        

        name = input("Enter Student Name: ")
        
        
        print("\nAll Courses:")
        for i, c in enumerate(self.catalog, 1):
            print(f"{i}. {c}")
        
        print("Type the exact name of the course to enroll :")
        selection = input("Course Name: ").strip()

        enrolled_courses = []
        if selection in self.catalog:
            enrolled_courses.append(selection)
            print(f"Added {selection}.")
        

        self.students[s_id] = {'name': name, 'courses': enrolled_courses}
        print(f"Success: Student {name} registered.")

    
    def view_students(self):
        print("\n--- [R] List Of students ---")
        if not self.students:
            print("No students found.")
        else:
            print(f"{'ID':<10} {'Name':<15} {'Enrolled Courses'}")
            print("-" * 60)
            for s_id, data in self.students.items():
                course_str = ", ".join(data['courses']) if data['courses'] else "None"
                print(f"{s_id:<10} {data['name']:<15} {course_str}")

   
    def update_enrollment(self):
        print("\n--- [U] Edit COURSES ---")
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

    
    def delete_student(self):
        print("\n--- [D] Delete  STUDENT ---")
        s_id = input("Enter Student ID: ")
        if s_id in self.students:
            del self.students[s_id]
            print("Success: Student deleted.")
        else:
            print("Error: ID not found.")


def main():
    system = MultiCourseSystem()
    
    while True:
        print("\n=== Course Manager ===")
        print("1. New Student")
        print("2. View All Courses")
        print("3. View Enrolled Students")
        print("4. Edit Courses")
        print("5. Remove Student")
        print("6. Exit")
        
        choice = input("Select Option (1-6): ")

        if choice == '1':
            system.register_student()
        elif choice == '2':
            system.view_courses() 
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
