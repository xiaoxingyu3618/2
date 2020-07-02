class Enemy:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if 100 <= value <= 200:
            self.__hp = value
        else:
            raise ValueError("我不要")


e01 = Enemy("灭霸", 100, 25)
e01.hp = 150
print(e01.hp)
print(e01.__dict__)
