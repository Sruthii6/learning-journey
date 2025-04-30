class Comp:
    def __init__(myobj,real = None,imag = None):
        myobj.real = real
        myobj.imag = imag

    def increment(myobj,val):
        myobj.real += val
        myobj.imag += val
        

    def add_complex(myobj,c1):
        c1.real += myobj.real
        #myobj.real += c1.real
        
        c1.imag += myobj.imag
        return(c1)

    def add_two_complex(myobj,c1,c2):
        c3 = Comp()
        c3.real = c1.real + c2.real
        c3.imag = c1.imag +c2.imag
        return c3
    
    def __add__(myobj,other):
        if isinstance(other,Comp):
            return myobj.add_complex(other)
        else:
            return myobj.increment(other)
        
    def __lt__(myobj,other):
        return ((myobj.real,myobj.imag)< (other.real,other.imag))

    def __ne__(myobj,other):
        return not myobj == other
    
    def __ge__(myobj,other):
        return not myobj < other    
    
    def __str__(myobj):
        return 'real = {0},imag ={1}'.format(myobj.real,myobj.imag)

    def print_complex(myobj):
        print(("hi %d %d ")% (myobj.real,myobj.imag))

    def print_attributes(myobj):
        for attr in vars(myobj):
            print(attr, getattr(myobj,attr))

c1 =Comp(2,3)
c2 =Comp(4,8)
    
# string representation
print("string representation")
print(c1)
print(c2)


# print ction
print("print function")
c1.print_complex()
c2.print_complex()

print(c1.__dict__)

"""
print("after increment")

c2.increment(13)
c2.print_complex()

print('after adding complex with self')
c1.add_complex(c2)
c2.print_complex()
print(c1)
"""
print('after adding 2 complex and return')
c3 = Comp(2,5)


#If you want to allow passing no arguments to the Class initiator, you have to define the initiator with default values set to None 

c4 = c1.add_two_complex(c2,c3)

c4.print_complex()


# type based prototyping
print(c1+c3)
    
c4 + 4

c4.print_complex()

#printing attributes taking attribute name as string and returing value
print('printing attributes')
print(vars(c4))

c4.print_attributes()

# comparisons
print(c1,c2,c3,c4)

print(c1 < c3)

print(c2 != c4)

print(c2 >= c4)




      








   


