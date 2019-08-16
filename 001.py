#第一个练习 - 导入两个模块（分别是 rect.py 和 circ.py）计算周长和面积
#由于rect.py和circ.py这个两个模块中有同名函数，因此只能用import导入，而不能使用from……import导入
import rect
import circ
print("长为10，宽为5的矩形的周长为 {} 厘米，面积为 {} 平方厘米。".format(rect.girth(10, 5), rect.area(10, 5)))
print("半径5的圆的周长为{: .2f} 厘米，面积为{: .2f} 平方厘米。".format(circ.girth(5), circ.area(5)))