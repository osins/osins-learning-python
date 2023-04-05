import random

# 定义游戏函数


def play_game(user_choice):
    # 设置选项（中文翻译：石头、剪刀、布）
    options = ['rock', 'paper', 'scissors']
    descs = ['石头', '剪刀', '布']
    # 计算机随机选择一个选项
    computer_choice = random.choice(options)
    # 打印出计算机选择的选项
    print("计算机选择了：", computer_choice.split('(')[0])
    # 检查游戏结果
    if computer_choice == user_choice:
        print("平局！")
        return "tie"
    elif (computer_choice == 'rock' and user_choice == 'scissors' or
          computer_choice == 'paper' and user_choice == 'rock' or
          computer_choice == 'scissors' and user_choice == 'paper'):
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
