"""
    练习1：在控制台中循环录入商品信息（名称，单价）
        如果名称录入空字符，则停止录入
"""
# dict_commodity = {}
# while True:
#     name = input("请输入商品名称：")
#     if name == "":
#         break
#     price = int(input("请输入商品单价："))
#     dict_commodity[name] = price
#
# for key, value in dict_commodity.items():
#     print("%s商品的单价是%d" % (key, value))

"""
    练习2：在控制台中循环录入学生信息（姓名，年龄，成绩，性别）
        如果名称录入空字符，则停止录入   字典内嵌字典
"""
list_student = []
while True:
    name = input("请输入学生姓名：")
    if name == "":
        break
    age = int(input("请输入年龄："))
    score = int(input("请输入成绩："))
    sex = input("请输入性别：")
    dict_info = {"name": name, "age": age, "score": score, "sex": sex}
    list_student.append(dict_info)

for dict_value in list_student:
    print("%s年龄是%d，成绩是%d，性别是%s" % (dict_value["name"], dict_value["age"], dict_value["score"], dict_value["sex"]))
