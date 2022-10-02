from random import random as rnd

from sympy.abc import *
from sympy.plotting import *
from sympy.liealgebras import *
from sympy import *

f, g, h = Function('f'), Function('g'), Function('h')

_ClassRegistry = C
C = symbols('C')

assert rnd, _ClassRegistry


globals_ = globals().copy()
globals_['__builtins__'] = {}

def eval_expr(__s: str):
    assert len(__s) < 300
    return eval(__s, globals_)
