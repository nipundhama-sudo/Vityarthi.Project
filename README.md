📚 MultiCourseSystem

A simple, interactive University Course & Student Management System built in Python.
This program allows you to register students, enroll them in courses, view course statistics, update enrollments, and delete student records — all through a console-based menu.

🔧 Features
✅ 1. Register Students

Add a new student using a unique student ID and name

Optionally enroll them in one course during registration

Automatically prevents duplicate student IDs

📘 2. View Available Courses

Shows the full course catalog

Displays how many students are enrolled in each course

Gives a quick snapshot of course popularity

👥 3. View All Students

Lists every student along with:

ID

Name

Courses they are enrolled in

Shows “None” if a student has no courses

🔄 4. Add or Drop Courses

Add a new course for a student

Remove an existing course

Validates your input and ensures courses exist in the catalog

❌ 5. Delete a Student

Permanently remove a student and their course enrollments

🚪 6. Exit

Clean, safe exit from the menu-driven system

🏛️ System Overview
📂 Student Database Structure

Each student is stored in a dictionary like:

{
    "102": {
        "name": "Aditya",
        "courses": ["Python Data Science", "Robotics 101"]
    }
}

📜 Course Catalog

A fixed list of available university courses:

["Python Data Science", "Robotics 101", "Web Development", "Cyber Security"]

🖥️ How It Works

Once you run the program, you’ll see this main menu:

=== UNIVERSITY MANAGER ===
1. Register Student
2. View Available Courses
3. View All Students
4. Add/Drop Courses
5. Remove Student
6. Exit


Just enter a number between 1–6 to perform the desired action.
All operations happen in real-time — no external database required.

🏁 Getting Started
Step 1 — Save the Code

Save the Python script (e.g., multi_course_system.py).

Step 2 — Run the Program

Open your terminal and run:

python multi_course_system.py

Step 3 — Use the Menu

Follow the on-screen instructions to manage your student database.

🧠 Why This Project Is Useful

This program is excellent for:

Learning Object-Oriented Programming (OOP)

Understanding CRUD operations (Create, Read, Update, Delete)

Practicing user-input handling in console applications

Building foundational logic for larger student-management systems

🚀 Future Improvements (Optional Ideas)

Add multiple course selection during registration

Save data to a file (JSON or CSV)

Add search functionality

Create a GUI using Tkinter or PyQt

Integrate course prerequisites or credit systems
