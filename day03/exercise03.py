"""
    简易计算器
"""

number01 = float(input("请输入第一个数字："))
operator = input("请输入运算符：")
number02 = float(input("请输入第二个数字："))
if operator == "+":
    result = number01 + number02
    print("结果为：" + str(result))
elif operator == "-":
    result = number01 - number02
    print("结果为：" + str(result))
elif operator == "*":
    result = number01 * number02
    print("结果为：" + str(result))
elif operator == "/":
    result = number01 / number02
    print("结果为：" + str(result))
else:
    print("运算符有误")
