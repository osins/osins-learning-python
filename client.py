import socket
import uuid

# 获取客户端的 UUID
client_uuid = str(uuid.uuid4())

# 连接到服务端
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 10086))

# 发送游戏加入请求
print("Do you want to join the game? (y/n)")
answer = input().strip().lower()
if answer == 'n':
    client_socket.close()
    exit()
elif answer == 'y':
    client_socket.send((client_uuid+":join").encode())

def input():
    print("Please enter a number:")
    number = input().strip()
    if not number.isdigit():
        print("Invalid input. Please enter a number.")
    
# 接收用户输入并发送给服务端
while True:
    # 等待服务端的游戏开始通知
    data = client_socket.recv(1024).decode()
    print('recv: ', data)
    
    if data != "start":
        client_socket.close()
        exit()
    
    

    # 将 UUID 和数字用冒号分隔符连接起来，并发送给服务端
