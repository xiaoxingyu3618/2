"""
    商品单价：25 （unit_price）
    商品数量：2   (number)
    最后获取金额：60
    应该找回多少钱
"""

unit_price = input("请输入商品单价：")
count = input("请输入商品数量：")
money = input("请输入金额：")
result = float(money) - float(unit_price) * float(count)
print("应找回的金额为：" + str(result))
