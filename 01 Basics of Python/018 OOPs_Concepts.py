# ============================================================
#                OBJECT ORIENTED PROGRAMMING (OOPs)
# ============================================================

# OOP is a programming paradigm based on "objects"
# Objects contain:
# - Data  → variables (attributes)
# - Code  → methods (functions)

# OOP helps in:
# 1. Code reusability
# 2. Better structure
# 3. Easy maintenance
# 4. Real-world modeling

# ============================================================
#               OOPs CONCEPTS SUMMARY TABLE
# ============================================================

# +--------------------+--------------------------------------+
# | Concept            | Description                          |
# +--------------------+--------------------------------------+
# | Class              | Blueprint of an object               |
# | Object             | Instance of a class                  |
# | Encapsulation      | Binding data & methods together      |
# | Inheritance        | Acquiring properties from parent     |
# | Polymorphism       | Same method, different behavior      |
# | Abstraction        | Hiding implementation details        |
# +--------------------+--------------------------------------+

# ============================================================
#               1. CLASS AND OBJECT
# ============================================================

# Class → blueprint
class Student:
    name = "Rahul"
    age = 21

# Object → instance of class
s1 = Student()

print(s1.name)
print(s1.age)

# ============================================================
#               2. __init__ METHOD (CONSTRUCTOR)
# ============================================================

# __init__ runs automatically when object is created

class Person:
    def __init__(self, name, age):
        self.name = name    # instance variable
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

p1 = Person("Aman", 22)
p1.display()

# ============================================================
#               3. INSTANCE & CLASS VARIABLES
# ============================================================

class Employee:
    company = "Google"   # class variable

    def __init__(self, name, salary):
        self.name = name       # instance variable
        self.salary = salary

e1 = Employee("Rahul", 50000)
e2 = Employee("Aman", 60000)

print(e1.company)
print(e2.company)

# ============================================================
#               4. ENCAPSULATION
# ============================================================

# Encapsulation = Wrapping data & methods together
# Achieved using access modifiers

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())

# ============================================================
#               5. INHERITANCE
# ============================================================

# Child class inherits parent class properties

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()
d.bark()

# ============================================================
#               TYPES OF INHERITANCE
# ============================================================

# Single Inheritance → A → B
# Multiple Inheritance → A, B → C
# Multilevel Inheritance → A → B → C
# Hierarchical Inheritance → A → B, C

# Example: Multilevel inheritance

class Vehicle:
    def move(self):
        print("Vehicle moves")

class Car(Vehicle):
    def wheels(self):
        print("Car has 4 wheels")

class ElectricCar(Car):
    def battery(self):
        print("Electric car has battery")

ec = ElectricCar()
ec.move()
ec.wheels()
ec.battery()

# ============================================================
#               6. POLYMORPHISM
# ============================================================

# Same method name, different behavior

class Bird:
    def fly(self):
        print("Bird can fly")

class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")

b = Bird()
p = Penguin()

b.fly()
p.fly()

# ============================================================
#               OPERATOR OVERLOADING (POLYMORPHISM)
# ============================================================

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

n1 = Number(10)
n2 = Number(20)

print(n1 + n2)

# ============================================================
#               7. ABSTRACTION
# ============================================================

# Abstraction hides implementation details
# Achieved using abc module

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

rect = Rectangle(5, 4)
print("Area:", rect.area())

# ============================================================
#               8. METHOD OVERRIDING
# ============================================================

class Parent:
    def show(self):
        print("This is parent method")

class Child(Parent):
    def show(self):
        print("This is child method")

c = Child()
c.show()

# ============================================================
#               9. SUPER() FUNCTION
# ============================================================

class Father:
    def __init__(self):
        print("Father constructor")

class Son(Father):
    def __init__(self):
        super().__init__()
        print("Son constructor")

s = Son()

# ============================================================
#               10. STATIC METHOD
# ============================================================

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(5, 10))

# ============================================================
#               REAL-LIFE EXAMPLES
# ============================================================

# ------------------------------------------------------------
# Example 1: Login system
# ------------------------------------------------------------

class User:
    def login(self):
        print("User login")

class Admin(User):
    def login(self):
        print("Admin login with extra privileges")

u = User()
a = Admin()

u.login()
a.login()

# ------------------------------------------------------------
# Example 2: Bank system
# ------------------------------------------------------------

class Bank:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

b = Bank(1000)
b.withdraw(300)

# ============================================================
#               COMMON MISTAKES
# ============================================================

# 1. Forgetting self keyword
# 2. Not calling super() in inheritance
# 3. Overusing inheritance instead of composition
# 4. Breaking encapsulation unnecessarily

# ============================================================
#               IMPORTANT POINTS
# ============================================================

# 1. Class is a blueprint, object is instance
# 2. Encapsulation improves security
# 3. Inheritance enables code reuse
# 4. Polymorphism provides flexibility
# 5. Abstraction hides complexity

# ============================================================
# End of File: 018 OOPs_Concepts.py
# ============================================================
