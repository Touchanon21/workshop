# 1.จงเขียนตารางสูตรคูณให้ผลลัพท์ที่ออกมาเป็นแบบตัวอย่างด้านล่างโดยใช้คำสั่ง while
# 2.จงเขียนตารางสูตรคูณให้ผลลัพท์ที่ออกมาเป็นแบบตัวอย่างด้านล่างโดยใช้คำสั่ง for

for i in range(1, 13):
    num = 1
    for num in range(1, 13):
        print('{0} * {1} : {2}'.format(i, num, i*num))
        num = num+1
    print('===========================')
    i = i + 1


i = int(input("เลือกแม่สูตรคูณที่คุณต้องการ?"))
while(i <= 12):
    j = 1
    while(j <= 12):
        print('{0} * {1} : {2}'.format(i, j, i*j))
        j = j + 1
    print('===========================')
    i = i + 1
