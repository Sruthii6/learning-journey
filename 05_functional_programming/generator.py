
def my_gen():
    n = 1
    print("this is the fisrt value printed")

    yield n

    n+=1
    print("second value")
    yield n


    n+=1
    print("second value")
    yield n

a = my_gen()

print(next(a))

print(next(a))

print(next(a))

#print(next(a))

for item in my_gen():
    print(item)
    
def rev_str(mystring):
    length = len(mystring)
    for i in range(length-1, -1, -1):
        yield mystring[i]
        
for char in rev_str("hi iam here"):
    print(char)




















my_list = [1,2,3,4]

# list comprehension
a = [x**2 for x in my_list]

print(a)

# generator expressions
b = (x**2 for x in my_list)

#print(b)

print(next(b))

print(next(b))
print(next(b))
print(next(b))
#next(b)

# within functions

res = sum(x**2 for x in my_list)
print("the sum is")
print(res)




# powtwo as generator

def PowTwo(max =0):
    n = 0
    while n < max:
        yield 2 ** n
        n +=1

print("the generator exp powtwo")
for i in PowTwo(6):
    print(i)







        
    


















        
