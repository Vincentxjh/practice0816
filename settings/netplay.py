#此模块用于统计上网时长（练习七007.py使用）
def surf_web(time):
    print("浏览网页 ", time, "小时")
    return time
def watch_videos(time):
    print("看视频 ", time, "小时")
    return time
def play_games(time):
    print("玩游戏 ", time, "小时")
    return time
def study(time):
    print("学习 ", time, "小时")
    return time
def total_times(time):
    if time >= 8:
       print("今天上网时间共计", time, "小时，请保护眼睛，合理安排上网时间！")
    return time