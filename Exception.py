try:
    num = int(input("Enter the Number:"))
    print(10/num)
except(ValueError):
    print("Please enter value only in number")
except(ZeroDivisionError):
    print("The enter above Zero")