from latex2mathml.converter import convert as latex_to_mathml
from lxml import etree

__all__ = [
    'latex_to_mathml',
    'mathml_to_omml'
]

OMML_WRAPPER = '<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math"></m:oMathPara>'


def _getXSLT(filename: str):
    xslt = etree.parse(filename)
    return etree.XSLT(xslt)


MML2OMML = _getXSLT('MML2OMML.XSL')


def mathml_to_omml(mathml: str, is_inline=True) -> str:
    if type(mathml) is str:
        output = MML2OMML(etree.fromstring(mathml))
    else:
        output = MML2OMML(mathml)
    if is_inline:
        return etree.tostring(output).decode('utf-8')
    else:
        wrapper = etree.fromstring(OMML_WRAPPER)
        assert isinstance(output, etree._XSLTResultTree)
        wrapper.append(output.getroot())
        return etree.tostring(wrapper).decode('utf-8')
