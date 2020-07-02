"""
    将1970年到2050年中的闰年，存入列表  （列表推导式）
"""

"""
    一堆数据用代码描述
"""
dict_result = {}
str_target = "abcdefce"
for item in str_target:
    if item not in dict_result:
        dict_result[item] = 1
    else:
        dict_result[item] += 1

print(dict_result)
