# 练习:1. 获取列表中所有字符串
#     2. 获取列表中所有小数
# 要求:分别使用生成器函数/生成器表达式/列表推导式完成.
list01 = [3, "54", True, 6, "76", 1.6, False, 3.5]


def find_str(list_target):
    for item in list_target:
        if type(item) == str:
            yield item

re = find_str(list01)
for item in re:
    print(item)