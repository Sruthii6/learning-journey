
fruits = ['apple', 'mango', 'strawbeerry']
numbers = [42, 123,657]
lt = []
print(fruits)

print(lt)

numbers[1] = 190

print(numbers)

print('mango' in fruits)
print('banana' in fruits)

for fruit in fruits:
    print(fruit)



for x in []:
    print("nothing")


a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)


list1 = [1,2,3] * 2
print(list1)

fruits = ['apple', 'mango', 'strawbeerry']
print(fruits[1:2])
print(fruits[:2])
print(fruits[1:])
print(fruits[:])

numbers = [42, 123,657]
numbers[1:2] = [1,2]
print(numbers)




t = ['a','b','c','d','e']

t.append('f')

print(t)

t1 = ['x','y','z']

t1.extend(t)

print(t1)

t1.sort()
print(t1)

"""





"""
def add_all(lt):
    total = 0
    for x in lt:
        total += x # augmented assignment statement
    return total   # accumulates the sum of values

lt = [1,2,3,4,5]
summation = add_all(lt)

print(summation)

print(sum(lt))

"""

"""







# map
alphabets = ['s','m','w','a']
def capitalize_all(s):
    res = []
    for s in alphabets:
        res.append(s.capitalize())
    return res

mod_alpha = capitalize_all(alphabets)
print(mod_alpha)











#filter

alpha = ['a','A','M','m']
def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res



new_list = only_upper(alpha)

print(new_list)



# list2

numbers = [42,123,657,50,78,96]
#print(numbers[-1])
#print(numbers[-2])
#print(numbers[-4])

numbers.insert(1,67)
numbers.insert(3,11)
print("after insert",numbers)


# deleting elements

# deleting element by value
numbers.remove(123)
print("after remove",numbers)

# returning the deleted value by index
t = numbers.pop()
print("popped element",t)

print(" second element popped",numbers.pop(2))

# deleting element by index without returning value
print(" elements of list before delete",numbers)
del numbers[1]
print(" elements of list after delete",numbers)

del numbers[1:3]
print("deleting the slice of list",numbers)










numbers+= [2] # eqt to extend -works for integer, list and strings
number_lt = numbers + [190]
print("the new list",number_lt)



















    
