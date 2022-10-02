import base64
import os
import re
import tempfile
import uuid

from latex2mathml.converter import convert as to_mathml
from sympy import latex as to_latex
from sympy.plotting.plot import Plot

from ._eval import eval_expr


def format_input(s: str) -> str:
    s = re.sub(r'([0-9]+) {0,}\/ {0,}([0-9]+)', r'\1*x/x/\2', s)
    s = re.sub(r'\^', '**', s)
    s = re.sub(r'([0-9])\(', r'\1*(', s)
    s = re.sub(r'([^a-zA-Z][0-9]+)([a-zA-Z])', r'\1*\2', s)
    s = re.sub(r'\)\(', ')*(', s)
    return s


def compute(content: str) -> dict[str]:
    try:
        ans = eval_expr(format_input(content))
    except Exception as e:
        errmsg = e.args[0]
        return {
            'code': -1,
            'ans': None,
            'msg': 'Error: ' + errmsg,
        }
    graph = None
    if isinstance(ans, Plot):
        with tempfile.TemporaryDirectory() as temp_dir:
            filename = '{}.svg'.format(uuid.uuid4())
            temp_graph = os.path.join(temp_dir, filename)
            ans.save(temp_graph)
            with open(temp_graph, 'rb') as f:
                base64_str = base64.b64encode(f.read()).decode('utf-8')
                graph = 'data:image/svg+xml;base64,' + base64_str
    latex = to_latex(ans)
    mathml = to_mathml(latex)
    return {
        'code': 0,
        'msg': 'ok',
        'ans': str(ans),
        'latex': latex,
        'mathml': mathml,
        'graph': graph
    }
