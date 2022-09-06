#Class Person
#Class Angajat ce mosteneste din Person
#O Clasa Manager ce mosteneste din Person
#Proprietati identice (nume, varsta, pozitie)
#Acces diferit intr-o aplicatie in companie

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


    def show_info(self):
        print(f"My name is {self.name} and i am {self.age} years old")
        print(f"Gender: {self.gender}")

class Employee(Person):
    def __init__(self,name, age, gender):
        super().__init__(name, age, gender)

class Worker(Employee):
    def __init__(self, name, age, gender):
        super(). __init__(name, age, gender)
        self.rights = 1


class Manager(Employee):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.rights = 10

class Company:
    def __init__(self,coName):
        self.coName = coName
        self.employee = []

    def add_emplotyee(self,employee):
        self.employees.append(employee)
        return self.employees




c = Person("Armando", 32, "Male")
c.show_info()

