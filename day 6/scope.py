x = 10

def add_x(x):
    new_x = 99
    return new_x

def sub_x():
    global x
    x = 5
    return x

result = add_x(x)
print(result)
result2 = sub_x()
print(result2)
print(x)
