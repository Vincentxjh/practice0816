#创建一个模块，用于模拟集五福过程（练习六006.py使用）
import random

def get_fu():
    fus = ("爱国福", "富强福", "和谐福", "友善福", "敬业福")
    global get
    get = random.sample(fus, 1)
    print("获取到：", get[0])

def owned_fu(fu_dict):
    fu_dict[get[0]] += 1
    print("当前拥有的福：")
    for key,value in fu_dict.items():
        print(key, ":", value, end="    ")
    print()

def judge(fu_dict):
    judge = False
    for i,j in fu_dict.items():
        if j == 0:
            judge = True
    return judge