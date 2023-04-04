from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# 存储客户端 UUID 和是否接受邀请的标志位
clients = {}

# 存储客户端 UUID 和数字的字典
client_data = {}

# 定义排序函数


def sort_numbers(numbers):
    return sorted(numbers)

# 处理 WebSocket 连接


@socketio.on('number')
def handle_message(message):
    global clients
    global client_data

    try:
        print("number:", message)

        if ':' not in message:
            return

        uuid, val = message.split(':')

        client_data[uuid] = int(val)

        # 如果字典中存储了三个不同 UUID 的数字，说明一轮游戏结束
        if len(client_data) == 3:
            # 调用排序函数对数字进行排序
            sorted_numbers = sort_numbers(client_data.values())

            # 将排序后的数字发送给每个客户端
            emit('message', sorted_numbers)
                
            # 清空客户端数据字典
            client_data = {}

    except Exception as e:
        print(f"Error: {e}")


@socketio.on('join')
def handle_response(message):
    global clients

    uuid, val = message.split(':')

    print(f"uuid:{uuid}, val:{val}")

    if val == 'y':
        emit('message', "wating")

        # 标记客户端已接受邀请
        clients[uuid] = None

        # 如果所有客户端都接受了邀请，向每个客户端发送请求输入数字的消息
        if all(clients.values()):
            for client_uuid in clients.keys():
                emit('message', 'Please input a number')

    elif val == 'n':
        # 如果客户端拒绝了邀请，则关闭连接
        emit('message', 'You have refused to join the game.')
        socketio.close_room(uuid)

    else:
        # 如果接收到的消息无效，则发送错误提示
        emit('message', 'Invalid message!', room=uuid)


# 监听客户端连接请求
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8000, debug=True)
