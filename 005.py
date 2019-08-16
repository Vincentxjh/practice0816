#第五个练习 - 模拟大乐透号码生成器
from settings import generatnum
print("大乐透号码生成器")
n = int(input("请输入要生成的大乐透号码注数："))
for i in range(n):
    finallist = generatnum.generate_num()
    print("{:0>2d} {:0>2d} {:0>2d} {:0>2d} {:0>2d}     {:0>2d} {:0>2d}".format(finallist[0],finallist[1],finallist[2],finallist[3],finallist[4],finallist[5],finallist[6]))
