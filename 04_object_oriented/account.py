class Account:
    int_rate = 0.05
    __counter = 0

    def __init__(self,accno,accname,bal):
        self.accno = accno
        self.accname = accname
        self.bal = bal
        type(self).__counter += 1
        
    def __str__(self):
        return 'accno = {0}, accname = {1},bal = {2}, int_rate = {3}'.format(self.accno,self.accname,self.bal,self.int_rate)

    def __del__(self):
        type(self).__counter -= 1

    @staticmethod
    def account_instance():
        return Account.__counter

    @classmethod
    def account_instance(self):
        return self, Account.__counter
    
ac1 = Account(123,'abc',2000)
ac2 = Account(124,'xyz',300)

print(ac1.int_rate)
print(ac2.int_rate)
print("ac1 modified")
ac1.int_rate += 0.02
print(ac1.int_rate)

Account.int_rate += 0.02



#print(ac1)

print(ac1.__dict__)


#del ac2

#print("number of instances : " + str(Account.__counter))

print(Account.account_instance())

print("account dictionary")

print(Account.__dict__)

