list=["english","maths","rotor","madam","malayalam","noon"]
#new=[i for i in list if i==i[::-1]]
#print(new)
new=[i.upper() for i in list]
print(new)
new=[i.replace('noon','morning') for i in list]
print(new)


