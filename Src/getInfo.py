from ping import ping
from traceRoute import tracert
from sourceip import getSourceIP
from functions import write_json, read_json

def getInfo(ip):
    v1 = ping(ip)
    v1.append(tracert(ip))
    list = [getSourceIP() + v1]
    return getSourceIP() + v1  # 返回一个列表
