from cmath import pi
import string 
import random
#Q1: Answer the following Questions.
'''
1-What are lists and tuples? What is the key difference between
the two? 
lists: are used to store multiple data in a single variable.
tuples: are also used to store multiple data in a single variable.
The key difference between them is the mutability.
Tuples are immutable datatype which means objects of this datatype(Tuples) do not allow 
any changes in it. On the other hand, lists are mutable and it's objects allow changes. 
'''
'''
2-What is break, continue and pass in Python? 
Break: is a keyword used to end the current iteration and 
exit the loop or the function it is written in.

Continue: is a keyword used to end the current iteration and proceed with the next one.

Pass: is a place-keeper keyword which means it will be implemented later. Also, 
the Pass word in python is a null statement 
'''
'''
3-What is the use of self in Python? 
the self is used to represent this object of a predefined class,
by which the attributes and methods of this class can be accessed
'''
'''
4-What is docstring in Python? 
Docstring is a multiline comment in the first line of a function, class or method
that is used as documentation and description of any python function, class or method.
'''
'''
5-Python supports multiple inheritance . explain it with example
Any class can be derived from more than one class.
Ex:
class Animal:
    def Eat(self):
        print ("Any animal has to eat")
class Dog():
    def Bark(self):
        print("Any doc can bark.")
class puppets(Animal,Dog):
    pass    
'''
#Q2:
'''
1- False.
2- False.
3- True.
4- False.
5- False
'''
#Q3:
'''
1-Create a function that takes a string and returns the number
(count) of vowels contained within it.
Example:
count_vowels("Celebration") ➞ 5 
'''
def count_vowels(word):
    lword = word.lower()
    count = 0
    vowel = ['a','e','i','o','u']
    for i in lword:
        for j in vowel:
            if i == j:
                count += 1
            else:
                continue
    print(f"{word} contains {count} vowels.")
count_vowels("Omnia")
'''
2-Write a function that finds the sum of the first n natural
numbers. Make your function recursive.
Example:
sum_numbers(5) ➞ 15
# 1 + 2 + 3 + 4 + 5 = 15 
'''
def sum_numbers(num):
    sum = 0
    if num == 0:
        return sum
    else:
        sum = num + sum_numbers(num-1) 
        return  sum
        
print(sum_numbers(5))

'''
3- Display Fibonacci series up to 10 terms
Expected output :
Fibonacci sequence:
0 1 1 2 3 5 8 13 21 34 
'''
def Fibonacci(x):
    listt=[0, 1]
    for i in range(2, x):
        res = listt[-1] + listt[-2]
        listt.append(res)
    return listt
fib = Fibonacci(10)
print(fib)

'''
4- Write a Python program to check if value 200 exists in the
following dictionary.
Given:
sample_dict = {'a': 100, 'b': 200, 'c': 300}
Expected output:
200 present in a dict
'''
sample_dict = {'a': 100, 'b': 200, 'c': 300}
x = 200
if x in sample_dict.values():
    print("200 is in the dectionary")
else:
    print("unfortunately, 200 is not in the dictionary") 

'''
5- classes
'''
class circle:
    def __init__(self, raduis, color):
        self.raduis = raduis
        self.color = color
    def getrad(self):
        return self.raduis
    def setrad(self, raduis):
        self.raduis = raduis
    def getcolor(self):
        return self.color
    def setcolor(self, color):
        self.color = color
    def getArea(self):
        return pow(self.raduis,2) * pi
    def displaycircule(self):
        print(f"Raduis is = {self.raduis} \nThe color is {self.getcolor()} ")

class clyinder(circle):
    def __init__(self, raduis, color, hight):
        super().__init__(raduis, color) 
        self.hight = hight
    def gethight(self):
        return self.hight
    def sethight(self, hight):
        self.hight = hight
    def getvolum(self):
        return self.getArea()*self.hight
#Q4:
'''
1- Generate Random Password Containing [40% uppercase 30%
lowercase and 30% numbers ] 
'''
upperletters = list(string.ascii_uppercase)
lowerletters = list(string.ascii_lowercase)
digits = list(string.digits)
print(" Generate your password ") 

def generatePassword():
    passwordLength = input('Enter password length: ')
    while True:
        try:
            passwordLength = int(passwordLength)
            if passwordLength < 8 :
                print("Password length must be at least 8 chars")
                passwordLength = int(input('Enter password length : '))
            break
        except:
            print('Please enter only numbers.!')
            passwordLength = int(input('Enter password length: '))
            
    password = []
    for i in range(round(passwordLength * .4)):
        password.append(random.choice(upperletters))
    for i in range(round(passwordLength * .3)):
        password.append(random.choice(lowerletters))
    for i in range(round(passwordLength * .3)):
        password.append(random.choice(digits))

    password = "".join(password[0:])

    print(f"Your password is : \n  {password}")

generatePassword()
''' 
2-  
'''
#Q5
'''
1- Default constructor vs parameterized constructor
    Default Constructor:
    def __init__(self) -> None:
        pass
    Parameterized Constructor
    def __init__(self, name):
        self.name = name

2- Class vs object
class person:
    pass 

person1 = person()

'''