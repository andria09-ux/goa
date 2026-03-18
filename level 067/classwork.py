class Person:
    def __init__(self, name, surname, dadname):
        self.name = name
        self.surname = surname
        self.dadname = dadname


    def __str__(self):
        return f"Name: {self.name},Surname: {self.surname} ,Father's name: {self.dadname}"
    

h1 = Person("davit", "grdzelishvili", "giorgadze")


print(h1)

