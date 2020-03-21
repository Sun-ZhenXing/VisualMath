ErrorDict = {
    SyntaxError :"语法错误",
    OverflowError :"数值过大溢出",
    AttributeError :"对象不存在属性",
    EOFError :"还未结束语句|没有内建输入",
    ZeroDivisionError:"您不应该用一个数除以0，那样没有意义",
    IndexError:"序列中没有对应索引",
    NameError:"本地变量没有初始化",
    TypeError:"无效类型",
    ValueError:"传入给函数的参数无效",
    KeyError:"没有键与之对应"
}
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

def handler_main(error, exc_info):
    """ 处理错误的主函数 """
    relist = {"status":1, "latex":"ERROR",}
    if type(error) in ErrorDict:
        relist["errorMsg"] = ErrorDict[type(error)] + f" @错误源：{type(error).__name__}: {exc_info[1]}"
    else:
        relist["errorMsg"] = "未发现错误内容信息" + f" @错误源：{type(error).__name__}: {exc_info[1]}"
    return str(relist)
