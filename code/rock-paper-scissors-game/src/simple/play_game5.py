import random

# 设置选项及其描述（中文翻译：石头、剪刀、布）
options = {'rock': '石头', 'paper': '剪刀', 'scissors': '布'}

# 可以获胜的情况
win_cases = [('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper')]

options_enumerate = enumerate(options.items())
options_keys = list(options.keys())

# 计算机随机选择选项的函数


def computer_choice():
    # 计算机随机选择一个选项
    computer_choice = random.choice(list(options.keys()))
    # 打印出计算机选择的选项
    print("计算机选择了：", computer_choice)
    return computer_choice

# 判断游戏结果的函数


def check_result(computer, user_choice):
    # 判断游戏结果
    if computer == user_choice:
        return "tie(平)"
    elif (computer, user_choice) in win_cases:
        return "win(赢)"
    else:
        return "lose(输)"

# 等待用户输入选项的函数


def get_user_choice():
    # 等待用户输入选项
    options_prompt = "、".join(
        [f"{index+1}:({desc}|{name})" for index, (name, desc) in options_enumerate])
    user_choice_index = int(input(f"请选择{options_prompt}："))
    # 获取用户选择的选项
    user_choice = options_keys[user_choice_index-1]
    print("好的,您的选择是：", user_choice)
    return user_choice

# 定义游戏函数


def play_game():
    user_choice = get_user_choice()
    computer = computer_choice()
    # 检查游戏结果并打印输出
    result = check_result(computer, user_choice)
    print(result)


# 无限循环，直到用户选择退出
while True:
    play_game()
    play_again = input("再玩一次？(y/n)")
    if play_again.lower() != 'y':
        break
