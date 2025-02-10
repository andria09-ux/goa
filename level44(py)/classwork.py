def count_by(x, n):
    arr = []
    for i in range(1, n+1):
        arr.append(i*x)
    return arr


def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - son_years_old * 2)



def greet(language):
    arr=[ 
    ("english", "Welcome")
 , ("czech", "Vitejte")
 , ("danish", "Velkomst")
 , ("dutch", "Welkom")
 , ("estonian", "Tere tulemast")
 , ("finnish", "Tervetuloa")
 , ("flemish", "Welgekomen")
 , ("french", "Bienvenue")
 , ("german", "Willkommen")
 , ("irish", "Failte")
 , ("italian", "Benvenuto")
 , ("latvian", "Gaidits")
 , ("lithuanian", "Laukiamas")
 , ("polish", "Witamy")
 , ("spanish", "Bienvenido")
 , ("swedish", "Valkommen")
 , ("welsh", "Croeso")
 ]
    for i in range(len(arr)):
        if arr[i][0] == language:
            return arr[i][1]
    return "Welcome"