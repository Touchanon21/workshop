# จงเขียนโปรแกรมเพื่อทำการคำนวณเกรดโดยมีเงื่อนไขดังนี้

# คะแนน 80 - 100 ได้ A
# คะแนน 75 - 79 ได้ B+
# คะแนน 70 - 74 ได้ B
# คะแนน 65 - 69 ได้ C+
# คะแนน 60 - 64 ได้ C
# คะแนน 55 - 59 ได้ D+
# คะแนน 50 - 54 ได้ D
# คะแนน 0 - 49 ได้ F

# และให้แสดงผลตามตัวอย่างด้านล่าง

# Enter your score: 49
# grade:  F

score = int(input('Enter the Score :'))
score = int(score)

if score >= 80:
    grade = 'A'
elif score >= 75:
    grade = 'B+'
elif score >= 70:
    grade = 'B'
elif score >= 65:
    grade = 'C+'
elif score >= 60:
    grade = 'C'
elif score >= 55:
    grade = 'D+'
elif score >= 50:
    grade = 'D'
else:
    grade = 'F'
print('Your Grade : ' + grade)
