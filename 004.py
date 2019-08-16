#第四个练习 - 生成由数字、字母组成的4位验证码(区分大小写)
import random
checklist = ""
for i in range(4):
    index = random.randint(0,4)
    if index == 0:
        checklist += str(random.randint(0, 9))
    elif index == 1:
        checklist += chr(random.randint(97, 122))
    elif index == 2:
        checklist += chr(random.randint(65, 90))
    else:
        checklist += chr(random.randint(97, 122))
print("验证码：" + checklist)

#也可写成
import random
checklist = ""
for i in range(4):
    index = random.randint(0,4)
    if index ==i:
        checklist += str(random.randint(0, 9))
    elif index + 1 == i:
        checklist += chr(random.randint(65, 90))
    else:
        checklist += chr(random.randint(97, 122))
print("验证码：" + checklist)
