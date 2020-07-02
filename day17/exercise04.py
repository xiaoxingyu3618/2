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


# 练习1:获取攻击比例大于6的所有技能
# 要求:使用生成器函数/生成器表达式完成

def get_skill():
    for item in list_skill:
        if item.atk_ratio > 6:
            yield item


re01 = get_skill()
for item in re01:
    print(item)

re02 = (item for item in list_skill if item.atk_ratio > 6)
for item in re02:
    print(item)
