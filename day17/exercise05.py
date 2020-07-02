list01 = [43, 4, 5, 5, 6, 7, 87]


# 需求1:在列表中查找所有偶数
def find01():
    for item in list01:
        if item % 2 == 0:
            yield item


# 需求2:在列表中查找所有大于10的数
def find02():
    for item in list01:
        if item > 10:
            yield item


# 需求3:在列表中查找所有范围在10--50之间的数
def find03():
    for item in list01:
        if 10 < item < 50:
            yield item


# "封装"
def condition01(item):
    return item % 2 == 0


def condition02(item):
    return item > 10


def condition03(item):
    return 10 < item < 50


# "继承"
def find(func_condition):
    for item in list01:
        # "多态"
        # 调用:具体条件的抽象
        # 执行:具体条件的函数
        if func_condition(item):
            yield item

for item in find(condition02):
    print(item)