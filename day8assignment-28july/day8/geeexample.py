class distance:
    def __init__(self,x=None,y=None):
        self.ft=x
        self.inch=y
    def __ge__(self,x):
        val1=self.ft*12+self.inch
        val2=x.ft*12+x.inch
        if val1>=val2:
            return True
        else:
            return False
d1=distance(1,2)
d2=distance(5,7)
print(d1>=d2)

