"""
    上一次作业
"""
# 3
# name = "悟空"
# age = 800
# score = 99.5
# message = "我叫%s,年龄是%d,成绩是%.1f。" % (name, age, score)
# print(message)

"""
    在控制台中画矩形
"""
# number = int(input("请输入整数："))
# for item in range(number):
#     if item == 0 or item == number - 1:
#         print("*" * number)
#     else:
#         print("*" + " " * (number - 2) + "*")

"""
    小球弹落问题
"""

height = 100
count = 0
distance = 100
while height / 2 > 0.01:
    height /= 2
    count += 1
    print("第%d次弹起来的高度是%f." % (count, height))
    distance += height * 2

print("总共经过的距离是%.2f" % distance)
