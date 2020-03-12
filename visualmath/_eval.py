# 设计目标
# 例：令牌解析
# text = 'foo = 23 + 42 * 10'
# 为了令牌化字符串，你不仅需要匹配模式，还得指定模式的类型。比如，你可能想
# 将字符串像下面这样转换为序列对：
# tokens = [('NAME', 'foo'), ('EQ','='), ('NUM', '23'), ('PLUS','+'),
# ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]
# 现在要求是解析以下对象：

# 抗歧义语法
# (,)	向量|坐标|区间
# [,]	列表|区间
# [,)	区间

# 语法补全
# ( ... / ...)(... => (...)

# 方程解析
# exp1 = exp2 => Eq(exp1, exp2) || exp1 - (exp2)

# 空格语法
# lim[+-] x [:,;] x [,->=>] [+oo,-oo,0,a][+-] 极限表达式
# sin x	=> sin(x) 遇到第一个非乘性运算符结束
# ln x^3*5 + 7 => ln(x^3*5) + 7 => ln(x**3*5) + 7
# tan 3r/23*I/pi + 4 => tan(3*r/23*I/pi)

# $ 生成配置
# 部分交给JavaScript处理
# $.use("模板文件")
# $.a = exp1
# $.sin2(x) 自定义函数设置
# $.m(x) [:|= ] x^3+5x-12
# $.setmod("mod", value)
# $.autov = True
# 运行使用i，e表示I，E
# $.debug = False
# $.vector = True
# 将数组解析为向量
# $.ind = False
# $.coor = False
# $.圆锥曲线 = True

# 预览
# LaTeX:

from sympy.abc import *
from sympy import *
plot = "Please go to plotting."
f,g,h = Function("f"), Function("g"), Function("h")

def EVAL(string):
	# return eval(string, _Globals, _Locals)
	# eval 安全性待测试
	return eval(string)



