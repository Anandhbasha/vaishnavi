# # car1Milage = 18
# # noofWheels = 4
# # airbags = 6
# # mirror = 2
# # varient = "diesel"
# # carName = "swift"

# # def acc():
# #     print(carName,"Moves")

# # def brake():
# #     print(carName,"stops")


# class cars:
#     car1Milage = 18
#     noofWheels = 4
#     airbags = 6
#     mirror = 2
#     varient = "diesel"
#     carName = "swift"

#     def acc(self):
#         print(self.carName,"Moves")

#     def brake(self):
#         print(self.carName,"stops")


# c1= cars()
# c1.carName = "dzire"
# c1.car1Milage = 22

# print(c1.car1Milage)
# c1.acc()

# c2 = cars()  #instence object create 
# c2.carName = "ALTO"
# c2.car1Milage = 21
# print(c2.car1Milage)
# c2.brake()


# private Variable
# __name 
# protected 
# _name

# encapsulation
# class BankAccount:
#     __balance = 500
#     def deposit(self,amount):
#         if amount>0:
#             self.__balance+=amount
#     def withdraw(self,amount):
#         if self.__balance>amount>0 :
#             self.__balance-=amount
#     def showBalance(self):
#         return self.__balance
    
# acc = BankAccount()
# acc.withdraw(100)
# print(acc.showBalance())
# acc.__balance = 2000
# print(acc.showBalance())

# # inhertence
# class Parent:
#     def relationship(self):
#         print("He is my Dad")
# class Son(Parent):
#     pass

# s= Son()
# s.relationship()
# Constructor and super class
# class Person:
#     def __init__(self,name):
#         self.name = name
#     def show(self):
#         print("Name:", self.name)
# class Student(Person):
#     def __init__(self, name,course):
#         super().__init__(name)
#         self.course = course
#     def details(self):
#         print(self.name,self.course)

# s= Student("Arun","Python")
# s.show()
# s.details()


# multiple
# class Dad:
#     def prints(self):
#         print("He is Dad")

# class Mom:
#     def printMom(self):
#         print("He is Mom")
# class Son(Dad,Mom):
#     pass

# S = Son()
# S.printMom()
# S.prints()

# multilevel
class GrandPa:
    def land(self):
        print("Grandpa's Land")
class Dad(GrandPa):
    def house(self):
        print("Father's house")
class Son(Dad):
    def Bike(self):
        print("Son's Bike")

S = Son()
S.Bike()
S.house()
S.land()


# Hierarchical
class Vehicle:
    def fuel(self):
        print("use Fuel")
class car(Vehicle):
    pass
class Bike(Vehicle):
    pass

C= car()
C.fuel()
B= Bike()
B.fuel()