

season = input("请输入季度：")
while True:
    if season == "春":
        print("1月、2月、3月")
    elif season == "夏":
        print("4月、5月、6月")
    elif season == "秋":
        print("7月、8月、9月")
    elif season == "冬":
        print("10月、11月、12月")
    elif input("输入e键退出") == "e":
        break