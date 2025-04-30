
def gen():
    yield 3
    yield 'wow'
    yield -1
    yield 1.2

x = gen()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
#print(next(x))
"""















"""

for i in gen():
   print(i)    
"""









"""
def generate_multiples(m, n):
    count = 0
    while count < n:
        yield m * count
        count += 1

def main():
    for mult in generate_multiples(3, 6):
        print(mult, end=' ')
        print()
        
if __name__ == '__main__':
    main()

"""







"""
import wordcount

print("from imported module")
print(wordcount.linecount('wordcount.py'))

print(wordcount.__name__)










#from random import randrange
def max(x, y):
    call_string = "max({}, {})".format(x, y)
    print(">>> Calling " + call_string)
    result = x if x > y else y
    print("<<< Returning {} from ".format(result) + call_string)
    return result

def gcd(m, n):
    call_string = "gcd({}, {})".format(m, n)
    print(">>> Calling " + call_string)
    if n == 0:
        result = m
    else:
        result = gcd(n, m % n)
        print("<<< Returning {} from ".format(result) + call_string)
    return result

max(20, 30)
print('------------------------')

gcd(20,30)
print('------------------------')



from random import randrange

# decorator function
def show_call_and_return_details(f):
    func_name = f.__name__ # Get the function's name
    
    def execute_augmented(x, y):
        call_string = "{}({}, {})".format(func_name, x, y)
        print(">>> Calling " + call_string)
        result = f(x, y)
        print("<<< Returning {} from ".format(result) + call_string)
        return result
    return execute_augmented


def max(x, y):
    return x if x > y else y

def gcd(m, n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)



augmented_max = show_call_and_return_details(max)

gcd = show_call_and_return_details(gcd)

augmented_max(20, 30)
print('------------------------')
max(20,30)

gcd(20, 30)
print('------------------------')










