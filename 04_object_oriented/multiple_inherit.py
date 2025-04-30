class Person:
    def __init__(self,first,last):
        #super().init()
        self.firstname = first
        self.lastname = last
        
    def __str__(self):
        return self.firstname + " " + self.lastname
    
class Employee(Person):
    
    def __init__(self,first,last,empid):
        super().__init__(first,last)
        #self.firstname = first
       # self.lastname = last
        self.employee_no = empid

    def __str__(self):
        return super().__str__() + "," + str(self.employee_no)

class Hourly_Employee(Employee,Person):

    def __init__(self,first,last,empid,sal):
        super().__init__(first,last,empid)
        self.salary = sal

  #  def __str__(self):
   #     return str(self.firstname,self.lastname,self.employee_no,self.salary)

    def getHourly_Employee(self):
        print("%s %s %d %d " % (firstname,lastname,employee_no,salary))
#p1 = Person("abc","xyz")

#p2 = Employee("ght","oij",1234)

p3 = Hourly_Employee("acb","hjr",1245,2000)


#print(p1)
#print(p2)
print(p3)
print(isinstance(p3,Person))
print(isinstance(p3,Employee))
#print(issubclass(p3,Person))
#p3.getHourly_Employee()
print(Hourly_Employee.__mro__)


