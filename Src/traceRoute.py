#coding=utf-8
import os
from functions import read_json
from functions import getip


def tracert(Sip):  # 函数参数是ip地址
    outputText = os.popen('traceroute -n -m 15 -q 1 -w 2 %s' % (Sip,)).read()  # -n命令取消将ip地址解析为主机名的操作，加快跟踪速度

    points = []  # 存放跟踪目标ip所经过的跃点、次数
    ipList = []  # 存放经过的ip
    list1 = []

    ipList = getip(outputText)
    ipList = filter(lambda ip: not ip.startswith("11."), ipList)
    ipList = list(ipList)

    return ipList
