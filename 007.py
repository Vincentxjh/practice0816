#第七个练习 - 封装用户的上网行为
from settings import netplay
name = "小明"
print(name, "上网时间、行为统计：")
time = 0
time += netplay.surf_web(1.5)
time += netplay.watch_videos(2)
time += netplay.play_games(3)
time += netplay.study(2)
netplay.total_times(time)
