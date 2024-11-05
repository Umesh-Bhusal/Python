#Lesson 6

# syntax:
# x = (first value) if (condition) else (second value)

a= 10
b=20
x=30 if a>b else 20
print (x)

# By default input la string lencha
a= int(input("enter first number"))
b= int(input("enter second number"))
min = a if a<b else b
# ( a print gar if a b vanda sano cha bhani )
print(min)

#Nesting of ternary operation

a= int(input("enter first number"))
b= int(input("enter second number"))
c= int(input("enter third number"))
min=a if a<b and a<c else b if b<c else c
print(min)




