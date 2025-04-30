
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print(days[0])

days = {'January':31, 'February':28, 'March':31, 'April':30,
'May':31, 'June':30, 'July':31, 'August':31,
'September':30, 'October':31, 'November':30, 'December':31}

print(days['January'])


name ={}
print(name)

#key -value pair

salary ={'oa':1000,'driver':2000,'messenger':1200}

print(salary['oa'])

salary['oa'] = 1500

print(salary)

del salary['messenger']
print(salary)

salary['typist'] = 4000
print(salary)

#examples
ascii_value = {'A':65,'Z':97}

points = {'left':2,'right':4,'up':5,'down':3}

game_move = ['left','up','down','right','up']

score = sum([points[c] for c in game_move])
print(score)







import random
# indicate a deck of cards
deck = [{'value':i, 'suit':c}
    for c in ['spades', 'clubs', 'hearts', 'diamonds']
    for i in range(2,15)]

# list of 52 dictionaries
#print(deck)











print(deck[1]['value'])
print(deck[1]['suit'])

random.shuffle(deck)

print(deck)
print(deck[1]['value'])
print(deck[1]['suit'])



points = {'left':2,'right':4,'up':5,'down':3}
move_pts = points.copy()
print(move_pts)

mv = input('Enter the move: ')
if mv in points:
    print('The value is', points[mv])
else:
    print('Not valid move')
















#Lists of keys and values
points = {'left':2,'right':4,'up':5,'down':3}
# keys
print("the list",list(points))
# values
print("the list values",list(points.values()))
# key-value pairs
print("the list items",list(points.items())) 

L = [x[0] for x in points.items() if x[1]==2]
print(L)

#create dictionary from list
stat = dict([('pen',10),('eraser',5)])
print(stat)

print(len(stat))




s = "python is a programming language"

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1

    return d

ct = histogram(s)
print(ct)

import random
print(ct.get('a'))

L = [random.randint(1,100) for i in range(100)]
print(L)
freq = [L.count(i) for i in range(1,101)]
print("frequencies",freq)








