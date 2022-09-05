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


class Manager(Person):
    def __init__(self, name, age, gender, position):
        super().__init__(name, age, gender)
        self.position = position

















c = Person("Armando", 32, "Male")
c.show_info()

