# EX1
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# EX2
string = "banana"
for char in string:
    print(char)

# EX3
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)

# EX4
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

# EX5
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
else:
    print("Finally finished!")

# EX6
adjectives = ["small", "big"]
fruits = ["apple", "banana", "cherry"]

for adjective in adjectives:
    for fruit in fruits:
        print(adjective, fruit)
