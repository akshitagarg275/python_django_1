'''
a function calling itself

base case
a smaller solution
'''

# TODO:1+2+3+4+5 

'''
n + f(n-1)


'''


# def sum_rec(n):
#     if n==1:
#         return 1
    
#     return n + sum_rec(n-1)

# nth fibonacci nums
# 0 1 1 2 3 5 8 13

def fib(n):
    if n==0 or n==1 :
        return n
    
    return fib(n-1)+fib(n-2)


# print(fib(5))

for i in range(6):
    print(fib(i), end=" ")