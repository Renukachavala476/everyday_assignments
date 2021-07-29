class Employee:
    def __init__(self):
        self.name="renuka"
        self.salary=10000
    def __str__(self):
        return "name="+self.name+"  salary="+str(self.salary)
e=Employee()
print(e)