import socket
import threading

# 存储客户端 UUID 和数字的字典
client_data = {}

# 定义排序函数
def sort_numbers(numbers):
    return sorted(numbers)

# 处理客户端连接请求
def handle_client(client_socket, address):
    global client_data
    while True:
        try:
            # 接收客户端发送的消息
            data = client_socket.recv(1024).decode()
            if not data:
                break

            # 解析消息中的 UUID 和数字
            uuid, number = data.split(':')

            # 将 UUID 和数字存储到字典中
            client_data[uuid] = int(number)

            # 如果字典中存储了三个不同 UUID 的数字，说明一轮游戏结束
            if len(client_data) == 3:
                # 调用排序函数对数字进行排序
                sorted_numbers = sort_numbers(client_data.values())

                # 将排序后的数字发送给每个客户端
                for client_uuid, client_socket in clients.items():
                    result = ':'.join([client_uuid, str(sorted_numbers)])
                    client_socket.send(result.encode())

                # 清空客户端数据字典
                client_data = {}

        except:
            break

    # 关闭客户端连接
    client_socket.close()

# 监听客户端连接请求
def accept_clients():
    global clients
    while True:
        client_socket, address = server_socket.accept()
        print(f"New connection from {address}")
        # 创建一个新的线程来处理客户端连接
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()

# 主函数
if __name__ == "__main__":
    # 创建 TCP 套接字并绑定 IP 地址和端口号
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 10086))

    # 开始监听连接请求
    server_socket.listen()

    # 等待客户端连接
    clients = {}
    accept_thread = threading.Thread(target=accept_clients)
    accept_thread.start()
    print("service start")
