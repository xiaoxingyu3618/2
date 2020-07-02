"""
    累加1-100的和
    累加 1-100之间偶数和
    累加10-36之间和
"""

sum_value = 0
for item in range(1,101):
    sum_value += item
print(sum_value)

sum_value = 0
for item in range(2,101,2):
    sum_value += item
print(sum_value)

sum_value = 0
for item in range(10,37):
    sum_value += item
print(sum_value)