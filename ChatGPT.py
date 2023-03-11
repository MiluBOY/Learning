import random

print("欢迎来到猜拳游戏！")
print("请出拳：1 - 石头，2 - 剪刀，3 - 布")

# 玩家出拳
player_choice = int(input())

# 电脑出拳
computer_choice = random.randint(1, 3)

# 判断胜负
if player_choice == computer_choice:
    print("平局！")
elif player_choice == 1 and computer_choice == 2:
    print("你赢了！")
elif player_choice == 2 and computer_choice == 3:
    print("你赢了！")
elif player_choice == 3 and computer_choice == 1:
    print("你赢了！")
else:
    print("你输了！")

print("电脑出的是：", computer_choice)
