'''
dictionary -> {key : value}
mutable
ordered
iterable
keys can only be immutable datatypes
'''

# friends = dict(input("Enter name and age: ").split() for _ in range(4))
# print(friends)


from platform import freedesktop_os_release


stu = {
    "fname" : "John",
    "lname" : "Doe",
    "course" : ["Python","django"],
    
}

# print(stu["course"][0])

stu["age"]=15
# stu["fname"]="john"
# print(stu)

# print(stu.items())
# print(stu.keys())
# print(stu.values())

# for k,v in stu.items():
#     print(f"key is {k} and value is {v}")

# TODO: count frequency of each character in a given string
# python -> {'p':1,'y':1}

# TODO: you are given a paragraph . Find occureence of each word

# print(stu['country'])

# print(stu.get('country',-1))

# print(stu.pop("fname"))

# stu.update([('frn','Jacky')])
# print(stu)

# stu.setdefault('country',"NONE")
# print(stu)

# print(stu)
# stu.popitem()
# print(stu)

s= "we are learning python"

# freq={}

# for i in s:
#     if freq.get(i):
#         freq[i] +=1
#     else:
#         freq[i]=1
# print(freq)


s_list=s.split()
# print(s_list)

freq={}

for i in s_list:
    if freq.get(i):
        freq[i]+=1
    else:
        freq[i]=1
print(freq)

print(freq['are'])
