'''for i in range(0,6):
    if i==3:
        continue
    else:
        print(i)

str='hello'
x=''
for char in str:
    x=ord(char)
    print(char,x)

li=[]
while True:
    line=input('Enter a line:')
    if line=='':
        break
    li.append(line.lower())
for l in li:
    print(l)


l,u,d,s=0,0,0,0
str=input()
if len(str)>5 and len(str)<17:
    for i in str:
        if i.islower():
            l=l+1
        if i.isupper():
            u=u+1
        if i.isdigit():
            d=d+1
        if i=='$' or i=='#' or i=='@':
            s=s+1
    if l>0 and u>0 and s>0 and d>0:
        print('Valid password')
    else:
        print('invalid password')
else:
    print('password should be greater than 5 and less than 17 characters')

str='Python'
c='l'
x=0
for i in range(0,len(str)):
    if str[i]==c:
        x=x+i
        print(x)
        break
if x==0:
    print('character not in str')

str=input()
swap1=str.replace(',','@')
print('Swap1:',swap1)
swap2=swap1.replace('.',',')
print('Swap2:',swap2)
finalswap=swap2.replace('@','.')
print('finalswap:',finalswap)

str=input()
final=str.replace(' ','')
print(final)

class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def display(self):
        print(f'Brand:{self.brand}')
        print(f'Model:{self.model}')

class car(Vehicle):
    def __init__(self, brand, model,year):
        super().__init__(brand,model)
        self.year=year

    def display(self):
        super().display()
        print(f'Year:{self.year}')


obj=car('TATA','Nexon','2021')
obj.display()

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"brand: {self.brand}")
        print(f"Model: {self.model}")

class car(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model)
        self.year = year

    def display_info(self):
        super().display_info()
        print(f"Year: {self.year}")

class truck(Vehicle):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.capacity = capacity

    def display_info(self):
        super().display_info()
        print(f"Capacity: {self.capacity} tons")

class sports(car):
    def __init__(self, brand, model, year, speed):
        super().__init__(brand, model,year)
        self.speed = speed

    def display_info(self):
        super().display_info()
        print(f"Speed: {self.speed} kmph")


car = car("Tata", "nexon", 2023)
truck = truck("mahindra", "suv", 5)
sports = sports("BMW", "x7", 2022, 200)

car.display_info()
print()
truck.display_info()
print()
sports.display_info()


class MyClass:
    def my_method(self, *args):
        if len(args) == 1:
            if isinstance(args[0], int):
                print(f"Method with one integer argument: {args[0]}")
            elif isinstance(args[0], str):
                print(f"Method with one string argument: {args[0]}")
        else:
            print("Method with no arguments")


obj = MyClass()
obj.my_method()
obj.my_method(1)
obj.my_method("Hello")'''

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.num_doors}")

class Truck(Vehicle):
    def __init__(self, brand, model, max_load):
        super().__init__(brand, model)
        self.max_load = max_load
    def display_info(self):
        super().display_info()
        print(f"Maximum Load Capacity: {self.max_load}")

class HybridVehicle(Car, Truck):
    def __init__(self, brand, model, num_doors, max_load, fuel_type):
        Car.__init__(self, brand, model, num_doors)
        Truck.__init__(self, brand, model, max_load)
        self.fuel_type = fuel_type
    def display_info(self):
        super(Car, self).display_info()
        print(f"Fuel Type: {self.fuel_type}")

# Create instances of HybridVehicle
hybrid_vehicle = HybridVehicle("Toyota", "Prius", 4,
                               "500 kg", "Hybrid")
hybrid_vehicle.display_info()











