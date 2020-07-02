"""
    练习1：在控制台中获取一个开始值和结束值，将中间的数值打印出来
"""

# begin = int(input("请输入开始值："))
# end = int(input("请输入结束值："))
#
# while begin < end:
#     print(begin)
#     begin += 1

"""
    练习2：一张纸的厚度是0.01mm  请计算对折多少次超过珠穆朗玛峰8844.43m
"""

mountain = 8844430
paper = 0.01
count = 0
while paper < mountain:
    count += 1
    paper *= 2
else:
    print(count)
