import socket
from utils import sendImage, saveImage2File, greaseImage

def listenClient(addr: str, port: str):
    interseptor = socket.socket()
    interseptor.bind((addr, port))
    interseptor.listen()
    conn, addr = interseptor.accept()
    saveImage2File(conn, 'duck_interseptor.png')
    conn.close()
    interseptor.close()

def run():
    addr, client_port, server_port = socket.gethostname(), 12345, 12356
    
    listenClient(addr, client_port)
    interseptor = socket.socket() # подключиться не получится, т.к соединение защищено
    greaseImage('duck_interseptor.png', 0.1)
    interseptor.connect((addr, server_port))
    sendImage(interseptor,'noisy_duck.png')
    interseptor.close()

if __name__=='__main__':
    run()