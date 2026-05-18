def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Emma"))
print(greet("Mike", "Hey"))
print(greet("Steve"))
print(greet(greeting="Yo", name="Sam"))
print(greet("Justin",goodbye="Welcome"))
