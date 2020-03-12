# author : sunzhenxing 
# website: https://github.com/Sun-ZhenXing/
# The core of Visual Math 
# version :1.1.0

from .utils import Functional_Method
from .errorHandler import handler_main
from traceback import print_exc
from eventlet import Timeout,monkey_patch

TimeLimit = 2
# 每次请求的计算时间，VIP特殊服务还没写
DebugMode = True
# 调试模式

monkey_patch()
print("[Msg] Visual Math loading...")
def compute(content, setting="default"):
    try:
        with Timeout(TimeLimit, TimeoutError("Timeout. VIP can compute 25s per time.")):
            jud = content.split(" ")[0]
            if jud in Functional_Method:
                output = Functional_Method[jud][0](jud, content)
            else:
                output = Functional_Method["default"][0](content)
    except Exception as error:
        output = handler_main(error)
        if DebugMode:
            print_exc()
    return output


if __name__ == "__main__":
    print(compute("lim (solve(x^120-pi)+x),x,oo"))
    while True:
        print(compute(input("> ")))