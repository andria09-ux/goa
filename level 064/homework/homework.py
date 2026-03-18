# 1
class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def car_info(self):
        return f"მანქანა: {self.brand} {self.model}, გამოშვების წელი: {self.year}"

# 2
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def is_passing(self):
        if self.grade > 5:
            return True
        else:
            return False
        
    def new(self):
        return f"student: {self.name}, age: {self.age}, grade: {self.grade}"

# 3
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark():
        return "woof!"

# 4
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(w, h):
        return w*h
    
    def calculate(self):
        return f"width: {self.width}, height: {self.height}"

# 5
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def info(self):
        return f"the title of the book is {self.title}. its author is {self.author}, and it was published in {self.year}"