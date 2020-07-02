"""
    判断是否为素数
"""

number = int(input("请输入一个数："))


for item in range(2, number):
    if number % item == 0:
        print("不是素数")
        break
else:
    print("是素数")