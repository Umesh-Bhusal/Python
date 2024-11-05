#lesson 5
#AND , OR, NOT
from operator import truediv

# Logical operator = boolean types vs Non boolean types

# bOOLEAN types= And, Or, Not

# Non boolean type =  0 = means false ,
# non 0 means True   (1, 2, 3, 4 ......... hello , any letter , words and alphabetic)
# empty = str, list, tuple,dic, set  output = empty







print(True and True)
print(True and False)
print(True or False)
print(not False)
print(not True)


# And operator
print(10 and 20)
print(0 and 20)
print("" and 20)
print([] and 20)
print ("hello" and "python")
print("" and "python")

username =input("enter your namet")
password=input("enter your password")
if username == "python" and password =="pass":
    print("correct")
else:
    print("username and password not match")

#OR Condition
# X or y

# x----->= true    Result ---> true
#  x----->= false  result----Y


# Not condition
print(not 10)
print(not [10.20])

