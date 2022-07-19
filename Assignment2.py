# Q1 (1) : z = 53

# Q1 (2)a : Type = <class 'list'>
# Q1 (2)b : Type = <function func at 0x00000213979CEF70>

# Q2 (1) :
from sympy import fibonacci


def  fun():
    x=y=z=10
    return x,y,z
print (fun())

# Q2 (2)
def sum (x):
    def sum2(y):
        return x+y
    return sum2
print(sum(5)(12))

# Q3 (1) :
num = "16461" #input("Enter a number :  ")
r = ""
for i in num:
   r = i + r

if( num == r):
    print ('Your number is palindrome')
else:
    print ('Your number is not palindrome')

# Q3 (2)
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
list3 = []
for i in list1:
    if i % 2 != 0:
        list3.append(i)
for i in list2:
    if i % 2 == 0:
        list3.append(i)
print(list3) 

# Q3 (3)
def Exponent(base, exponent):
    #return base ** exponent
    return pow(base, exponent)
print(Exponent(3,3))

# Q3 (4)
num = int(input("please enter the number to get its multiplication table :  "))
for i in range(1, 13):
    r = num*i
    print(f"{num} * {i} = {r}" )

# Q3 (5)
l = [1, 2, 3, 4, 5]
l.reverse()
print (l)

# Q3 (6)
num = 3 #int(input("please enter a number :  "))
if (num < 1 or num == 1):
    print("Your number is not a prime number")
else:
    for i in range(2, num):
        if (num % i == 0):
            print("Your number is not a prome number!")
        else:
            print("Your nummber is a prime number!")

# Q3 (7)
for i in range(1, 51):
    if (i % 3 == 0 and i % 5 != 0):
        print ('Fizz')
    elif (i % 5 == 0 and i % 3 !=0):
        print ('Buzz')
    elif (i % 3 == 0 and i % 5 == 0):
        print ('FizzBuzz') 
    else:
        print(i)

# Q3 (8):
x = ('omnia', 'omnia', 'Omnia')
res = all(x)
if (res):
    print("The tuples' items are the same")
else:
    print("the tuples' items are not the same")
#-------------------------------------------------
# Fibonacci sequence:
def Fibonacci(x):
    listt=[0, 1]
    for i in range(2, x+1):
        res = listt[-1] + listt[-2]
        listt.append(res)
    return listt
fib = Fibonacci(10)
print(fib)
