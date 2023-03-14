import os
import tkinter as tk
from tkinter import filedialog
from pygame import mixer

mixer.init()  # 初始化音频

# 创建窗口
window = tk.Tk()
window.title('音乐播放器')

# 添加标签
label = tk.Label(window, text='请选择要播放的音乐文件')
label.pack()

# 定义函数：选择音乐文件
def choose_file():
    file_path = filedialog.askopenfilename()
    mixer.music.load(file_path)
    label.config(text='正在播放：{}'.format(os.path.basename(file_path)))
    mixer.music.play()

# 添加按钮
button = tk.Button(window, text='选择文件', command=choose_file)
button.pack()

# 运行程序
window.mainloop()
