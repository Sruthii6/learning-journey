
def factorial(n):
    if n == 0:
        return 1
    else:

        return n * factorial(n - 1)
def main():
    print(" 0! = ", factorial(0))
    print(" 1! = ", factorial(1))
    print(" 6! = ", factorial(6))
    print("10! = ", factorial(10))
main()


















from math import sqrt

print(type(sqrt))







# function as parameter

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def evaluate(f, x, y):
    return f(x, y)

def main():
    print(add(2, 3))
    print(multiply(2, 3))
    print(evaluate(add, 2, 3))
    print(evaluate(multiply, 2, 3))
    
main() 






from math import sqrt

def evaluate(f, x, y):
    return f(x, y)


print(evaluate(lambda x, y: 3*x + y, 10, 2))


print("the multiply value is:",evaluate(lambda x,y: x * y, 2,3))
print("the add value is:",evaluate(lambda x,y:x+y,2,3))

print(evaluate(lambda x, y: max(x, y) + x - sqrt(y), 20, 9))


        



def evaluate(f, x, y):
    return f(x, y)



def main():
    a = int(input('Enter an integer:'))
    print(evaluate(lambda x, y: True if x == a else False, 2, 3))
main()










# closure property



def make_adder():
    loc_val = 2 # Local variable definition
    return lambda x: x + loc_val # Returns a function

def main():
    f = make_adder()
    print(f(10))
    print(f(2))

main()
"""



"""
def print_msg(msg):

    def printer():
        print(msg)

    printer()
    
print_msg("hello")





def print_msg(msg):

    def printer():
        print(msg)

    return printer
    
f = print_msg("hello world")

f()


print(f.__closure__)
print(f.__closure__[0].cell_contents)

















































































