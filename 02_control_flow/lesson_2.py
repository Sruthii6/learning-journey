




x =5

if x==5:
    y=x
print(y)


















if x<=5: y = x

print(y)











x=4


if 0 < x < 10:
    print('x is a positive single-digit number.')





 
#pass example
if x < 0:
    pass 
else:
    print("the pass example",x)

if x >= 0:
    print(x)









# floating point equality

d1 = 1.11 - 1.10
d2 = 2.11 - 2.10

print('d1 =', d1, ' d2 =', d2)

if d1 == d2:
    print('Same')
else:
    print('Different')













    

diff = d1 - d2 # Compute difference
if diff < 0: # Compute absolute value
    diff = -diff
if diff < 0.0000001: # Are the values close enough?
    print('Same')
else:
    print('Different')









# while example
print("enter the input")
x = int(input()) # Get integer from user
while x != 0:
    print(x) # Print x only if x is nonzero
    x -= 1 # Decrement x




# range example
for n in range(21, 0, -3):
    print(n)









for c in 'ABCDEF':
    print('[', c, ']', end='', sep='')
print()




# example for the nested loops
# Get the number of rows and columns in the table
size = int(input("Please enter the table size: "))

for row in range(1, size + 1):
    for column in range(1, size + 1):
        product = row*column # Compute product
        print(product, end=' ') # Display product
    print()                     # to move the cursor to the next row




















# break and continue example
sum = 0
done = False
while not done:
    val = int(input("Enter positive integer (999 quits):"))
    if val < 0:
        #break

        print("Negative value", val, "ignored")
        continue # Skip rest of body for this iteration
    if val != 999:
        print("Tallying", val)
        sum += val
    else:
        done = (val == 999) # 999 entry exits loop
print("sum =", sum)












word = input('Enter text (no X\'s, please): ')
vowel_count = 0
for c in word:
    if c == 'A' or c == 'a' or c == 'E' or c == 'e' \
        or c == 'I' or c == 'i' or c == 'O' or c == 'o':    
        print(c, ', ', sep='', end='') # Print the vowel
        vowel_count += 1 # Count the vowel
    elif c == 'X' or c =='x':
        print('X not allowed')
        break
else:
    print(' (', vowel_count, ' vowels)', sep='')

"""





"""
def multiply(x,y):
    return(x*y)



