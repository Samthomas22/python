'''a=int(input())
if a%2==0:
    print('even')
else:
    print('odd')

a=int(input())
b=int(input())
if a>b:
    print('largest number:',a)
else:
    print('largest number:',b)


a=11
print(a)
print(type(a))

a='hello'
print(a)
print(type(a))

for i in range(1,11):
    if i%2==0:
        print('Even:',i)
    else:
        print('odd:',i)

prime numbers
swap 2 variable
check if no is positive or negative
if year is leap year
reverse a numbers
string is palindrome
display all even and do sum of all even
a=int(input())
for i in range(2,a):
    if a%i==0:
        print('no is not prime')
        break
    else:
        print('prime')
        break


a=input()
b=input()
a,b=b,a
print('A is:',a)
print('B is:',b)

a=int(input())
if a<0:
    print('negative')
else:
    print('positive')

a=int(input())
if a%4==0 and a%100!=0 or a%400==0:
    print('leap year')
else:
    print('not leap year')

a=int(input())
rev=0
while a!=0:
    rem=a%10
    rev=rev*10+rem
    a=a//10
print(rev)

a=input()
x=a[::-1]
if x==a:
    print('palindrome')
else:
    print('not palindrome')

a=input()
x=''
for i in a:
    x=i+x
if x==a:
    print('palindrome')
else:
    print('not palindrome')

i=int(input())
x=0
for y in range(1,i):
    if y%2==0:
        x=x+y
print('SUM:',x)

from datetime import datetime
def sum():
    x=int(input('Enter a no:'))
    y=int(input('Enter a no:'))
    result=x+y
    print(result)
sum()


currentdate=datetime.now()
print(currentdate)

formatdate=currentdate.strftime("%d-%b-%Y")
print(formatdate)


li=[]
for i in range(1,11):
    li.append(i)
print(li)

li.append(11)
print(li)

tuple=(1,1,'hello')
print(tuple)
tuple=tuple+(2,'welcome')
print(tuple)

d1={'fruit':'mango'}
print(dict)
d1['veg']='potato'
print(d1)
print(len(d1))

d1['fruit']='Mango'
print(d1)
print(len(d1))

if(d1.get('fruits')==None):
    d1['fruits']='Grapes'
print(d1)
print(len(d1))

x=int(input())
y=int(input())
z=int(input())
def max():
    if x>y and y>z:
        print('max is:',x)
    elif y>x and y>z:
        print('max is:',y)
    else:
        print('max is:',z)
max()


li=[]
x=0
y=1
for i in range(1,6):
    li.append(i)
for i in li:
    x=x+i
    y=y*i
print(x)
print(y)

x=int(input())
def fact():
    y=1
    for i in range(1,x+1):
        y=y*i
    print(y)
fact()

x=int(input())
def inrange():
        if x in range(1,10):
            print(x,' is in given range')
        else:
            print('out of range')
inrange()

dict={'Uppercase':0,'lowercase':0}
x=input()
def count():
    for c in x:
        if c.isupper():
            dict['Uppercase']=dict['Uppercase']+1
        if c.islower():
            dict['lowercase']=dict['lowercase']+1
    y=dict['Uppercase']
    z=dict['lowercase']
    print(y,z)
count()

li=[1,2,2,3,3,3,4,4,5]
x=[]
def distinct():
      for i in li:
          if i not in x:
              x.append(i)
      print(x)
distinct()

a=input()
def reverse():
      x=''
      for i in a:
          x=i+x
      print(x)
reverse()

def perfect(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum = sum+x
    if sum==n:
        print('Perfect no')
    else:
        print('not perfect no')
perfect(8)

def pangram(str):
   alphabet = "abcdefghijklmnopqrstuvwxyz"
   for c in alphabet:
      if c not in str.lower():
         print('not pangram')
   print('pangram')

str='The quick brown fox jumps over the lazy dog'
pangram(str)

str=input()
x=str.split('-')
x.sort()
print('-'.join(x))

li=[]
def squares():
   for i in range(1,31):
      li.append(i*i)
   print(li)
squares()

str1 = """
a = 3
b = 6
c = a + b
print(c)
"""
exec(str1)

def func1():
   a=5
   def func2():
      b=5
      c=a+b
      print(c)
   return func2()
func1()

def func():
    a = 1
    str = 'hello'
print(func.__code__.co_nlocals)

def pascal_triangle(n):
   row = [1]
   col = [0]
   y=row+col
   print(y)
   for x in range(max(n,0)):
      print(row)
      row=[l+r for l,r in zip(row+col, col+row)]
   return n>=1
pascal_triangle(6)

def solve(n):
   for i in range(n+1):
      C = 1
      for j in range(1, i+1):
         print(C, end='')
         C = C * (i - j) // j
      print()

n = 5
solve(n)

import time
def delay():
   time.sleep(10)
   print('hello')
delay()

def make_bold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def make_italic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

def make_underline(fn):
    def wrapped():
        return "<u>" + fn() + "</u>"
    return wrapped
@make_bold
@make_italic
@make_underline
def hello():
    return "hello world"
print(hello())

class Demo:
    a=20
    def show(self):
        print(self.a)
        b=22
        print(b)

    def show1(self):
        c = 22
        print(c)
#Demo().show()
d=Demo()
d.show()
d.show1()

class Student:
    def studentname(self,name):
        self.name=name
        print(name)
    def studentmarks(self,marks):
        self.marks=marks
        print(marks)

s1=Student()
s1.studentmarks(80)
s1.studentname("John")

#Encapsulation
class Laptop:
    def mouse(self):
        print("this is mouse")
    def keyboard(self):
        print("this is keyboard")
    def camera(self):
         print("this is camera")
l=Laptop()
l.mouse()
l.keyboard()
l.camera()

Access Specfiers
Default:public
protected:_
private:__

class Operation:
    def __init__(self):
        self.a=80
        self.b=90
        self._c=10
        self._d=20
        self.__e=11
        self.__f=12
    def add(self):
        total=self.a+self.b
        print(total)

    def add_Pro(self):
        total=self._c+self._d
        print(total)

    def add_pp(self):
         total=self.__e+self.__f
         print(total)
class output:
    o=Operation()
    def __sum_pp(self):
        return self.o.add_pp()
    def total(self):
        return self.__sum_pp()

o1=output()
o1.total()


# define parent class Company
class Company:
    # constructor
    def __init__(self, name, proj):
        self.name = name  # name(name of company) is public
        self._proj = proj  # proj(current project) is protected

    # public function to show the details
    def show(self):
        print("The code of the company is = ", self.ccode)


# define child class Emp
class Emp(Company):
    # constructor
    def __init__(self, eName, sal, cName, proj):
        # calling parent class constructor
        Company.__init__(self, cName, proj)
        self.name = eName  # public member variable
        self.__sal = sal  # private member variable

    # public function to show salary details
    def show_sal(self):
        print("The salary of ", self.name, " is ", self.__sal, )


# creating instance of Company class
c = Company("Stark Industries", "Mark 4")
# creating instance of Employee class
e = Emp("Steve", 9999999, c.name, c._proj)

print("Welcome to ", c.name)
print("Here ", e.name, " is working on ", e._proj)

# only the instance itself can change the __sal variable
# and to show the value we have created a public function show_sal()
e.show_sal()


from abc import ABC, abstractmethod
class A:
    @abstractmethod
    def test(self):
        pass

    @abstractmethod
    def test1(self):
        pass
class B(A):
    def test(self):
        print("test")

    def test1(self):
        print("test1")

    def test2(self):
        print("test2")
O=B()
O.test()
O.test1()
O.test2()


def smart_div(func):
    def inner(self,a,b):
        print(a,"and",b)
        if(b==0):
            print("division not possible")
            quit()
        return func(self,a,b)
    return inner


class division:
    @smart_div
    def div(self,a,b):
        output=a/b
        return output

d=division()
print(d.div(56,0))

class Person:
    def __init__(self, name, age):
        self._name = name  # Protected attribute
        self._age = age    # Protected attribute

    # Getter method
    def get_name(self):
        return self._name

    # Setter method
    def set_age(self, age):
        if age >= 0:
            self._age = age
        else:
            print("Age cannot be negative.")

    # Property for age
    @property
    def age(self):
        return self._age

    # Property setter for age
    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            print("Age cannot be negative.")

# Creating an instance of the Person class
person = Person("Alice", 30)
# Accessing attributes using getter methods
print(person.get_name())
print(person.age)

# Modifying age using setter methods
person.set_age(35)
print(person.age)

# Using properties to get and set age
person.age = 25
print(person.age)


class MyClass:
    def __init__(self):
        self._my_variable = 10  # Protected attribute
        self.__private_var = 20  # Private attribute

    # Getter method for the protected attribute
    def get_my_variable(self):
        return self._my_variable

    # Setter method for the protected attribute
    def set_my_variable(self, value):
        if value > 0:
            self._my_variable = value
        else:
            print("Value must be greater than 0.")

    # Getter method for the private attribute
    def get_private_var(self):
        return self.__private_var

    # Setter method for the private attribute
    def set_private_var(self, value):
        self.__private_var = value

# Create an instance of MyClass
obj = MyClass()

# Access and modify the protected attribute using getter and setter methods
print('Initial value of protected variable:',obj.get_my_variable())  # Access
obj.set_my_variable(15)  # Modify
print('Value after modification:',obj.get_my_variable())  # Access

# Access and modify the private attribute using getter and setter methods
print('Initial value of private variable:',obj.get_private_var())  # Access
obj.set_private_var(30)  # Modify
print('Value after modification:',obj.get_private_var())  # Access

'''

def div(func):
    def inner(a,b):
        print('Enter values are', a, 'and', b)
        if b==0:
            print('cannot divide by 0')
            quit()
        return func(a,b)
    return inner


@div
def divide(a,b):
    return a/b
print(divide(5,2))