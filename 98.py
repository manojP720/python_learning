students = {}

def add_student():
    usn = input("Enter USN: ")
    name = input("Enter Name: ")
    branch = input("Enter Branch: ")

    students[usn] = {
        "Name": name,
        "Branch": branch
    }

    print("\nStudent Added Successfully!\n")


def view_students():
    if not students:
        print("\nNo Records Found.\n")
        return

    print("\n----- Student Records -----")
    for usn, details in students.items():
        print(f"USN    : {usn}")
        print(f"Name   : {details['Name']}")
        print(f"Branch : {details['Branch']}")
        print("-" * 25)


def search_student():
    usn = input("Enter USN to Search: ")

    if usn in students:
        print("\nStudent Found")
        print(f"Name   : {students[usn]['Name']}")
        print(f"Branch : {students[usn]['Branch']}")
    else:
        print("\nStudent Not Found")


def delete_student():
    usn = input("Enter USN to Delete: ")

    if usn in students:
        del students[usn]
        print("\nStudent Deleted Successfully!")
    else:
        print("\nStudent Not Found")


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("\nThank You!")
        break
    else:
        print("\nInvalid Choice!")