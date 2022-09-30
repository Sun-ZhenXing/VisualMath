from random import random as rnd

from sympy.abc import *
from sympy import *

f, g, h = Function('f'), Function('g'), Function('h')

_ClassRegistry = C
C = symbols('C')

assert rnd, _ClassRegistry


def eval_expr(s: str):
    return eval(s)
