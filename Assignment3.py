# Omnia Mahmoud
import string 
import random

Letters = list(string.ascii_letters)
Digits = list(string.digits)
Chars = list(string.punctuation)
characters = list (string.ascii_letters + string.digits + string.punctuation)
# characters list is used if the user entered number of chracters that is less than the defined password length 
print("Let's generate your password :)") 

def PasswordGenerator():
    # force the user to a fixed length
    passwordLength = 10
    flag = True
    
    while flag:
        # askin the user for the options the he want.
        lettersCount = int(input("Enter the number of letters you want in your password : "))
        digitsCount = int(input("Enter the number of digits you want in your password : "))
        charCount = int(input("Enter the number of spicial characters you want in your password : "))
        totalCount = lettersCount + digitsCount +charCount
        if totalCount < passwordLength or totalCount == passwordLength:
            flag = False
        else:
            print("The total must be 10 characters ... ")
            flag = True
            
    Password = []
    for i in range(round(lettersCount)):
        Password.append(random.choice(Letters))
        # random.choice instead of shuffling the lists.
    for i in range(round(digitsCount)):
        Password.append(random.choice(Digits))
    
    for i in range(round(charCount)):
        Password.append(random.choice(Chars))

    if totalCount < passwordLength:
        for i in range(passwordLength - totalCount):
            Password.append(random.choice(characters)) # characters list

    Password = "".join(Password[0:])

    print(f"Your password is : \n  {Password}")

PasswordGenerator()
