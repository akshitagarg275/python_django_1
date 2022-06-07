'''
errors

syntax error 

logical error -> 2+2 =4 , 2+2=22

runtime error -> on execution of the program

exception handling allows us to handle potentially occurring errors gracefully
'''

# try:
#     pass

# except :
#     pass


n1=4
n2=0

# try:
#     print(n1//n2)
#     # print(a)


# except ZeroDivisionError as e:
#     print(e)
#     print("Denominator cannot be zero")
# except BaseException as e:
#     print(e)

# else: 
#     print("Either except block executes or else block gets executed")
# finally:
#     print("No matter what exception will occur")


# a=0
# if a==0:
#     raise "denominator can't be zero"

name="John"

# if name=="John":
#     raise ValueError("John is not allowed")



def func():
    try:
        return 1
    except:
        return 2
    else:
        return 3
    finally:
        return 4

print(func())