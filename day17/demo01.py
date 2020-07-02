list01 = [3, "54", True, 6, "76", 1.6, False, 3.5]

# 生成器函数
def find_int(list_target):
    for item in list_target:
        if type(item) == int:
            yield item
#
#
# re = find_int(list01)
# for item in re:
#     print(item)

re = (item for item in list01 if type(item) == int)
for item in re:
    print(item)