# & .........>1 ta matra cha bhani bitwise and
# | -------> bitwise or
# ^ ---------------> bitwise x-or
# ~ ---------> bitwise not / complement
#
# << -----------> left shif operator
# >> --------------> right shift operatir
#
# to use bitwise operator it must be INT or BOOL it does not work with other if you use it it show error

# & -> if both bits are 1 then result is 1 else 0
# | ---> if atlest one bit is 1  resuolt  is 1 else result is 0
# ^ -> if bits are diff result is 1 else 0
# ~ --> if there is 1 then it will give 0 if there is 0 then it will give 1  it turn positive into negative and negatice into positive

# AND condition

print (4&5)
#        100
#        101
# ---------------
       # 100  ------------ when you convert it it gives 4 because 100 means 4
# OR condition

print(4|5)

# 100
# 101
# ---
# 101 -----------> output 5

# x-OR condition


# ~ ---------> bitwise not / complement
#
# Notes: MSB indicates sign bit  = 0---> positive  1 ---> negative
#  positive number will be represented directly in memory
# whereas -ve numbers will be represented in 2's complement' form

print(~4)

