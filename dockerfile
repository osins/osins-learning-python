FROM python:alpine3.17

WORKDIR /working
COPY server.py .

CMD [ "python", "./server.py" ]