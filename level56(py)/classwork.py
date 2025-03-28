def nugzar_chubinidze(sadgerdzelo, limit):
    if sadgerdzelo > limit:
        return "ლუიზა: ნუგზარი აღარ დალიო მეტი!"
    else:
        return "ახლა მართლა, დამილოცნიე!"
    
'''
შევქმნათ ფუნქცია yuri_gagarini()
იური გაგარინის წნევა აღწვევდა 120-გულის წნევას პულსი 80-ს თქვენი დავალეება რომ შექმნათ ფუქნცია რომელიც 
მომახარებელს user -ს შეეკითხება თუ რამდენი აქვს გულის წნევა და პუსლი თუ დაემთხვევა პულსი იურინი გაგარინს პულს მაშინ Ture გამოიტანოს წინააღმდეგ შემთხვევაში Falase
'''
def yuri_gagarini():
    heart_rate = int(input("enter heart rate:"))
    puls_rate = int(input("enter puls rate:"))
    if (heart_rate == 120 and puls_rate == 80):
        return True
    else:
        return False

def captianjack(coins):
    if coins == 0:
        return "ajanyda"
    elif coins == 150:
        return ""


apples = ["green", "green", "red"]

# return set(apples)

def solve(s):
    upper_count = 0
    lower_count = 0
    
    for char in s:
        if char.isupper():
            upper_count += 1
        else:
            lower_count += 1
    
    if upper_count == lower_count:
        return s.lower()
    
    if lower_count > upper_count:
        return s.lower()
    else:
        return s.lower()