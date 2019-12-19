import socket


def getSourceIP():
    hostname = socket.gethostname()
    x = socket.gethostbyname(hostname)
    list=[]
    list.append(x)
    return list
