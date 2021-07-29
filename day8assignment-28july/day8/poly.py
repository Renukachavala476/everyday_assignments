class A:
    def sayHello(self):
        print("hello")
class B(A):
    def sayHello(self):
        print("hai")
objA=A()
objB=B()
objA.sayHello()
objB.sayHello()
