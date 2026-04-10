from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def display_info(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

    def display_info(self):
        print("Full-Time Employee")
        print("Name:", self.name)
        print("Monthly Salary:", self.calculate_salary())

class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

    def display_info(self):
        print("Part-Time Employee")
        print("Name:", self.name)
        print("Salary:", self.calculate_salary())

f = FullTimeEmployee("Rahul", 30000)
p = PartTimeEmployee("Amit", 200, 40)

f.display_info()
print() 
p.display_info()
