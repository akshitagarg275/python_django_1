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
profile()

# TODO: keyword functions
# TODO: return statement
# TODO: variable length arguments
# TODO: variable length keyword arguments
# TODO: lambda functions

