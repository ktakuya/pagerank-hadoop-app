FROM golang:latest
MAINTAINER ktakuya

ADD . /go/src/github.com/ktakuya/vote-app

RUN go get code.google.com/p/go.net/websocket
RUN go get github.com/garyburd/redigo/redis
RUN go install github.com/ktakuya/vote-app

# Copy static files
RUN cp -r /go/src/github.com/ktakuya/vote-app/public /go/bin/public
RUN cp -r /go/src/github.com/ktakuya/vote-app/data /go/bin/data

ENTRYPOINT /go/bin/vote-app
WORKDIR /go/bin

EXPOSE 80
