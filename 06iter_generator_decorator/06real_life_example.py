DB={
    'admin':'p@ss'
}


def login(func):
    def wrapper(username, password , *args , **kwargs):
        if username in DB and DB[username] == password:
            func(*args, **kwargs)
        else:
            print("You are not authenticated")
    return wrapper

@login
def add(a,b):
    print(a)
    print(b)
    print(a+b)

add(3,5)
add('admin','p@ss',2,5)


