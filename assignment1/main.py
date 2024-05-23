import json
from department import Department
from employee  import Employee


class EmployeeManagementSystem:
    def __init__(self):
        self.company = {}

    def add_department(self, name):
        if name not in self.company:
            self.company[name] = Department(name)
            print(f"Department {name} added.")
        else:
            print("Department already exists!")

    def remove_department(self, name):
        if name in self.company:
            del self.company[name]
            print(f"Department {name} removed.")
        else:
            print("Department not found!")

    def display_departments(self):
        print("List of departments:")
        for department in self.company:
            print(department)

    def add_employee(self, name, emp_id, title, dept):
        if dept in self.company:
            emp = Employee(name, emp_id, title, dept)
            self.company[dept].add_employee(emp)
            print(f"Employee {name} added to {dept}.")
        else:
            print("Department not found!")

    def remove_employee(self, emp_id, dept):
        if dept in self.company:
            self.company[dept].remove_employee(emp_id)
        else:
            print("Department not found!")

    def display_dept_employees(self, dept):
        if dept in self.company:
            self.company[dept].list_employees()
        else:
            print("Department not found!")

    def save_data(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.company, file)
        print("Data saved successfully.")

    def load_data(self, filename):
        try:
            with open(filename, 'r') as file:
                self.company = json.load(file)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("File not found. Starting with an empty company.")
        except json.JSONDecodeError:
            print("Error decoding JSON. Starting with an empty company.")


def print_menu():
    print("\nEmployee Management System Menu:")
    print("1. Add Department")
    print("2. Remove Department")
    print("3. Display Departments")
    print("4. Add Employee")
    print("5. Remove Employee")
    print("6. Display Department Employees")
    print("7. Save Data")
    print("8. Load Data")
    print("9. Exit")


# Sample usage
if __name__ == "__main__":
    emp_sys = EmployeeManagementSystem()
    filename = "company_data.json"

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter department name: ")
            emp_sys.add_department(name)
        elif choice == "2":
            name = input("Enter department name to remove: ")
            emp_sys.remove_department(name)
        elif choice == "3":
            emp_sys.display_departments()
        elif choice == "4":
            name = input("Enter employee name: ")
            emp_id = input("Enter employee ID: ")
            title = input("Enter employee title: ")
            dept = input("Enter department to add employee to: ")
            emp_sys.add_employee(name, emp_id, title, dept)
        elif choice == "5":
            emp_id = input("Enter employee ID to remove: ")
            dept = input("Enter department: ")
            emp_sys.remove_employee(emp_id, dept)
        elif choice == "6":
            dept = input("Enter department to display employees: ")
            emp_sys.display_dept_employees(dept)
        elif choice == "7":
            emp_sys.save_data(filename)
        elif choice == "8":
            emp_sys.load_data(filename)
        elif choice == "9":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
