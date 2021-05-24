#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import *
from ssl import *
from utils import saveImage2File, clearImage
path = 'server-example.jpg'
def run(ssl:bool):
    addr, port = gethostname(), 46625
    if ssl:
        server = wrap_socket(socket(AF_INET, SOCK_STREAM), 'server.key', 'server.crt')
    else:
        server = socket(AF_INET, SOCK_STREAM)
    server.bind((addr, port))
    server.listen()
    conn, addr = server.accept()
    saveImage2File(conn, path)
    clearImage(path)
    conn.close()


if __name__ == '__main__':
    run(False)