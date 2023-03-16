import time

# 开场白
print("欢迎来到迷失森林！你已经迷失在这个森林里很久了，现在需要尽快找到出口才能逃脱。")

# 定义游戏场景和可行操作
scenes = {
    "开始": {
        "描述": "你站在一个草丛中，周围是茂密的树林。你看到两个方向可以前进，一个是往东，一个是往南。",
        "可行操作": ["向东走", "向南走"]
    },
    "往东走": {
        "描述": "你走进了树林深处，看到一只熊在远处出没。你需要小心避开。",
        "可行操作": ["返回开始", "继续向前"]
    },
    "向南走": {
        "描述": "你走过了一片开阔地，发现一条小溪流过。你需要决定是跟着溪流走还是离开它。",
        "可行操作": ["跟着溪流走", "离开溪流"]
    },
    "跟着溪流走": {
        "描述": "你继续跟着溪流走，一直走到了一个瀑布前。你可以试着爬上去看看。",
        "可行操作": ["返回南边", "爬上瀑布"]
    },
    "离开溪流": {
        "描述": "你离开了溪流，绕过一片危险的沼泽地。现在你来到了一条小路上，可以继续往前走。",
        "可行操作": ["返回南边", "继续前进"]
    },
    "爬上瀑布": {
        "描述": "你成功爬上了瀑布，但你发现前面是一片荒凉的沙漠，无路可走。你只能返回。",
        "可行操作": ["返回瀑布前"]
    },
    "返回开始": {
        "描述": "你返回了草丛中。",
        "可行操作": ["向东走", "向南走"]
    },
    "返回南边": {
        "描述": "你返回了南边。",
        "可行操作": ["跟着溪流走", "离开溪流"]
    },
    "继续前进": {
        "描述": "你走过了一座小山，发现前方有一座古老的城堡。你可以试着进去看看。",
        "可行操作": ["返回路径", "进入城堡"]
    },}