#创建一个模块，(练习二002.py使用)
pinetree = "我是一颗松树"
def fun_dream():
    '''
    功能：一个梦
    无返回值
    '''
    pinetree = "孩子们为我挂上了彩灯、礼物……我变成了一颗圣诞树 ^_^ \n"
    print(pinetree)
#调用函数
if __name__ == '__main__':
    print("下雪了……\n")
    print("========进入了梦乡========\n")
    fun_dream()
    print("==========梦醒了==========\n")
    pinetree = "我身上落满雪花，" + pinetree + "-_-"
    print(pinetree)