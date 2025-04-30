class Person:
    def __init__(self,first,last):
        self.firstname = first
        self.lastname = last
        
    def name(self):
        return self.firstname + " " + self.lastname

    def __str__(self):
        return self.firstname + " " + self.lastname
    
class Employee(Person):
    
    def __init__(self,first,last,empid):
        #Person.__init__(self,first,last)
        super().__init__(first,last)
        
        self.employee_no = empid
        

    def getEmployee(self):
         return self.name() + ", " + self.employee_no

    def __str__(self):
        return super().__str__() + "," + self.employee_no

p1 = Person("abc","xyz")

p2 = Employee("ght","oij","1234")

print(p1.name())

print(p2.getEmployee())

print(p1)
print(p2)
"""
print(Employee.__mro__)

print(Person.__mro__)
"""


    
