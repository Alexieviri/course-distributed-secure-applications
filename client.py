#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import * 
from ssl import *
from utils import sendImage
import os 

path = 'example.jpg'
def run(ssl:bool):
    addr, port = gethostname(), 12345
    if ssl:
        client = wrap_socket(socket(AF_INET, SOCK_STREAM), 'server.key', 'server.crt', False)
        port = 12356
    else:
        client = socket(AF_INET, SOCK_STREAM)
    client.connect((addr,port))
    sendImage(client,path)
    client.close()

if __name__ == '__main__':
    run(True)