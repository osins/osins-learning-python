import random

# 计算机随机选择选项的函数


def computer_choice():
    # 设置选项（中文翻译：石头、剪刀、布）
    options = ['rock', 'paper', 'scissors']
    # 计算机随机选择一个选项
    return random.choice(options)

# 定义游戏函数


def play_game(user_choice):
    # 计算机随机选择一个选项
    computer = computer_choice()
    # 设置选项描述（中文翻译：石头、剪刀、布）
    desc = {'rock': '石头', 'paper': '剪刀', 'scissors': '布'}
    # 打印出计算机选择的选项
    print("计算机选择了：", desc[computer])
    # 检查游戏结果
    if computer == user_choice:
        print("平局！")
        return "tie"
    elif (computer == 'rock' and user_choice == 'scissors' or
          computer == 'paper' and user_choice == 'rock' or
          computer == 'scissors' and user_choice == 'paper'):
        print("你输了！")
        return "lose"
    else:
        print("你赢了！")
        return "win"


# 无限循环，直到用户选择退出
while True:
    user_choice = input("请选择石头、剪刀或布：")
    result = play_game(user_choice)
    play_again = input("再玩一次？(y/n)")
    if play_again.lower() != 'y':
        break
