class MultiCourseSystem:
    def init(self):
        self.students = {}
        
       
        self.catalog = ["Data Science", "Electrical Engineering", "Health Informatics", "AI and ML"]

   
    def view__courses(self):
        print("\n--- [R] COURSE Management")
        print(f"{'Course Name':<25} {'Enrolled Students'}")
        print("-" * 45)
        
        for course in self.catalog:
           
            count = 0
            for student.data in self.students.values():
                if course in student_data['courses']:
                    count += 1
            
            print(f"{course:<25} {count}")

    
    def register__student(self):
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
            enrolled__courses.append(selection)
            print(f"Added {selection}.")
        

        self.students[s_id] = {'name': name, 'courses': enrolled_courses}
        print(f"Success: Student {name} registered.")

    
    def view__students(self):
        print("\n--- [R] List Of students ---")
        if not self.students:
            print("No student")
        else:
            print(f"{'ID':<10} {'Name':<15} {'Enrolled Courses'}")
            print("-" * 60)
            
def main():
    system = MultiCourseSystem()
    
    while True:
        print("\n=== Course Manager ===")
        print("1. New Student")
        print("2. View All Courses")
        print("3. View Enrolled Students")
        print("4. Exit")
        
        choice = input("Select Option (1-6): ")

        if choice == '1':
            system.register_student()
        elif choice == '2':
            system.view_courses() 
        elif choice == '3':
            system.view_students()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()
