"""
    选择语句  调试
"""

price = float(input("请输入商品的单价："))
count = int(input("请输入商品的数量："))
money = float(input("请输入金额："))
result = money - price * count
if result >= 0:
    print("应找回：" + str(result))
else:
    print("所付金额不足")