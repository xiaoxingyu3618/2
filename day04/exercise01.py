"""
    在控制台中获取一个整数，如果是偶数赋值为偶数
"""

number = int(input("请输入一个整数："))
state = "奇数" if number % 2 else "偶数"
print(state)
