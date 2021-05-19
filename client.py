#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import ssl
from utils import sendImage
import logging

def run():
    client = ssl.wrap_socket(socket.socket())
    addr, port = socket.gethostname(), 12345
    client.connect((addr,port))
    sendImage(client, 'duck.png')
    client.close()

if __name__ == '__main__':
    run()