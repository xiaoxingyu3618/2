"""
    在控制台中获取字符串，打印每个字符的编码值
"""

# str01 = input("请输入字符串：")
# for item in str01:
#     number = ord(item)
#     print(number)


"""
    在控制台中录入一个编码值，然后打印字符
"""
while True:
    str_code = input("请输入编码值：")
    if str_code == "":
        break
    code = int(str_code)
    print(chr(code))
