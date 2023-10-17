import base64
import os
import re
import tempfile
import uuid
from typing import Any

from sympy import Expr
from sympy import latex as to_latex
from sympy.plotting.plot import Plot

from visualmath._eval import eval_expr
from visualmath.utils import latex_to_mathml, mathml_to_omml


def format_input(s: str) -> str:
    s = re.sub(r"([0-9]+) {0,}\/ {0,}([0-9]+)", r"\1*x/x/\2", s)
    s = re.sub(r"\^", "**", s)
    s = re.sub(r"([0-9])\(", r"\1*(", s)
    s = re.sub(r"([^a-zA-Z][0-9]+)([a-zA-Z])", r"\1*\2", s)
    s = re.sub(r"^([0-9]+)([a-zA-Z])", r"\1*\2", s)
    return s


class Component:
    def __init__(self, expr: Expr) -> None:
        if type(self) is __class__:
            raise NotImplementedError
        self._expr = expr

    def accept(self) -> bool:
        ...

    def to_dict(self) -> dict:
        ...


class Basic(Component):
    def accept(self) -> bool:
        return True

    def to_dict(self) -> dict:
        latex = to_latex(self._expr)
        mathml = latex_to_mathml(latex)
        try:
            omml = mathml_to_omml(mathml)
        except:
            omml = "Error when convert!"
        return {"expr": str(self._expr), "mathml": mathml, "latex": latex, "omml": omml}


class Graph(Component):
    def accept(self) -> bool:
        return isinstance(self._expr, Plot)

    def to_dict(self) -> dict:
        graph = None
        if isinstance(self._expr, Plot):
            with tempfile.TemporaryDirectory() as temp_dir:
                filename = "{}.svg".format(uuid.uuid4())
                temp_graph = os.path.join(temp_dir, filename)
                self._expr.save(temp_graph)
                with open(temp_graph, "rb") as f:
                    base64_str = base64.b64encode(f.read()).decode("utf-8")
                    graph = (
                        '<img src="data:image/svg+xml;base64,{}" alt="graph" />'.format(
                            base64_str
                        )
                    )
        return {"graph": graph}


def router(expr: str, context: dict | None = None) -> dict:
    res = {"code": 0, "msg": "ok", "data": []}
    try:
        ans = eval_expr(format_input(expr))
    except Exception as e:
        print(e.args)
        errmsg = "Error: " + e.args[0]
        res["code"] = -1
        res["msg"] = errmsg
        return res
    for c in [Basic, Graph]:
        component: Component = c(ans)
        if component.accept():
            d = component.to_dict()
            d["component"] = component.__class__.__name__
            res["data"].append(d)
    return res
