import random
import pygame

# 初始化 pygame
pygame.init()

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 定义屏幕大小和格子大小
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
CELL_SIZE = 20

# 创建屏幕对象
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# 设置窗口标题
pygame.display.set_caption("贪吃蛇游戏")

# 定义贪吃蛇类
class Snake:
    def __init__(self):
        # 初始位置
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        # 初始速度和方向
        self.speed = CELL_SIZE
        self.direction = "right"
        # 初始身体长度和颜色
        self.body = [(self.x, self.y)]
        self.color = GREEN

    # 更新贪吃蛇位置和方向
    def update(self):
        # 根据方向更新位置
        if self.direction == "right":
            self.x += self.speed
        elif self.direction == "left":
            self.x -= self.speed
        elif self.direction == "up":
            self.y -= self.speed
        elif self.direction == "down":
            self.y += self.speed
        # 更新身体
        self.body.insert(0, (self.x, self.y))
        if len(self.body) > 1:
            self.body.pop()

    # 改变方向
    def change_direction(self, direction):
        if direction == "right" and self.direction != "left":
            self.direction = "right"
        elif direction == "left" and self.direction != "right":
            self.direction = "left"
        elif direction == "up" and self.direction != "down":
            self.direction = "up"
        elif direction == "down" and self.direction != "up":
            self.direction = "down"

    # 判断是否吃到食物
    def eat_food(self, food):
        if self.x == food.x and self.y == food.y:
            self.body.append((self.x, self.y))
            return True
        else:
            return False

    # 判断是否碰到边界或身体
    def check_collision(self):
        if self.x < 0 or self.x > SCREEN_WIDTH - CELL_SIZE or self.y < 0 or self.y > SCREEN_HEIGHT - CELL_SIZE:
            return True
        for i in range(1, len(self.body)):
            if self.body[i] == (self.x, self.y):
                return True
        return False

    # 绘制贪吃蛇
    def draw(self):
        for x, y in self.body:
            pygame.draw.rect(screen, self.color, [x, y, CELL_SIZE, CELL_SIZE])

# 定义食物类
class Food:
    def __init__(self):
        # 随机位置
        self.x = random.randrange(0, SCREEN_WIDTH // CELL_SIZE) * CELL_SIZE
        self.y = random.randrange(0, SCREEN_HEIGHT // CELL_SIZE) * CELL_SIZE
