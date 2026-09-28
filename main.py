
from database import create_table
from employee_operation import (
    add_employee, 
    view_employee,
    search_employee,
    update_employee, 
    delete_employee
    )

print(" program started")


def main():

 while True:

    print("\n--- Employee Management System ---")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
     view_employee()
     
    elif choice == "3":
     search_employee()

    elif choice == "4":
        update_employee()

    elif choice == "5":
        delete_employee()

    elif choice == "6":
         print("Exiting program...")

    break
 else:
    
    print("Invalid choice. Please try again.")

if __name__ == "__main__":
    
    create_table()
    main()
    