'''
Python generator is kind of a function only.It generates a sequence of values that we can iterate on.

unlike functions generators do not terminate after returning the values

yield keyword is used
generator is also iterable

generators preserve the state of function
'''



def my_gen():
    n=1
    print("First time")
    yield n

    n+=1
    print("Second time")
    yield n

    n+=1
    print("third time")
    yield n

gen = my_gen()
# print(gen)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))