"""
    for for
"""
# for r in range(3):
#     for c in range(4):
#         print("*", end=" ")
#     print()

"""
    *#*#*#
    *#*#*#
    *#*#*#
    *#*#*#
"""

# for r in range(4):
#     for c in range(6):
#         if c % 2 == 0:
#             print("*", end="")
#         else:
#             print("#", end="")
#     print()

"""
    *
    **
    ***
    ****
"""
# for r in range(4):
#     for c in range(r + 1):
#         print("*", end="")
#     print()

"""
    [3,80,45,5,7,1]  列表升序
"""
# list_input = [3, 80, 45, 5, 7, 1]
# for r in range(len(list_input) - 1):  # 1 2 3 4
#     for c in range(r + 1, len(list_input)):
#         # list_input[0]  list_input[c]
#         if list_input[r] < list_input[c]:
#             list_input[r], list_input[c] = list_input[c], list_input[r]
# print(list_input)

"""
    [3,80,45,5,80,1]  判断列表是否重合
"""

# list01 = [3, 80, 45, 5, 81, 1]
# result = False
# for r in range(len(list01) - 1):
#     for c in range(r + 1, len(list01)):
#         if list01[r] == list01[c]:
#             print("有相同")
#             result = True
#             break
#     if result:
#         break
#
# if result == False:
#     print("没有相同")

"""
    矩阵转置
"""


"""
    列表推导式嵌套
"""