"""
    在控制台中录入西游记喜欢的人物
"""

list_person = []

while True:
    str_input = input("请输入西游记中喜欢的人物：")
    if str_input == "":
        break
    list_person.append(str_input)

for item in list_person:
    print(item)