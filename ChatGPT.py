while True:
    # 用户输入
    expression = input('请输入要计算的表达式（例如：1+2）：')

    # 分割表达式
    operator_list = ['+', '-', '*', '/']
    operator = None
    for op in operator_list:
        if op in expression:
            operator = op
            break
    if not operator:
        print('输入错误，请重新输入！')
        continue
    num1, num2 = expression.split(operator)
    num1 = float(num1.strip())
    num2 = float(num2.strip())

    # 计算结果
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print('除数不能为0，请重新输入！')
            continue
        result = num1 / num2

    # 输出结果
    print('结果为：{}'.format(result))
