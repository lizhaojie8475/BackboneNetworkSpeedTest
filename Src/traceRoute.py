#coding=utf-8
import os
from functions import read_json

from functions import getip


def tracert(Sip):  # 函数参数是ip地址
    f = os.popen('traceroute -n -m 15 -q 1 -w 3 %s' % (Sip))  # -n命令取消将ip地址解析为主机名的操作，加快跟踪速度

    # 将cmd窗口显示的文字信息写入txt文件，再从文件中逐行筛选、呈现
    file = open('/home/data/tracert/%s tracert.txt' % (Sip), 'w')
    file.write(f.read())
    file.close()
    file = open('/home/data/tracert/%s tracert.txt' % (Sip), "r")
    #file = file.read()

    points = []  # 存放跟踪目标ip所经过的跃点、次数
    ipList = []  # 存放经过的ip
    list1 = []

    for line in file:  # 产生元素为字典的列表和元素为ip的列表
        flag1 = line.find('*')
        flag2 = line.find('ms')
        if flag1 == -1 and flag2 != -1:
            ip = getip(line)[0]
            if ip[0:2] != '11':
                dic = {}
                dic.update({ip: 1})
                points.append(dic)
                ipList.append(ip)
    #print(points)
    if os.path.exists('/home/data/json/%s.json' % Sip):
        list1 = read_json(Sip)[4]
        #print(list1)
        for i in range(0, len(ipList)):
            hasFound = 0
            k = ipList[i]
            for c in list1:
                if k in c:
                    c[k] = c[k] + 1
                    hasFound = 1
            if hasFound == 0:
                dic = {}
                dic.update({k: 1})
                points.append(dic)
        points = list1
    #print(ipList)
    #print(read_json(ip)[4])

    #print(points)
    file.close()
    return points
