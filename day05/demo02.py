"""
    [54,25,12,42,35,17]选出最大值
"""

list01 = [54, 25, 12, 42, 35, 17]
max_value = list01[0]
for item in range(1, len(list01)):
    if max_value < list01[item]:
        max_value = list01[item]

print(max_value)