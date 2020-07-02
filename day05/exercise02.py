"""
    在控制台中录入所有学生姓名
    如果姓名重复，则提示“姓名已经存在，不添加到列表中
    如果录入空，则倒叙输出
"""

list_name = []

while True:
    str_name = input("请输入姓名：")
    if str_name == "":
        break
    elif str_name not in list_name:
        list_name.append(str_name)
    else:
        print("姓名已经存在")

for index in range(len(list_name) - 1, -1, -1):
    print(list_name[index])


