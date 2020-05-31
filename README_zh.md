# VisualMath
基于Sympy的数学计算服务

强烈推荐看一下介绍：https://sun-zhenxing.gitee.io/myblog/pages/visualmath.html

开源数学计算服务框架

简洁易用，是一个不错的小工具，摆脱了DOS下sympy只能看见字符，看不到数学公式的烦恼
## 支持
目前支持SymPy内的方法基本都可以调用，还可能加入绘图、伪代码、机器证明等
## 本项目是基于一些框架
```
katex 最快的网络排版库
layui 是一款简洁易用的网页框架
flask 服务器框架
jQuery 所有网页逻辑都是jq写的
```
## 依赖
版本要求：python3.x | 其他最新即可

```
pip install sympy
pip install flask
pip install latex2mathml
```
## 下载到计算机
直接打包下载即可，不需要额外操作

或者git clone到电脑
## 使用方法
直接运行 flask_server.py 即可

在 utils.py 中可以修改参数、自定义方法

默认监听自身ip

打开浏览器输入 http://ip:3389/
## 许可证
本项目采用CC-BY-NC-SA 4.0 许可证发布（署名—非商业性使用—相同方式共享 4.0 协议国际公共许可证），简称为 CC BY-SA 4.0

我没有将licenses放在项目库中，这并不表示您不必遵守这些协议。您如果需要协议以外的授权，请与我联系。

