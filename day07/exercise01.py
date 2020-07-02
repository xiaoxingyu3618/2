"""
    在控制台中循环录入字符串，输入空字符串为止
"""
set_result = set()
while True:
    str_input = input("请输入字符串：")
    if str_input == "":
        break
    set_result.add(str_input)

