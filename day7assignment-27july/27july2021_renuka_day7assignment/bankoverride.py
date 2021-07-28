class RBI:
    def interest(self,n1):
        self.interest=n1
        print(self.interest)
class SBI(RBI):
    def interest(self,n2):
        self.interest=n2
        print(self.interest)
class HDFC(RBI):
    def interest(self,n3):
        self.interest=n3
        print(self.interest)
objrbi=RBI()
objrbi.interest(5)
objsbi=SBI()
objsbi.interest(6)
objhdfc=HDFC()
objhdfc.interest(7)
