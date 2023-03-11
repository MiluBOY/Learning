import random

print("欢迎来到猜数字游戏！")
print("请输入一个1到100之间的整数：")

# 随机生成一个1到100之间的整数
answer = random.randint(1, 100)

# 循环猜数字
while True:
    # 玩家输入猜测的数字
    guess = int(input())

    # 判断猜测的数字与答案的大小关系
    if guess > answer:
        print("猜大了，再试试吧！")
    elif guess < answer:
        print("猜小了，再试试吧！")
    else:
        print("恭喜你，猜对了！")
        break
