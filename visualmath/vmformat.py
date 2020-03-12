import re
from .errorHandler import InputValueError

def _check_func(string):
    """ 检查输入是否合法 """
    ill_set = ["dict", "help", "setattr", "all", "dir", "next", "slice",
    "any", "divmod", "id", "object", "sorted",
    "ascii", "enumerate", "input", "staticmethod", "bin", "eval", "open",
    "exec", "isinstance", "sum", "bytearray", "filter", "issubclass", "super",
    "bytes", "iter", "print", "callable", "format", "property",
    "chr", "frozenset", "list", "vars", "classmethod", "getattr", "locals",
    "repr", "zip", "compile", "globals", "map", "reversed", "complex",
    "hasattr", "round", "delattr", "hash", "memoryview", "set", "copyright",
    "credits", "license", "exit", "Exception", "quit", "raise",
    "del", "generator", "cmp", "mod"]
    for func in ill_set:
        if re.search(r"\b" + func + r"\b", string):
            raise InputValueError("检测到" + func + \
                "() 函数，这个Python内置函数是不允许的，除非在debug模式中")
    if re.search(r"e[0-9]", string) or re.search(r"E[0-9]", string):
        raise InputValueError("注意：VisualMath 不支持用类似3e5, 5.6E-9 表示数字，这会产生歧义")
    if re.search("_", string):
        raise InputValueError("发现“_”，这是不被允许的，除非使用debug命令")
    return True

def format_main(string):
    """ 格式化输入数据 """
    string0 = re.sub(r"([0-9]+) {0,}\/ {0,}([0-9]+)", r"\1*x/x/\2", string)
    if _check_func(string0):
        string0 = re.sub(r"\^", "**", string0)
        string0 = re.sub(r"([0-9])\(",r"\1*(", string0)
        string0 = re.sub(r"([0-9])([a-zA-Z])", r"\1*\2", string0)
        string0 = re.sub(r"\)\(", ")*(", string0)
    return string0

def format_ans(obj):
    """ 格式化结果，返回字符串，相当于format_main()的逆向操作 """
    string = str(obj).replace("**", "^")
    string0 = re.sub(r"([0-9])\*([a-zA-Z])", r"\1\2", string)
    string0 = re.sub(r"([0-9])\*\(", r"\1\2", string0)
    string0 = re.sub(r"\)\*\(", r"\1\2", string0)
    return string0

def removeJud(jud, content):
    """ 去掉head """
    return re.sub(jud + " ", "", content, 1)

