'''
unary

-binary 
    -arithmetic
    -assignment
    -relational
    -logical
    -bitwise
    -membership
    -identity
'''

# TODO: unary
# a=-2

# TODO: Arithmetic operator
'''
+,-,/,*
'''

# print(5+3)
# print(5-3)
# print(5*3)
# print(5/3)

# floor divison (//)
# print(5//3)

# modulus operator (%) remainder
# print(5%3)


# TODO : assignment '='

a = 2

# a = a *3
# a*=3

# print(a)


'''
relational(comparison) operator 
It return either True/False
> : greater than
< : less than
>= : greater than equal to
<= : less than equal to
== : equal to
!= : not equal to
'''

# print(4>2)

# print(5>=4)
# print(5>=5)

# print(5==5)

# print(5!=5)

'''
Logical operator
and - if any one input is False output will be False

or - if any one input is True ouyput will be True

not - It reverses the current state 
'''

# print(5>3 and 2<1)

# print(5>3 or 2<1)

# Falsy values -> 0, False, None, ""
# print(not 0)
# print(not -1)
# print(not "")


# Bitwise operators
'''
It simply performs operation on bits
& : bitwise and
| : bitwise or
^ : bitwise xor
<< : bitwise left shift
>> : bitwise right shift
'''

# print(5&8)

# print(5| 8)

# print(5^8)

# bitwise left shift << : It increase the bits

# print(5<<1)
# print(5<<2)

# bitwise right shift : It decreases the bits

# print(10>>1)
# print(10>>2)

#membership operator (in)

nums = [1,2,3,4,5,6]

# print(1 in nums)
# print(1 not in nums)

# st="python"
# print("P" in st)

# identity operator (is)
# It checks whether two variables' value is at same memory address

# a=5
# print(id(a))

# b=5
# print(id(b))

# print(a is b)


l1=[1,2]
print(id(l1))

l2=[1,2]
print(id(l2))

print(l1 is l2)

l3 =l1
print(id(l3))

print(l3 is l1)



