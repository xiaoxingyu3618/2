"""
    在控制台中获取一个字符串
    打印第一个字符

"""
str01 = "我叫齐天大圣"
print(str01[0])
print(str01[-1])
print(str01[-3])
print(str01[:2])
print(str01[::-1])
if len(str01) % 2 == 1:
    print(str01[len(str01) // 2]
