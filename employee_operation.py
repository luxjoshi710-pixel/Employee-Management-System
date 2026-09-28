
import sqlite3
print("employee_operation file loaded")
def add_employee():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    department = input("Enter  department: ")
    salary = int(input("Enter salary: "))

    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()

    cursor.execute(" INSERT INTO employee (name, age, department, salary) VALUES (?, ?, ?, ?)",
                    (name, age, department, salary))


    conn.commit()
    conn.close()

    print("Employee added successfully.")

def view_employee():
    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employee")
    employees = cursor.fetchall()

    if employees:
        print("\n--- Employee List ---")
        for emp in employees:
            print(f"ID: {emp[0]}, Name: {emp[1]}, Age: {emp[2]}, Department: {emp[3]}, Salary: {emp[4]}")
    else:
        print("No employees found.")

    conn.close()

def search_employee():
    name = input("Enter name to search: ")

    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employee WHERE name LIKE ?", ('%' + name + '%',))
    employees = cursor.fetchall()

    if employees:
        print("\n--- Search Results ---")
        for emp in employees:
            print(f"ID: {emp[0]}, Name: {emp[1]}, Age: {emp[2]}, Department: {emp[3]}, Salary: {emp[4]}")
    else:
        print("No employees found with that name.")

    conn.close()

def update_employee():
    emp_id = int(input("Enter employee ID to update: "))
    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    department = input("Enter new department: ")
    salary = int(input("Enter new salary: "))

    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE employee 
    SET name = ?, age = ?, department = ?, salary = ? 
    WHERE id = ?
    """, (name, age, department, salary, emp_id))

    if cursor.rowcount > 0:
        print("Employee updated successfully.")
    else:
        print("Employee not found.")

    conn.commit()
    conn.close()

def delete_employee():
    emp_id = int(input("Enter employee ID to delete: "))

    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM employee WHERE id = ?", (emp_id,))

    if cursor.rowcount > 0:
        print("Employee deleted successfully.")
    else:
        print("Employee not found.")

    conn.commit()
    conn.close()


