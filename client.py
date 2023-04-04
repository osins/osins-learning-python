import socketio
import uuid

uuid = uuid.uuid4()
sio = socketio.Client()

# 定义连接成功事件处理函数


@sio.event
def connect():
    global uuid
    print('Connected to server.')
    sio.emit('login', f"{uuid}")

# 定义邀请消息事件处理函数


@sio.on('invite')
def handle_invite(message):
    print(message)
    response = input()

    # 向服务器发送回复消息
    sio.emit('join', f"{uuid}:{response}")

# 定义服务器发送的消息事件处理函数


@sio.on('message')
def handle_message(message):
    print('message: ', message)

    if ':' not in message:
        return

    uuid, op, val = message.split(':')

    if op == 'input':
        # 如果服务器发送的消息为请求输入数字的消息，则提示用户输入数字
        number = int(input(val))
        sio.emit('message', f"{uuid}:in:{number}")

    elif op == 'result':
        # 如果服务器发送的消息为本轮游戏排序结果，则输出结果
        print(f"The sorted numbers are: {val}")

# 定义连接错误事件处理函数


@sio.event
def connect_error():
    print("Connection failed.")

# 定义连接断开事件处理函数


@sio.event
def disconnect():
    print("Disconnected.")


if __name__ == '__main__':
    # 连接服务器
    sio.connect('http://localhost:10086')

    # 等待连接成功
    sio.wait()
