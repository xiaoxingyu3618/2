"""
    在控制台中录入多个人的多个喜好
"""

dict_hobby = {}
while True:
    name = input("请输入学生姓名：")
    if name == "":
        break
    dict_hobby[name] = []
    while True:
        hobby = input("请输入喜好：")
        if hobby == "":
            break
        dict_hobby[name].append(hobby)

for key, hobby in dict_hobby.items():
    print("%s喜欢：%s" % (key, hobby))
