class Employees:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def wage(self):
        return self.wage()

    def employee(self):
        print(f" Employee name is {self.name} and is {self.age} years old")


class Department:
    def __init__(self, name="IT"):
        self.name = name
        self.employees = []

    def add_new(self, employee):
        self.employees.append(employee)
        return self.employees

    def remove(self,employee):
        self.employees.remove(employee)
        return self.employees

    def print_info(self):
        self.count = 0
        for employee in self.employees:
            print(f"Current Employees are: {employee.name}, {employee.age} years old and the paid wage is {employee.wage}.")
            self.count = employee.wage
        print(f"Total wage is {self.count}")

e = Employees("Armando", 32, 3500)
e1 = Employees("Andreea", 30, 4000)

d = Department()

d.add_new(e)
d.add_new(e1)
d.print_info()
d.remove(e1)
d.print_info()