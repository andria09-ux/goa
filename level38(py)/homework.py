def AddToDatabase(name, surname, age):
    db = {
        "name" : name,
        "surname" : surname,
        "age" : age
    }
    return db
print(AddToDatabase("davit", "grdxelishvili", 20))