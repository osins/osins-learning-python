import random

# 定义游戏函数


def play_game():
    # 设置选项（中文翻译：石头、剪刀、布）
    options = ['rock', 'paper', 'scissors']
    descs = ['石头', '剪刀', '布']
    # 计算机随机选择一个选项
    computer_choice = random.choice(options)
    # 等待用户输入选项
    user_choice = input(
        f"Choose {options[0]}({descs[0]}), {options[1]}({descs[0]}), or {options[2]}({descs[0]}): ")
    # 打印出计算机选择的选项
    print("Computer chose", computer_choice, "（计算机选择了",
          computer_choice.split('(')[0], "）")
    # 检查游戏结果
    if computer_choice == user_choice:
        print("Tie! （平局）")
    elif (computer_choice == 'rock' and user_choice == 'scissors' or
          computer_choice == 'paper' and user_choice == 'rock' or
          computer_choice == 'scissors' and user_choice == 'paper'):
        print("You lose! （你输了）")
    else:
        print("You win! （你赢了）")


# 无限循环，直到用户选择退出
while True:
    play_game()  # 调用游戏函数
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != 'y':
        break
