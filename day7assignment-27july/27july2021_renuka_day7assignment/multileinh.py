class operation1:
    def addition(self,n1,n2):
        return n1+n2
class operation2:
    def subtraction(self,n1,n2):
        return n1-n2
class operation3:
    def multiplication(self,n1,n2):
        return n1*n2
class  derivedclass(operation1,operation2,operation3):
    def division(self,n1,n2):
        return n1/n2
d=derivedclass()
n1=int(input("enter a number"))
n2=int(input("enter a number"))
print(d.addition(n1,n2))
print(d.subtraction(n1,n2))
print(d.multiplication(n1,n2))

