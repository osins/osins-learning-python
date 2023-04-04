FROM python:alpine3.17

WORKDIR /working
COPY server.py .
RUN pip install flask_socketio eventlet


CMD [ "python", "/working/server.py" ]