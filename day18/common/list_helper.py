"""
    列表助手模块
"""


class ListHelper:
    """
        列表助手类
    """

    @staticmethod
    def find_all(list_target, func_condition):
        """
            通用的查找某个条件的所有元素方法
        :param list_target: 需要查找的列表
        :param func_condition: 需要查找的条件,函数类型
                函数名(参数) --> bool
        :return: 需要查找的元素,生成器类型.
        """
        for item in list_target:
            if func_condition(item):
                yield item

    @staticmethod
    def find_single(list_target, func_condition):
        """
            通用的查找某个条件的单个元素方法
        :param list_target: 需要查找的列表
        :param func_condition: 需要查找的条件,函数类型
                函数名(参数) --> bool
        :return: 需要查找的元素
        """
        for item in list_target:
            if func_condition(item):
                return item

    @staticmethod
    def get_count(list_target, func_duration):
        """
               通用的计算满足某个条件的元素数量方法
           :param list_target: 需要查找的列表
           :param func_condition: 需要查找的条件,函数类型
                   函数名(参数) --> bool
           :return: 满足条件元素的数量
        """
        count_value = 0
        for item in list_target:
            if func_duration(item):
                count_value += 1
        return count_value

    @staticmethod
    def is_exists(list_target, func_condition):
        """
                      通用的判断是否存在某个元素
                  :param list_target: 需要查找的列表
                  :param func_condition: 需要查找的条件,函数类型
                          函数名(参数) --> bool
                  :return: True False
               """
        for item in list_target:
            if func_condition(item):
                return True
        return False

    @staticmethod
    def sum(list_target, fun_condition):
        total_value = 0
        for item in list_target:
            total_value += fun_condition(item)
        return total_value

    @staticmethod
    def select(list_target, fun_condition):
        result_list = []
        for item in list_target:
            result_list.append(fun_condition(item))
        return result_list

    @staticmethod
    def get_max(list_target, fun_condition):
        max_result = list_target[0]
        for item in list_target:
            if fun_condition(item) > fun_condition(max_result):
                max_result = item
        return max_result

    @staticmethod
    def ascending_order(list_target, fun_condition):
        for i in range(len(list_target) - 1):
            for c in range(i + 1, len(list_target)):
                if fun_condition(list_target[i]) > fun_condition(list_target[c]):
                    list_target[i], list_target[c] = list_target[c], list_target[i]
