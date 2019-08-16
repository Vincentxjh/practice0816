#第六个练习 - 模拟春节集五福
from settings import jifu
print("开始集福啦~~~~")
fu = {"爱国福": 0, "富强福": 0, "和谐福": 0, "友善福": 0, "敬业福": 0}
t = True
while t:
    print()
    input("按下<Enter>键获取五福")
    jifu.get_fu()
    jifu.owned_fu(fu)
    t = jifu.judge(fu)
print("\n恭喜您集成五福！！！")

