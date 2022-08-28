class Curs:
    def __init__(self, nume_curs):
        self.nume_curs = nume_curs
        self.students=[]
        self.grupe=[]
    def __str__(self):
        result = "Curs:"+ self.nume_curs+'\n'+"Grupa:"
        for grupa in self.grupe:
            nume_grupa = grupa.get_numeGrupa()
            result = result + nume_grupa + '\n'
        for student in self.students:
            nume_student = student.get_numeStudent()
            prenume_student=student.get_prenumeStudent()
            result = result + "Student:"+ nume_student +" "+prenume_student + '\n'
        return result
    def addGrupa(self,nume_grupa):
        grupa=Grupe(nume_grupa)
        self.grupe.append(grupa)
    def addStudent(self, nume,prenume):
        student = Student(nume, prenume)
        self.students.append(student)
class Grupe:
    def __init__(self, nume_grupa):
            self.nume_grupa = nume_grupa
    def get_numeGrupa(self):
        return str(self.nume_grupa)
class Student:
    def __init__(self, nume, prenume):
        self.nume = nume
        self.prenume = prenume
    def get_numeStudent(self):
        return self.nume
    def get_prenumeStudent(self):
        return self.prenume


c=Curs("Matematica")
g=Grupe("A")
s=Student("Georgescu","Mihai")
c2 = Curs("Fizica")
g2 = Grupe("B")
s2 = Student("Odagiu", "Armando")
c.addGrupa(g.nume_grupa)
c.addStudent(s.nume,s.prenume)
c2.addGrupa(g2.nume_grupa)
c2.addStudent(s2.nume,s2.prenume)
print(c)
print(c2)