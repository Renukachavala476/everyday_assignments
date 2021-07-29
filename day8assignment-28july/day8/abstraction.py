#class A:
#   __name="raju"
#objA=A()
#print(objA.__name)
class A:
    __name="raju"           #hidden variable
    def Test(self):
        print(__name)
objA=A()
#objA.Test()
print(objA._A__name)        #syntax to access hidden variable

