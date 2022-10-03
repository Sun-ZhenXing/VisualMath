from random import random as rnd

from sympy import *
from sympy.abc import *
from sympy.liealgebras import *
from sympy.plotting import *

f, g, h = Function('f'), Function('g'), Function('h')

_ClassRegistry = C
C = symbols('C')

assert rnd, _ClassRegistry


globals_ = globals().copy()
globals_['__builtins__'] = {}


def eval_expr(__s: str):
    assert len(__s) < 256, 'expr too long, no more than 256'
    assert '__' not in __s, '"__" should not exist in expr'
    return eval(__s, globals_, {})
