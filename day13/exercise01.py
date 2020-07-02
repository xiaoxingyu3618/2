"""
    定义员工管理器
        1.管理所有员工
        2. 计算所有员工工资

    员工：
        程序员：底薪 + 项目分红
        销售：底薪 + 销售额 * 0.05
        软件测试...
        ...

    要求：增加新岗位，员工管理器不变.
"""


class Staffmanager:
    def __init__(self):
        self.__staff = []

    def add_staff(self, staff):
        if isinstance(staff, Staff):
            self.__staff.append(staff)
        else:
            raise ValueError()

    def get_total_salary(self):
        total_salsry = 0
        # 遍历图形列表，累加每个图形的面积
        for item in self.__staff:
            total_salsry += item.calculate_salary()
        return total_salsry


class Staff:
    def __init__(self,basic):
        self.basic = basic

    def calculate_salary(self):
        raise NotImplementedError()


class Programmer(Staff):
    def __init__(self, basic, profile):
        super().__init__(basic)
        self.profile = profile

    def calculate_salary(self):
        return self.basic + self.profile


class Salesman(Staff):
    def __init__(self, basic, sale):
        super().__init__(basic)
        self.sale = sale

    def calculate_salary(self):
        return self.basic + self.sale * 0.05


p1 = Programmer(50, 100)
s1 = Salesman(100, 1000)
m = Staffmanager()
m.add_staff(p1)
m.add_staff(s1)
print(m.get_total_salary())