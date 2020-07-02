"""
    2048 core
"""
list_merge = [8, 2, 0, 2]


def zero_to_end():
    """
        零元素移动到末尾
    :return:
    """
    for item in range(len(list_merge) - 1, -1, -1):
        if list_merge[item] == 0:
            del list_merge[item]
            list_merge.append(0)


def merge():
    """
        合并
    :return:
    """
    zero_to_end()
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i] += list_merge[i + 1]
            del list_merge[i + 1]
            list_merge.append(0)


map = [
    [2, 0, 0, 2],
    [4, 4, 2, 2],
    [2, 4, 0, 4],
    [0, 0, 2, 2],
]


def move_left():
    for line in map:
        global list_merge
        list_merge = line
        merge()


# move_left()
#
# move_left()
# print(map)


def move_right():
    for line in map:
        global list_merge
        list_merge = line[::-1]
        merge()
        line[::-1] = list_merge


# move_right()
# print(map)

def matrix_transport(list01):
    for r in range(len(list01) - 1):
        for c in range(r + 1, len(list01)):
            list01[r][c], list01[c][r] = list01[c][r], list01[r][c]


def move_up():
    matrix_transport(map)
    move_left()
    matrix_transport(map)


def move_down():
    matrix_transport(map)
    move_right()
    matrix_transport(map)


move_down()
print(map)
