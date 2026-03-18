# def repeat_str(repeat, string):
#     return string * repeat

class MyCat:
    x = "cat"

p1 = MyCat()

print(p1.x)

class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        
    def __str__(slef):
        return f"{slef.name} {slef.surname} {slef.age}"
    
    def __me__(self):
        return f"me var {self.name}({self.surname}) da var {self.age}"

p1 = Human("davit","grdzelo",19)

print(p1)


class Person:
    pass