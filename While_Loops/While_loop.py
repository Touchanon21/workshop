# EX1
i = 1
while i < 5:
    print(i)
    i += 1

# EX2
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# EX3
i = 1
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# EX4
i = 1
while i < 3:
    print(i)
    i += 1
else:
    print("i is no longer less than 3")
