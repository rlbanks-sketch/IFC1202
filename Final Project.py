import os

VALID_STATES = {
    # 50 states + DC
    "AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA",
    "HI","ID","IL","IN","IA","KS","KY","LA","ME","MD",
    "MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ",
    "NM","NY","NC","ND","OH","OK","OR","PA","RI","SC",
    "SD","TN","TX","UT","VT","VA","WA","WV","WI","WY","DC"
}

class Employee:
    def __init__(self, employee_number:int, first_name:str, last_name:str, address:str, city:str, state:str, zip_code:str):
        # Validation done before setting attributes
        if not isinstance(employee_number, int):
            raise ValueError("Employee Number must be an integer")
        if not first_name.strip():
            raise ValueError("First Name is required")
        if not last_name.strip():
            raise ValueError("Last Name is required")
        if not address.strip():
            raise ValueError("Address is required")
        if not city.strip():
            raise ValueError("City is required")
        if state not in VALID_STATES:
            raise ValueError("State must be a valid upper case state abbreviation")
        if len(zip_code) != 5 or not zip_code.isdigit():
            raise ValueError("Zip must be 5 numeric digits")

        self.employee_number = employee_number
        self.first_name = first_name.strip()
        self.last_name = last_name.strip()
        self.address = address.strip()
        self.city = city.strip()
        self.state = state
        self.zip_code = zip_code

class EmployeeList:
    def __init__(self, filename:str):
        self.filename = filename
        self.employees = []  # list of Employee objects
        self.ReadEmployeeFile()

    def ReadEmployeeFile(self):
        """Open filename and read employees into list."""
        self.employees.clear()
        if not os.path.exists(self.filename):
            # File does not exist; no employees yet
            return
        with open(self.filename, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = [part.strip() for part in line.split(",")]
                if len(parts) != 7:
                    # Skip invalid lines
                    print(f"Skipping invalid line: {line}")
                    continue
                try:
                    emp_num = int(parts[0])
                    first = parts[1]
                    last = parts[2]
                    address = parts[3]
                    city = parts[4]
                    state = parts[5].upper()
                    zip_code = parts[6]
                    emp = Employee(emp_num, first, last, address, city, state, zip_code)
                    self.employees.append(emp)
                except Exception as e:
                    print(f"Error reading employee from line: {line}\n  {e}")

    def WriteEmployeeFile(self):
        """Write all employee data in CSV format to file."""
        with open(self.filename, "w") as file:
            for emp in self.employees:
                line = f"{emp.employee_number}, {emp.first_name}, {emp.last_name}, {emp.address}, {emp.city}, {emp.state}, {emp.zip_code}\n"
                file.write(line)

    def DisplayEmployeeList(self):
        """Print headings and all employee data."""
        print()
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "Employee", "First", "Last", "Address", "City", "State", "Zip"))
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            "Number", "Name", "Name", "", "", "", ""))
        print("-"*15*7)
        for emp in self.employees:
            print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
                emp.employee_number, emp.first_name, emp.last_name, emp.address,
                emp.city, emp.state, emp.zip_code))
        print()

    def FindEmployee(self, employee_number:int):
        """Return index if employee found; else -1"""
        for idx, emp in enumerate(self.employees):
            if emp.employee_number == employee_number:
                return idx
        return -1

    def ReadEmployee(self, employee_number:int):
        """Return the employee object for employee_number or None if not found"""
        idx = self.FindEmployee(employee_number)
        if idx == -1:
            return None
        return self.employees[idx]

    def NextEmployeeNumber(self):
        """Get last employee number +1, or 1 if none."""
        if not self.employees:
            return 1
        last_number = max(emp.employee_number for emp in self.employees)
        return last_number + 1

    def AddEmployee(self, first_name, last_name, address, city, state, zip_code):
        emp_num = self.NextEmployeeNumber()
        emp = Employee(emp_num, first_name, last_name, address, city, state, zip_code)
        self.employees.append(emp)
        print("Employee Added")

    def UpdateEmployee(self, employee_number, first_name, last_name, address, city, state, zip_code):
        idx = self.FindEmployee(employee_number)
        if idx == -1:
            print("Employee not found")
            return False
        try:
            emp = Employee(employee_number, first_name, last_name, address, city, state, zip_code)
            self.employees[idx] = emp
            return True
        except Exception as e:
            print(f"Error updating employee: {e}")
            return False

    def DeleteEmployee(self, employee_number):
        idx = self.FindEmployee(employee_number)
        if idx == -1:
            print("Employee not found")
            return False
        del self.employees[idx]
        print("Employee Deleted")
        return True

