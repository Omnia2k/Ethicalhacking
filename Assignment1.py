#problem 1 
print('Check your grade')
grade = int(input("Enter your grade in this course: \n"))
if grade >85 or grade == 85:
    print ('Excellent')
elif grade < 85 and grade > 75:
    print ('Very good')
elif grade < 75 and grade > 65:
    print ('Good')
elif grade < 65 and grade > 50:
    print ('Pass')
else: 
    print ('Fail')
##############################################
#problem 2

print('Play FIZZBUZZ game (:')
num = int(input('Enter the number you want: \n'))
if num % 3 == 0 and num % 5 != 0:
    print ('Fizz')
elif num % 5 == 0 and num % 3 !=0:
    print ('Buzz')
elif num % 3 == 0 and num % 5 == 0:
    print ('FizzBuzz') 
else:
    print('Try again')

############################################
#problem 3 even or odd

num = int(input('Enter the number you want: \n'))
if num == 0:
    print ('Zero is not even or odd number')
else:
    if num % 2 == 0:
        print (num,' is Even')
    else:
        print (num,' is Odd')

##########################################
#problem 4

word = input("Enter a word :  ")
r = ""
for i in word:
   r = i + r

if( word == r):
    print ('Your string is palindrome')
else:
    print ('Your string is not palindrome')
###########################################
#problem 5

len = int(input("Enter the Length : "))
wid = int(input("Enter the Width : "))
area = len * wid
perimeter = 2 * (len+wid)
print("The area of Rectangle : ",area)
print("The perimeter of Rectangle : ",perimeter)


