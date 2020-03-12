class NoAnsError(Exception):
    """ 表达式有问题或不能解出结果 """
    def __init__(self, value = ""):
        if value == "":
            self.value = "无法解出"

class InputValueError(Exception):
    """ 输入了违法的函数，使用Python内置函数是不允许的 """
    def __init__(self, value = ""):
        if value == "":
            self.value = "输入了不允许的函数！"
        else:
            self.value = value
    def __repr__(self):
        return self.value
    def __str__(self):
        return self.value

def handler_main(error):
    """ 处理错误的主函数 """
    if type(error) == TimeoutError:
        return str({"status":1, "latex":"timeout error"})
    else:
        return str({"status":1, "latex":"error"})
    # if type(error) == InputValueError:
    #     pass