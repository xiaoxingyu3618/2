"""
    列表  遍历列表
"""
# str_list = "我是齐天大圣"
# list01 = list(str_list)
# print(list01)
# for item in list01[::-1]:  #形成新列表
#     print(item)

str_list = "我是齐天大圣"
list01 = list(str_list)
print(list01)
for index in range(len(list01) - 1, -1, -1):   #不复制列表
    print(list01[index])
