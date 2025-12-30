# def greet():
#     print("Hello Welcome")

# greet()
# greet()
# greet()
# greet()
# greet()
# greet()
# greet()
# greet()
# greet()

# def add(T,E,M,S,SS):
#     print(T+E+M+S+SS)


# add(E=55,T=77,M=88,SS=99,S=55)



def add(*args):
    total = 0
    for s in args:
        total+=s
    print(total)

add(77,99,55)


# lambda function
square = lambda x,y: x+y

print(square(5,6))