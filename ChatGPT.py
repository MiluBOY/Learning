def init_board(board_size):
    # 初始化棋盘
    board = []
    for i in range(board_size):
        row = [0] * board_size
        board.append(row)
    return board

def print_board(board):
    # 打印棋盘
    board_size = len(board)
    for i in range(board_size):
        print(board[i])

def check_win(board, player):
    # 检查是否有五子连珠
    board_size = len(board)
    for i in range(board_size):
        for j in range(board_size):
            if j + 4 < board_size and board[i][j]==player and board[i][j+1]==player and board[i][j+2]==player and board[i][j+3]==player and board[i][j+4]==player:
                return True
            elif i + 4 < board_size and board[i][j]==player and board[i+1][j]==player and board[i+2][j]==player and board[i+3][j]==player and board[i+4][j]==player:
                return True
            elif i + 4 < board_size and j + 4 < board_size and board[i][j]==player and board[i+1][j+1]==player and board[i+2][j+2]==player and board[i+3][j+3]==player and board[i+4][j+4]==player:
                return True
            elif i >=4 and j + 4 < board_size and board[i][j]==player and board[i-1][j+1]==player and board[i-2][j+2]==player and board[i-3][j+3]==player and board[i-4][j+4]==player:
                return True
    return False

def play():
    # 开始游戏
    board_size = 15
    board = init_board(board_size)
    player = 1
    while True:
        print_board(board)
        print("当前玩家：{}".format(player))
        x = int(input("请输入行号："))
        y = int(input("请输入列号："))
        if board[x][y] != 0:
            print("该坐标已经有棋子，请重新输入！")
            continue
        board[x][y] = player
        if check_win(board, player):
            print_board(board)
            print("玩家{}获胜！".format(player))
            break
        player = 2 if player == 1 else 1
        print("----------------------------")

if __name__ == '__main__':
    play()