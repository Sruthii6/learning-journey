"""
mylist = [1,2,3,4]


my_iter = iter(mylist)

print(next(my_iter))

print(next(my_iter))

print(my_iter.__next__())

print(my_iter.__next__())

next(my_iter)


"""

class PowTwo:
    def __init__(self,max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
       # if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
       # else:
        #    raise StopIteration

a = PowTwo(6)

i = iter(a)

print(next(i))
print(next(i))

for i in PowTwo(6):
    print(i)

# infinite iterators
int()

inf = iter(int,1)

print(next(inf))


a = iter(PowTwo())

print(next(a))

print(next(a))

print(next(a))








      







