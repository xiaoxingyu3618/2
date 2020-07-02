list01 = [3, 4, 55, 6, 7]


def my_enumerate(iterable_target):
    for index in range(len(iterable_target)):
        yield (index, iterable_target[index])


for index, element in my_enumerate(list01):
    print(index, element)


def my_zip2(*args):
    # 根据星号元组形参args第一个参数的长度生成索引len(args[0])
    for i in range(len(args[0])):
        list_result = []
        for item in args:
            list_result.append(item[i])
        yield tuple(list_result)


for item in my_zip2(list02, list03):
    print(item)
