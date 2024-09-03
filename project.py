# Initialising dictionary
student_grades = {}

# Add a new student
def add_student(name, grade):
    """Adds a new student to the student grades dictionary."""
    student_grades[name] = grade
    print(f"Added {name} with a grade of {grade}")

# Update student
def update_student(name, grade):
    """Updates the grade of an existing student."""
    if name in student_grades:
        student_grades[name] = grade
        print(f"Updated {name} with a grade of {grade}")
    else:
        print(f"{name} not found!")

# Delete a student
def delete_student(name):
    """Deletes a student from the student grades dictionary."""
    if name in student_grades:
        del student_grades[name]
        print(f"Deleted {name}")
    else:
        print(f"{name} not found!")

# View all students
def display_all_students():
    """Displays all students and their grades."""
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")
    else:
        print("No students found/added")

def main():
    while True:
        print("\nStudent Grades Management System")
        print("1. Add student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Student")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        if choice == 1:
            name = input("Enter student name: ")
            try:
                grade = int(input("Enter student grade: "))
            except ValueError:
                print("Invalid input. Please enter an integer.")
                continue
            add_student(name, grade)

        elif choice == 2:
            name = input("Enter student name: ")
            try:
                grade = int(input("Enter student grade: "))
            except ValueError:
                print("Invalid input. Please enter an integer.")
                continue
            update_student(name, grade)

        elif choice == 3:
            name = input("Enter student name: ")
            delete_student(name)

        elif choice == 4:
            display_all_students()

        elif choice == 5:
            print("Closing the program...")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()