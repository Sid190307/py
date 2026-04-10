class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display_details(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)

class Manager(Employee):
    def approve_leave(self):
        print("Manager has approved the leave")

class Developer(Employee):
    def write_code(self):
        print("Developer is writing code")

class Clerk(Employee):
    def maintain_records(self):
        print("Clerk is maintaining records")

emp_id = int(input("Enter Manager ID: "))
name = input("Enter Manager Name: ")
salary = int(input("Enter Manager Salary: "))
m = Manager(emp_id, name, salary)

emp_id = int(input("\nEnter Developer ID: "))
name = input("Enter Developer Name: ")
salary = int(input("Enter Developer Salary: "))
d = Developer(emp_id, name, salary)

emp_id = int(input("\nEnter Clerk ID: "))
name = input("Enter Clerk Name: ")
salary = int(input("Enter Clerk Salary: "))
c = Clerk(emp_id, name, salary)

m.display_details()
m.approve_leave()

d.display_details()
d.write_code()

c.display_details()
c.maintain_records()
