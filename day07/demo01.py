"""
   ["无忌","赵敏","周芷若"]   [101,102,103]
"""
list01 = ["无忌", "赵敏", "周芷若"]
list02 = [101,102,103]
dict01 = {}
for i in range(len(list01)):
    dict01[list01[i]] = list02[i]

dict02 = {item:len(item) for item in list01}

print(dict01)
