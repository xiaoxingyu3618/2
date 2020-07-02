"""

    练习2

"""
date01 = input("请输入第一个变量：")
date02 = input("请输入第二个变量：")
# 所有语言通用思想
# temp = date01
# date01 = date02
# date02 = temp

# 适合Python
date01, date02 = date02, date01
print("第一个变量是：" + date01)
print("第二个变量是：" + date02)
