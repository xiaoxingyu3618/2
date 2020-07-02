def square_matrix_transposition(target_list):
    '''
        方阵转置
    :param target_list:
    :return:
    '''
    for r in range(len(target_list) - 1):  # 0 1 2
        for c in range(r + 1, len(target_list)):  # 1 2 3
            target_list[r][c], target_list[c][r] = target_list[c][r], target_list[r][c]


target_list = [
    [1, 2, 3, 44, 56],
    [4, 5, 5, 65, 55],
    [5, 6, 7, 89, 5],
    [4, 5, 5, 65, 6],
    [4, 55, 7, 65, 6]
]

square_matrix_transposition(target_list)
print(target_list)