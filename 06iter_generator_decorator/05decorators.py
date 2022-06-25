'''
High order function -> functions which take other functions as the argument 
everything inside python including functions is an object
'''

# def add(ele):
#     return ele+1

# def sub(ele):
#     return ele-1

# def calc(operator , val):
#     res = operator(val)
#     return res

# print(calc(add , 5))


'''
decorators
A decorator takes a function as a argument , adds some functionality to the existing code and 
return the function
'''

def basic():
    print("I am a basic function")

def add_feature(func):
    def wrapper():
        print("="*30)
        print("Functionality added")
        print("="*30)
        func()
    return wrapper

def add_feature1(func):
    def wrapper():
        print("$"*30)
        print("Functionality added")
        print("$"*30)
        func()
    return wrapper
# def add_feature(func):
#     def wrapper():
#         print("="*30)
#         print("Functionality added")
#         print("="*30)
#         func()
#     return wrapper

# new_func=add_feature(basic)
# new_func()

@add_feature
@add_feature1
def new_basic():
    print("I am new basic function")

new_basic()