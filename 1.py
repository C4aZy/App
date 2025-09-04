import json
import os

EMPLOYEE_FILE = "employees.json"
def leave():
    employee_name = input('Enter your name registered with the company: ')
    try:
        a = int(input("Enter the number of days you want leave: "))
    except ValueError:
        print("Invalid input for number of days.")
        return
    if a > 10:  # Existing leave function
        print("State your leave emergency:\nOptions are:\nhospital\nfamily_gathering\nwedding or party of family\nanything else")
        b = input("Tell why you want a leave: ").strip()
        if b == "hospital":
            print(f"{employee_name} will get paid leave for 10 days. Enjoy your paid and unpaid leaves. {a-10} days of leave will be unpaid.")
        elif b == "family_gathering":
            print(f"{employee_name} will get a paid leave for 7 days. Enjoy your paid and unpaid leaves. {a-7} days of leave will be unpaid.")
        elif b == "wedding or party of family":
            print(f"{employee_name} will get a paid leave for 5 days. Enjoy your paid and unpaid leaves. {a-5} days of leave will be unpaid.")
        elif b == "anything else":
            print(f"{employee_name} will get a paid leave of 3 days. Enjoy your paid and unpaid leaves. {a-3} days of leave will be unpaid.")
        else:
            print(f"{employee_name} will get a leave which is fully unpaid. Enjoy the leave.")
    else:
        print(f"{employee_name} will get {a} days of paid leave.")
    
def load_employees():
    if os.path.exists(EMPLOYEE_FILE):
        with open(EMPLOYEE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_employees(employees):
    with open(EMPLOYEE_FILE, "w") as f:
        json.dump(employees, f, indent=2)

def add_employee(employees):
    name = input("Enter employee name: ").strip()
    if name in employees:
        print("Employee already exists.")
        return
    position = input("Enter position: ").strip()
    years = int(input("Enter years worked: "))
    employees[name] = {
        "position": position,
        "years": years,
        "leaves": 0,
        "salary": 0
    }
    save_employees(employees)
    print("Employee added.")

def view_employee(employees):
    name = input("Enter employee name: ").strip()
    emp = employees.get(name)
    if emp:
        print(json.dumps(emp, indent=2))
    else:
        print("Employee not found.")

def update_employee(employees):
    name = input("Enter employee name: ").strip()
    if name not in employees:
        print("Employee not found.")
        return
    position = input("Enter new position: ").strip()
    years = int(input("Enter new years worked: "))
    employees[name]["position"] = position
    employees[name]["years"] = years
    save_employees(employees)
    print("Employee updated.")

def delete_employee(employees):
    name = input("Enter employee name: ").strip()
    if name in employees:
        del employees[name]
        save_employees(employees)
        print("Employee deleted.")
    else:
        print("Employee not found.")

def list_employees(employees):
    if not employees:
        print("No employees found.")
        return
    for name in employees:
        print(name)

def salary():
    employee_name = input('Enter your name registered with the company: ')
    try:
        b = int(input("Enter the number of days you worked in a month: "))
    except ValueError:
        print("Invalid input for number of days.")
        return
    if b >= 20:
        print(f"{employee_name} will get full salary.")
    elif b >= 10:
        print(f"{employee_name} will get 75% of salary.")
    elif b >= 5:
        print(f"{employee_name} will get 50% of salary.")
    else:
        print(f"{employee_name} will get 25% of salary.")

def salary_hike():
    employee_name = input('Enter your name registered with the company: ')
    try:
        c = int(input("Enter the number of years you worked in the company: "))
    except ValueError:
        print("Invalid input for number of years.")
        return
    if c >= 5:
        print(f"{employee_name} will get 20% hike in salary.")
    elif c >= 3:
        print(f"{employee_name} will get 10% hike in salary.")
    elif c >= 1:
        print(f"{employee_name} will get 5% hike in salary.")
    else:
        print(f"{employee_name} will not get any hike in salary.")

def promotion():
    employee_name = input('Enter your name registered with the company: ')
    try:
        d = int(input("Enter the number of years you worked in the company: "))
    except ValueError:
        print("Invalid input for number of years.")
        return
    e = input("Enter the position you are working in currently:\nOptions are:\nassistant manager\nmanager\nsenior manager\n").strip().lower()
    if d >= 5 and e == "assistant manager":
        print(f"{employee_name} will be promoted to manager.")
    elif d >= 3 and e == "manager":
        print(f"{employee_name} will be promoted to senior manager.")
    elif d >= 1 and e == "senior manager":
        print(f"{employee_name} will be promoted to general manager.")
    else:
        print(f"{employee_name} will not get any promotion.")

def main():
    employees = load_employees()
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employee")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. List Employees")
        print("6. Apply for Leave")
        print("7. Calculate Salary")
        print("8. Request Salary Hike")
        print("9. Promotion Request")
        print("0. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice.")
            continue
        if choice == 1:
            add_employee(employees)
        elif choice == 2:
            view_employee(employees)
        elif choice == 3:
            update_employee(employees)
        elif choice == 4:
            delete_employee(employees)
        elif choice == 5:
            list_employees(employees)
        elif choice == 6:
            leave(employees)
        elif choice == 7:
            salary()
        elif choice == 8:
            salary_hike()
        elif choice == 9:
            promotion()
        elif choice == 0:
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
def salary():
    employee_name = input('Enter your name registered with the company: ')
    try:
        b = int(input("Enter the number of days you worked in a month: "))
    except ValueError:
        print("Invalid input for number of days.")
        return
    if b >= 20:
        print(f"{employee_name} will get full salary.")
    elif b >= 10:
        print(f"{employee_name} will get 75% of salary.")
    elif b >= 5:
        print(f"{employee_name} will get 50% of salary.")
    else:
        print(f"{employee_name} will get 25% of salary.")
def salary_hike():
    employee_name = input('Enter your name registered with the company: ')
    try:
        c = int(input("Enter the number of years you worked in the company: "))
    except ValueError:
        print("Invalid input for number of years.")
        return
    if c >= 5:
        print(f"{employee_name} will get 20% hike in salary.")
    elif c >= 3:
        print(f"{employee_name} will get 10% hike in salary.")
    elif c >= 1:
        print(f"{employee_name} will get 5% hike in salary.")
    else:
        print(f"{employee_name} will not get any hike in salary.")
def promotion():
    employee_name = input('Enter your name registered with the company: ')
    try:
        d = int(input("Enter the number of years you worked in the company: "))
    except ValueError:
        print("Invalid input for number of years.")
        return
    e = input("Enter the position you are working in currently:\nOptions are:\nassistant manager\nmanager\nsenior manager\n").strip().lower()
    if d >= 5 and e == "assistant manager":
        print(f"{employee_name} will be promoted to manager.")
    elif d >= 3 and e == "manager":
        print(f"{employee_name} will be promoted to senior manager.")
    elif d >= 1 and e == "senior manager":
        print(f"{employee_name} will be promoted to general manager.")
    else:
        print(f"{employee_name} will not get any promotion.")

def main():
    print("Enter your choice:\n1. Employee Leave\n2. Employee Salary\n3. Employee Salary Hike\n4. Employee Promotion")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice.")
        return
    if choice == 1:
        leave()
    elif choice == 2:
        salary()
    elif choice == 3:
        salary_hike()
    elif choice == 4:
        promotion()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()



