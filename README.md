# VisualMath

![](images/2022-10-02-10-16-15.png)

![](images/2022-09-30-19-39-18.png)

![](images/2022-09-30-19-24-55.png)

Sympy-based mathematical computing services.

Framework for Open Source Mathematical Computing Services.

Simple and easy to use, it is a nice little tool to get rid of the DOS sympy can only see characters, not see the trouble of mathematical equations.

The methods currently supported within SymPy are basically callable.

基于 Sympy 的数学计算服务，基于开源数学计算服务框架。

简洁易用，是一个不错的小工具，摆脱了 DOS 下 Sympy 只能看见字符，看不到数学公式的烦恼。

目前支持 SymPy 内的方法基本都可以调用，因为完全就是封装了一层网页而已。

## Usage | 使用方法

```bash
git clone https://github.com/Sun-ZhenXing/VisualMath
cd VisualMath
pip install -r requirements.txt
python sanic_server.py
```

If you need to support drawing, you can install `matplotlib`. If you need a real-time GUI, you can comment the following code.

如果需要支持绘图，可以安装 `matplotlib`，如果需要实时 GUI，可以注释下面这一句：

```python
# sanic_server.py line 2
matplotlib.use('agg')
```

Open: <http://127.0.0.1:3389/>

## License | 许可证

MIT.
