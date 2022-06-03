nums= [1,2,3,4,5,6]

# nums = [ i for i in range(1,7)]
# print(nums)

# even = [i for i in range(0,11,2)]
# even = [i for i in range(0,11) if i%2==0]
# print(even)

# give a list , if a no is even provide its square , if it is odd provide its cube

nums = [ i**2 if i%2==0 else i**3 for i in range(0,11)]
# print(nums)


twoDMatrix = [[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]]

# print([ [i[j]for i in twoDMatrix] for j in range(len(twoDMatrix))])

mat = [[j for j in range(5)] for i in range(3)]
# print(mat)

# TODO: dictionary comprehension
# {k:v for k,v in iterable}

# nums = {i:i**2 for i in range(5)}
# print(nums)


# val = {i.upper(): i for i in  'python'}
# print(val)


# keys= ['a','b','c','d','e']
# vals=[1,2,3,4,5]

# print({k:v for (k,v) in zip(keys,vals)})

# print([i for i in range(1,100) if (i%2==0 and i%5==0)])
# print([i for i in range(1,100) if i%2==0 if i%5==0])
