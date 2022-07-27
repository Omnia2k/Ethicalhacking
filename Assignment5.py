from cmath import pi

'''1.1'''
class circle:
    def __init__(self, raduis):
        self.raduis = raduis
    def getrad(self):
        return self.raduis
    def setrad(self, raduis):
        self.raduis = raduis
    def circleArea(self):
        return pow(self.raduis,2) * pi
    def circleCircumference(self):
        return 2 * pi * self.raduis
    def displaycircule(self):
        print(f"Raduis is = {self.raduis} \nThe Area is = {self.circleArea()} \nThe circumference is = {self.circleCircumference()}") 

circle1= circle(5)
circle1.displaycircule()    

#----------------------
'''1.3'''

class Rectangle :
    def __init__(self, len, wid):
        self.len = len
        self.wid = wid
    def getlength(self):
        return self.len
    def setlength(self, len):
        self.len = len
    def getwidth(self):
        return self.wid
    def setwidth(self, wid):
        self.wid = wid
    def getArea(self):
        return self.len * self.wid
    def getPerimeter(self):
        return 2 * ( self.len + self.wid )
    def display(self):
        print(f"The length = {self.len} , and the width = {self.wid}\nThe Area = {self.getArea()}\nThe Perimeter = {self.getPerimeter()}")

R1 = Rectangle(8,6)
R1.display()

'''1.4'''
class Employee:
    def __init__(self, id, fname, lname, salary):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.salary = salary
    def getid(self):
        return self.id
    def getfname(self):
        return self.fname
    def getlname(self):
        return self.lname
    def getsalary(self):
        return self.salary
    def setid(self, id):
        self.id = id
    def setfname(self, fname):
        self.fname = fname
    def setlname(self, lname):
        self.lname= lname
    def setsalary(self, salary):
        self.salary = salary
    def getAnnualSalary(self):
        return self.salary * 12
    def raiseSalary(self, percent):
        return (self.salary * percent) + self.salary
    def DisplayEmp(self):
        print(f"Information of employee {self.fname} {self.lname}")
        print(f"ID: {self.id}\nSalary: {self.salary}\nHis Annual Salary: {self.getAnnualSalary()}")
E1 = Employee(206450, 'Omnia', 'Mahmoud', 100000)
E1.DisplayEmp()

'''1.6'''
class Account:
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name
        self.balance = balance
    def getid(self):
        return self.id
    def getname(self):
        return self.name
    def getbalance(self):
        return self.balance
    def cridet(self, amount):
        self.balance += amount
        return self.balance
    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("successful process")
        else:
            print("Amount exceeded the balance")
    def transferTo(self, otheraccount, amount):
        if amount <= self.balance:
            self.balance -= amount
            otheraccount.balance += amount
            #print(otheraccount.balance) #just to make sure it works
            print("successful process")
        else:
            print("Amount exceeded the balance")
    def display(self):
        print(f"Account[id: {self.id}, Name: {self.name}, Balance = {self.balance}")

a1 = Account("206450", "Omnia", 200000)
a2 = Account("264525", "Ayman", 102020)
a1.transferTo(a2, 100)