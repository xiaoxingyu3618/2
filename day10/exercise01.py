class Wife:
    count = 0

    @classmethod
    def print_count(cls):
        print(cls.count)

    def __init__(self, name):
        self.name = name
        Wife.count += 1


w01 = Wife("莉莉")
w02 = Wife("小乔")
w03 = Wife("大乔")
Wife.print_count()
