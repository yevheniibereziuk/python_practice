def print_privet(name):
    """Print privetstvie"""
    print("Congratulations," + name +  " wish you all the best")
    print("Hello, wish you good luck")


def summa(x, y):
    # print(x+y)
    
    return x+y


def factorial(x):
    """Calculate Factorial of number X"""
    otvet = 1
    for i in range(1, x + 1):
        otvet = otvet * i
    return otvet

#----------------------
print("----------------------")
print_privet("Yevhenii")
print_privet("Ostap")

# summa(10, 30)
x = summa(33, 22)
print(x)

# 2! = 1 * 2
# 3! = 1 * 2 * 3
# 4! = 1 * 2 * 3 * 4

for i in range(1, 10 + 1):
    print(str(i) + "!\t = " + str(factorial(i)))
# print(factorial(1))
# print(factorial(5))

