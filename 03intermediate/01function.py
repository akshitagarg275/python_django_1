'''
DRY-> Donot Repeat Yourself
when a set of code is wrapped under a name

def function_name(parameters):
    function statements
'''

# function definition
def greet():
    print("Good morning")

# calling
# greet()

# TODO: parameterised functions

# def profile(name,age):
#     print(f"name is {name} and age is {age}")

# profile("John",13)
n="Jane"
a=14
# profile(n,a)
# profile(n)

# TODO: default functions
# NOTE: default arguments will always come after non-default arguments
def profile(name="NA",age="NA"):
    print(f"name is {name} and age is {age}")
    
# profile(n,14)
# profile()
# profile(13 , "Jane")


# TODO: keyword functions
def profile(name="NA",age="NA"):
    print(f"name is {name} and age is {age}")

# profile(age=13, name="Jane")

# TODO: return statement

def calc (num1 , num2):
    return num1+num2 , num1 - num2

# print(calc(2,3))
# ans1 , ans2 = calc(5,6)
# print("Sum is :",ans1)
# print("Diff is :",ans2)

# TODO: variable length arguments
def func(*args):
    # print(args)
    # print(type(args))
    count=0
    sum=0
    for i in args:
        sum+=i
        count+=1
    print("Count is :",count)
    print("Sum is: ",sum)
# func(1,2,3,4,5,6,7)
# func(1,2,3,4)

# TODO: variable length keyword arguments
def func(**kwargs):
    # print(kwargs)
    # print(type(kwargs))
    for k,v in kwargs.items():
        print(f"{k}--> {v}")

# func(fname="John",lname="Doe")

# TODO: lambda functions
# variable_name = lambda parameters : expression

# def isEven(num):
#     return num%2==0

# print(isEven(23))


# isEven = lambda x : x%2==0
# sum = lambda a,b : a+b

# print(sum(7,9))

# max = lambda a,b : a if (a>b)  else b


# TODO: map
nums=[1,2,3,4,5,6]
sqr = list(map(lambda x : x**2, nums))
# print(sqr)
# TODO: filter

odd = list(filter(lambda x : x%2!=0,nums))
print(odd)

# TODO: reduce

from functools import reduce

sum = reduce(lambda a,b : a+b,nums)
print(sum)

# print(max(14,5))

# print(isEven(3))

# n=[]
# a=int(input())

# n.append(a**2)
# print(a)