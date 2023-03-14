import tkinter as tk

# 创建窗口
window = tk.Tk()
window.title('交互面板')

# 添加标签
label = tk.Label(window, text='请输入一个数值')
label.pack()

# 添加输入框
entry = tk.Entry(window)
entry.pack()

# 定义计算函数
def calculate():
    value = float(entry.get())
    result = value ** 2
    label.config(text='结果：{}'.format(result))

# 添加按钮
button = tk.Button(window, text='计算', command=calculate)
button.pack()

# 运行程序
window.mainloop()
