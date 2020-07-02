from common.list_helper import *


class SkillData:
    def __init__(self, id, name, atk_ratio, duration):
        self.id = id
        self.name = name
        self.atk_ratio = atk_ratio
        self.duration = duration

    def __str__(self):
        return "技能数据是:%d,%s,%d,%d" % (self.id, self.name, self.atk_ratio, self.duration)


list_skill = [
    SkillData(101, "乾坤大挪移", 5, 10),
    SkillData(102, "降龙十八掌", 8, 5),
    SkillData(103, "葵花宝典", 10, 2),
]


def condition01(item):
    return item.atk_ratio > 6


def condition02(item):
    return 4 < item.duration < 11


def condition03(item):
    return len(item.name) > 4 and item.duration < 6


for item in ListHelper.find_all(list_skill, lambda item: item.atk_ratio > 6):
    print(item)
