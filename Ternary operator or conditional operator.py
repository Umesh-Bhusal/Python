#Lesson 6
from itertools import chain

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

# Special operators
#  identity operator
#  Membership operator
#
# identity  operator
#  two types of identity operator:
#            is
#            is not
# to compare address   but not sano cha ki thulo cha
# to ckeck address is same or not

a=10
b=10
print(id(a))
print(id(a))
print(a is b)
print(a is not b)

 # Membership operator (in, not in)
x= "python is fun"
print('s' in x)
print("s" not in x)

a=["umesh", "gita", "sita"]
print("umesh" in a)
print("umesh" not in a)

