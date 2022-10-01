import re

from latex2mathml.converter import convert as to_mathml
from sympy import latex as to_latex

from ._eval import eval_expr


def format_input(s: str) -> str:
    s = re.sub(r'([0-9]+) {0,}\/ {0,}([0-9]+)', r'\1*x/x/\2', s)
    s = re.sub(r'\^', '**', s)
    s = re.sub(r'([0-9])\(', r'\1*(', s)
    s = re.sub(r'([^a-zA-Z][0-9]+)([a-zA-Z])', r'\1*\2', s)
    s = re.sub(r'\)\(', ')*(', s)
    return s


def compute(content: str) -> dict[str]:
    ans = eval_expr(format_input(content))
    latex = to_latex(ans)
    mathml = to_mathml(latex)
    return {
        'ans': str(ans),
        'latex': latex,
        'mathml': mathml
    }
