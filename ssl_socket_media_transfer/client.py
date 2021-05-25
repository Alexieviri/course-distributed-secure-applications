#!/usr/bin/env python
# -*- coding: utf-8 -*-

from socket import * 
from ssl import *
from utils import saveImage2File, sendImage
import os 

path = 'example.jpg'
def run(ssl:bool):
    addr, port = gethostname(), 46626
    client = socket(AF_INET, SOCK_STREAM)
    if ssl:
        client = wrap_socket(socket(AF_INET, SOCK_STREAM), 'key.pem', 'cert.pem', ssl_version=PROTOCOL_TLSv1)
        port = 46626  
    client.connect((addr,port))
    sendImage(client,path)
    client.close()

if __name__ == '__main__':
    run(True)