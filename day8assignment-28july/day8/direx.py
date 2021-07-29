class student:
    def __dir__(self):
        return[1,2,3]
s=student()
att=dir(s)
print(att)