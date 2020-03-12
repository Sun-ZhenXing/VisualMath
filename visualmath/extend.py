from .vmformat import format_main, format_ans, removeJud
from ._eval import EVAL, latex as Latex
from latex2mathml import converter
toMathML = converter.convert
debugPassword = "876rfbjugfde45678iko09865wsdfg"


def lim_(jud, exp):
    """
    求极限
    ======
    ## >lim f(x),x,oo
    这只是方法，不允许在表达式的其他地方出现
    比如
    #### lim (lim f(x),x,pi),x,0
    后面可能会允许这种方法
    """
    assert jud == "lim"
    expr = format_main(removeJud(jud, exp))
    val = EVAL(f"limit({expr})")
    myLatex = Latex(val)
    try:
        mathml = toMathML(myLatex)
    except:
        mathml = "ERROR"
    return str({"status": 0, "value": str(val), "latex": myLatex, "MathML":mathml})

def latex_(jud, exp):
    """
    展示LaTeX
    ========
    ## latex str
    """
    assert jud == "latex"
    expr = removeJud(jud, exp)
    myLatex = Latex(expr)
    return str({"status": 0, "value": 0, "latex": myLatex, "MathML":0})

def mathml_(jud, exp):
    """
    显示MathML
    ==========
    ## mathml latex_str
    """
    assert jud == "mathml"
    expr = toMathML(removeJud(jud, exp))
    return str({"status": 0, "value": str(val), "latex": expr, "MathML":expr})

def default_(exp):
    """
    默认方法，直接计算
    =======
    """
    expr = format_main(exp)
    val = EVAL(expr)
    myLatex = Latex(val)
    try:
        mathml = toMathML(myLatex)
    except:
        mathml = "ERROR"
    return str({"status": 0, "value": str(val), "latex": myLatex, "MathML":mathml})

def debug_(jud, exp):
    """
    仅限调试
    =========
    ## debug cmd password
    """
    assert jud == "debug"
    password = exp.split(" ")[-1]
    if password == debugPassword:
        cmd = removeJud("debug",exp).replace(" " + password, "")
        print("eval ", cmd)
        eval(cmd)

def solve_(jud, exp):
    """
    解方程
    ===============
    ## solve expr, [x,y,...]
    """
    assert jud == "solve"
    expr = format_main(removeJud(jud, exp))
    val = EVAL(f"solve({expr})")
    myLatex = Latex(val)
    try:
        mathml = toMathML(myLatex)
    except:
        mathml = "ERROR"
    return str({"status": 0, "value": str(val), "latex": myLatex, "MathML":mathml})
