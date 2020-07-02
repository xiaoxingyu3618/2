# def print_double_list(double_list):
#     for r in double_list:
#         for c in r:
#             print(c,end=" ")
#         print()
#
# list01 = [
#     [1,2,3,44],
#     [4,5,5,65,5],
#     [5,6,7,89,0]
# ]
# print(print_double_list(list01))

list01 = [
    [1, 2, 3, 44, 56],
    [4, 5, 5, 65, 55],
    [5, 6, 7, 89, 5],
    [4, 5, 5, 65, 6],
    [4, 55, 7, 65, 6]
]

for r in range(len(list01) - 1):  # 0 1 2
    for c in range(r + 1, len(list01)):  # 1 2 3
        list01[r][c], list01[c][r] = list01[c][r], list01[r][c]

print(list01)
