#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import ssl
from utils import saveImage2File, clearImage

def run():
    addr, port = socket.gethostname(), 12356
    server = ssl.wrap_socket(socket.socket(), 'server.key', 'server.crt', True) # нужен сертификат и ключ
    server.bind((addr, port))
    server.listen()
    conn, addr = server.accept()
    saveImage2File(conn, 'raw_duck.png')
    clearImage('raw_duck.png')
    conn.close()


if __name__ == '__main__':
    run()