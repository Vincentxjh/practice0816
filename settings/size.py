#创建一个模块，用于获取宽度和高度（练习三003.py使用）
_width = 800
_heigth = 600
def change(w, h):
    global _width
    global _heigth
    _width = w
    _heigth = h
def getWidth():
    return _width
def geiHeigth():
    return  _heigth