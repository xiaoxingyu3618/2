"""
    学生信息管理系统
"""


class StudentModel:
    """
        学生数据模型
    """

    def __init__(self, name="", age=0, score=0, id=0):
        self.name = name
        self.age = age
        self.score = score
        self.id = id


class StudentManagerController:
    __init_id = 1000

    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        return self.__stu_list

    def add_student(self, stu_info):
        stu_info.id = self.__generate_id()
        self.__stu_list.append(stu_info)

    def __generate_id(self):
        StudentManagerController.__init_id += 1
        return StudentManagerController.__init_id

    def remove_student(self, id):
        for item in self.__stu_list:
            if item.id == id:
                self.__stu_list.remove(item)
                return True
        return False

    def update_student(self, stu_info):
        for item in self.__stu_list:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score

    def order_by_score(self):
        pass


class StudentManagerView:
    """
        学生管理器视图
    """

    def __init__(self):
        self.__maneger = StudentManagerController()

    def __display_menu(self):
        print("1）添加学生")
        print("2）显示学生")
        print("3）删除学生")
        print("4）修改学生")
        print("5）按照成绩升序显示学生")

    def __select_menu_item(self):
        item = input("请输入：")
        if item == "1":
            self.__input_students()
        elif item == "2":
            self.__output_students(self.__maneger.stu_list)
        elif item == "3":
            self.__delete_student()
        elif item == "4":
            self.__modify_student()
        elif item == "5":
            self.__output_student_by_score()

    def main(self):
        """
            界面入口
        :return:
        """
        while True:
            self.__display_menu()
            self.__select_menu_item()

    def __input_students(self):
        name = input("请输入姓名：")
        age = int(input("请输入年龄："))
        score = int(input("请输入成绩："))
        stu = StudentModel(name, age, score)
        self.__maneger.add_student(stu)

    def __output_students(self, list_output):
        for item in list_output:
            print(item.id, item.name, item.age, item.score)

    def __delete_student(self):
        id = int(input("请输入删除的编号"))
        if self.__maneger.remove_student(id):
            print("移除成功")
        else:
            print("移除失败")

    def __modify_student(self):
        id = int(input("请输入需要修改的编号"))
        name = input("请输入姓名：")
        age = int(input("请输入年龄："))
        score = int(input("请输入成绩："))
        stu = StudentModel(name, age, score, id)
        if self.__maneger.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")

    def __output_student_by_score(self):
        self.__maneger.order_by_score()
        self.__output_student_by_score(self.__maneger.__stu_list)

view = StudentManagerView()
view.main()
