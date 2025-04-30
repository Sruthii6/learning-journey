"""

def fib(n):
    a,b =0,1
    for i in range(n):
        a,b = b, a + b
    return a

def fiblist(n):
    fib = {0,1}
    for i in range (1,n):
        fib += [fib[-1] +fib[-2]]
    return fib

if __name__ == "__main__":
    if fib(0) == 0 and fib(10) == 55 and fib(50) == 12586269025:
        print("test for fib successful")
    else:
        print("test for fib unsuccessful!")
"""
class Person:
    name = []

    def set_name(self,user_name):
        self.name.append(user_name)
        return len(self.name)

    def get_name(self,user_id):
        if user_id >= len(self.name):
            return "there is no such user"
        else:
            return self.name[user_id]
        
if __name__ == '__main__':
    person = Person()
    print('user sam has been added with id',person.set_name('sam'))
   # print('user associated with id o is ', person.get_name(0))

    print('user peter has been added with id',person.set_name('peter'))
    #print('user associated with id o is ', person.get_name(1))

    print('user david has been added with id',person.set_name('david'))
    #print('user associated with id o is ', person.get_name(2))

    print('user daisy has been added with id',person.set_name('daisy'))
    print('user associated with id 0 is ', person.get_name(2))
    print('user associated with id 0 is ', person.get_name(4))

    
    















