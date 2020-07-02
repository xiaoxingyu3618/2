"""
    猜数字游戏
    游戏随机运行产生一个1-100的随机数
    提示：大了，小了，猜对了
"""

import random

random_number = random.randint(1, 100)
count = 0
while True:
    input_number = int(input("你猜的数字："))
    count += 1
    if input_number > random_number:
        print("大了")
    elif input_number < random_number:
        print("小了")
    else:
        print("猜对了，总共猜了" + str(count) + "次")
        break
