# EX1
a = 33
b = 200

if b > a:
    print("b is greater than a")

# EX2
a = 33
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# EX3
a = 200
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# EX4
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")

# EX5
a = 2
b = 330

max = a if a > b else b

print(max)

# EX6
a = 200
b = 33
c = 500

if a > b and c > a:
       print("Both conditions are True")

# EX7
a = 200
b = 33
c = 500

if a > b or c > a:
       print("At least one of the conditions is True")

# EX8
x = 41

if x > 10:
       print("Above ten,")
       if x > 20:
           print("and also above 20!")
        else:
            print("but not above 20.")






