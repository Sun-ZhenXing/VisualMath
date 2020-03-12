# 自定义方法写在这里
# "method":[func, "summary..."]

from .extend import lim_,latex_,mathml_,default_,solve_,debug_


Functional_Method = {
    "debug":[debug_, " debug"],
    "latex":[latex_, "渲染输入的LaTeX"],
    "lim":[lim_, "求极限"],
    "default":[default_, "默认方法"],
    "solve":[solve_, "解方程"],
    "mathml":[mathml_, "将latex转化为MathML"]
}
