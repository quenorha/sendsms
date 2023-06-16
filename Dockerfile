FROM python:3-alpine

WORKDIR /usr/src/app

RUN pip3 install pyserial

COPY . .

ENTRYPOINT [ "python","-u", "sendsms.py" ]
