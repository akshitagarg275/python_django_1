'''
yield returns a value and pauses the execution while maintaining the internal state

return statement returns a value and terminates the execution of the function

when a generator is called it returns an object(iterato) but does not start execution immediately

local variables and their stated are remembered between successive calls
'''

# function
def count(n):
    i=1
    while i<=n:
        return i
        i+=1

# print(count(5))

# generator
def gen_count(n):
    i=1
    while i<=n:
        yield i
        i+=1

# print(gen_count(5))
# my_gen=gen_count(5)
# print(next(my_gen))

# for ele in my_gen:
#     print(ele)


