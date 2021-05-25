import socket
from utils import sendImage, saveImage2File, greaseImage
path = 'interseptor-example.jpg'
def listenClient(addr: str, port: str):
    interseptor = socket.socket()
    interseptor.bind((addr, port))
    interseptor.listen()
    conn, addr = interseptor.accept()
    saveImage2File(conn, path)
    conn.close()
    interseptor.close()

def run():
    addr, client_port, server_port = socket.gethostname(), 46626, 46625
    
    listenClient(addr, client_port)
    interseptor = socket.socket() # подключиться не получится, т.к соединение защищено
    greaseImage(path, 0.1)
    interseptor.connect((addr, server_port))
    sendImage(interseptor,path)
    interseptor.close()

if __name__=='__main__':
    run()