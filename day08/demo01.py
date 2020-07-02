def calculate_weight_jin(liang_weight):
    """
        根据两计算几斤零几两
    :param liang_weight: 计算需要的两
    :return: 元组（斤，两）
    """
    jin = liang_weight // 16
    liang = liang_weight % 16
    return (jin,liang)

re = calculate_weight_jin(188)
print(str(re[0])+"斤"+str(re[1])+"两")


