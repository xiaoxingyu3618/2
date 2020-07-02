"""
    练习随机加法考试
    随机数（1-10）
    控制台中获取两数相加的结果
"""
import random

score = 0
for item in range(3):
    random_number01 = random.randint(1, 10)
    random_number02 = random.randint(1, 10)
    input_number = int(input("请输入" + str(random_number01) + "加" + str(random_number02) + "等于"))
    if input_number == random_number01 + random_number02:
        score += 10
print(score)

