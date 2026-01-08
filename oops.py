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
class BankAccount:
    __balance = 500
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
    def withdraw(self,amount):
        if self.__balance>amount>0 :
            self.__balance-=amount
    def showBalance(self):
        return self.__balance
    
acc = BankAccount()
acc.withdraw(100)
print(acc.showBalance())
acc.__balance = 2000
print(acc.showBalance())