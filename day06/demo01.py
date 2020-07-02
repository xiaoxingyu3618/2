"""
    列表推导式
"""
# 列表中每个数加1
# list01 = [46, 84, 35, 14, 8, 94, 68, 16]
# list02 = [item + 1 for item in list01]
# print(list02)

# 将list01中大于20的元素，增加1后存入list02中
# list02 = []
# for item in list01:
#     if item >20:
#         list02.append(item+1)
# list02 = [item+1 for item in list01 if item >20]
#
# print(list02)


# 使用range 生成1-10的数字，将数字的平方存入list01中
# list01奇数存入list02
# list01偶数存入list03
# list01 = []
# for item in range(1, 11):
#     list01.append(item ** 2)

list01 = [item ** 2 for item in range(1, 11)]
list02 = [item for item in list01 if item % 2 == 1]
list03 = [item for item in list01 if item % 2 == 0]
list04 = [item + 1 for item in list03 if item > 5]
print(list04)