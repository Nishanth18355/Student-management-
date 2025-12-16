students = []   # List to store student records

def add_student():
    roll = input("Enter Roll Number: ")
    fullname = input("Enter FullName: ")
    grade = input("Enter Grade: ")
    admissionnumber=input("Enter Admission number: ")
    percentage=input("Enter student Percentage: ")
    attendance=input(" Enter student attendance: ")
    students.append([roll, fullname, grade,admissionnumber,percentage,attendance])
    print("  Student added successfully!\n")

def display_students():
    if len(students) == 0:

        print(" No students available.\n")
    else:
        print("\n--- Student Records ---")
        for s in students:
            print("Roll No:", s[0], "| FullName:", s[1], "| Grade:", s[2], "| Admissionnumber:", s[3], "| Percentage:",s[4]," | Attendance:",s[5])
        print()

def search_student():
    roll = input("Enter Roll Number to search: ")
    for s in students:
        if s[0] == roll:
            print(" Student Found = Roll No:", s[0], "| fullName:", s[1], "| Grade:", s[2], "| Admissionnumber:", s[3], "| Percentage:",s[4]," | Attendance:",s[5] )
            return
    print(" Student not found.\n")

def update_student():
    roll = input("Enter Roll Number to update: ")
    for s in students:
        if s[0] == roll:
            name = input("Enter New Name: ")
            grade = input("Enter New Grade: ")
            admissionnumber=input("Enter New Admissionnumber: ")
            percentage=input("Enter New Percentage: ")
            attendance=input("Enter student attendance: ")
            s[1] = name
            s[2] = grade
            s[3] = admissionnumber
            s[4] = percentage
            s[5] = attendance
            print(" Student record updated!\n")
        return
    print(" Student not found.\n")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    for s in students:
        if s[0] == roll:
            students.remove(s)
            print(" Student deleted successfully!\n")
        return
    print(" Student not found.\n")

def show_studentattendance():
    roll = input("enter the roll number: ")
    for s in students:
        if s[0] == roll:
            print(" | Attendance Of student =" , s[5])
        return 
    print("Student has not found. \n")
# Menu
while True:
    print("===== School Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Attendance of Student")
    print("7. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
         show_studentattendance()
    elif choice == "7":
        print(" Exiting system. Goodbye!")
        break
    else:
        print(" Invalid choice! Try again.\n")