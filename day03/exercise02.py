"""
    练习：在控制台中获取一个季度（春夏秋冬）
        显示相应的月份
"""

season = input("请输入季节：")

# if season == "春":
#     print("1月、2月、3月")
# if season == "夏":
#     print("4月、5月、6月")
# if season == "秋":
#     print("7月、8月、9月")
# if season == "冬":
#     print("10月、11月、12月")

# 相比上面的代码，具有以上的有点：具有互斥性
if season == "春":
    print("1月、2月、3月")
elif season == "夏":
    print("4月、5月、6月")
elif season == "秋":
    print("7月、8月、9月")
elif season == "冬":
    print("10月、11月、12月")
