#创建一个模块，用于模拟大乐透号码生成器(练习五005.py使用)
import random
def generate_num():
    list = [i for i in range(1,36)]
    frontlist = random.sample(list, 5)
    list = [i for i in range(1,13)]
    backlist = random.sample(list, 2)
    frontlist.sort()
    backlist.sort()
    finallist = frontlist + backlist
    return  finallist