def input_required(prompt):
    while True:
        val = input(prompt).strip()
        if val:
            return val
        else:
            print("This field is required.")

def input_state(prompt):
    while True:
        val = input(prompt).strip().upper()
        if val in VALID_STATES:
            return val
        else:
            print("Invalid state. Please enter a valid 2-letter uppercase state abbreviation.")

def input_zip(prompt):
    while True:
        val = input(prompt).strip()
        if len(val) == 5 and val.isdigit():
            return val
        else:
            print("Invalid zip code. Must be 5 numeric digits.")

def main():
    filename = "Final Project Employees.txt"
    emp_list = EmployeeList(filename)

    while True:
        print("(A)dd a New Employee")
        print("(D)elete an Existing Employee")
        print("(C)hange an Existing Employee")
        print("(P)rint All Employees")
        print("(S)ave Changes to File")
        print("(Q)uit\n")
        selection = input("Enter Selection: ").strip().upper()

        if selection == "A":
            # Add new employee
            first = input_required("Enter First Name: ")
            last = input_required("Enter Last Name: ")
            address = input_required("Enter Address: ")
            city = input_required("Enter City: ")
            state = input_state("Enter State: ")
            zip_code = input_zip("Enter Zip: ")

            try:
                emp_list.AddEmployee(first, last, address, city, state, zip_code)
            except Exception as e:
                print(f"Error adding employee: {e}")

        elif selection == "D":
            # Delete employee
            try:
                emp_num_str = input("Enter Employee Number: ").strip()
                emp_num = int(emp_num_str)
            except:
                print("Invalid Employee Number")
                continue

            emp_list.DeleteEmployee(emp_num)

        elif selection == "C":
            # Change employee
            try:
                emp_num_str = input("Enter Employee Number: ").strip()
                emp_num = int(emp_num_str)
            except:
                print("Invalid Employee Number")
                continue

            emp = emp_list.ReadEmployee(emp_num)
            if emp is None:
                print("Employee not found")
                continue

            while True:
                print()
                print("(F)irst Name")
                print("(L)Last Name")
                print("(A)ddress")
                print("(C)ity")
                print("(S)tate")
                print("(Z)ip")
                print("(B)ack to Main Menu\n")
                choice = input("Enter Selection: ").strip().upper()

                if choice == "F":
                    first = input_required("Enter First Name: ")
                    emp.first_name = first
                    print("First Name updated.")
                elif choice == "L":
                    last = input_required("Enter Last Name: ")
                    emp.last_name = last
                    print("Last Name updated.")
                elif choice == "A":
                    address = input_required("Enter Address: ")
                    emp.address = address
                    print("Address updated.")
                elif choice == "C":
                    city = input_required("Enter City: ")
                    emp.city = city
                    print("City updated.")
                elif choice == "S":
                    state = input_state("Enter State: ")
                    emp.state = state
                    print("State updated.")
                elif choice == "Z":
                    zip_code = input_zip("Enter Zip: ")
                    emp.zip_code = zip_code
                    print("Zip updated.")
                elif choice == "B":
                    break
                else:
                    print("Invalid selection.")

                # After update, replace employee in list
                idx = emp_list.FindEmployee(emp.employee_number)
                if idx != -1:
                    emp_list.employees[idx] = emp  # Update employee record

        elif selection == "P":
            # Print all employees
            emp_list.DisplayEmployeeList()

        elif selection == "S":
            # Save to file
            emp_list.WriteEmployeeFile()
            print("Changes Saved")

        elif selection == "Q":
            print("Good-bye")
            break

        else:
            print("Invalid selection. Please enter A, D, C, P, S, or Q.")

if __name__ == "__main__":
    main()
