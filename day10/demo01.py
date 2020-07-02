class Student:
    def __init__(self, name, age, score, sex):
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex

    def print_self_info(self):
        print("%s的年龄是%d，成绩是%d,性别是%s" % (self.name, self.age, self.score))


list01 = [
    Student("赵敏", 28, 100, "女"),
    Student("苏大强", 68, 62, "男"),
    Student("明玉", 30, 95, "女"),
    Student("张无忌", 29, 70, "男"),
]


def find01():
    result = []
    for item in list01:
        if item.sex == "女":
            result.append(item)
    return result
