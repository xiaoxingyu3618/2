"""
    元组
        基础操作
    列表与元组可以互相转换
    容器封装思想
"""
# 练习：在控制台中录入月份和日  计算天数

day_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
month = int(input("请输入月份："))
day = int(input("请输入日："))
total_day = sum(day_of_month[:month-1])
total_day += day
print(total_day)

