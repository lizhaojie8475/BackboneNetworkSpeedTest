import os
from functions import get_int_after
from threading import Thread


def ping(ip):  # 函数参数是ip地址
    f = os.popen('ping %s -t -n 5' % (ip,))

    # 将cmd窗口显示的文字信息写入txt文件，再从文件中逐行筛选、呈现
    file = open('/home/data/ping/%s ping.txt' % (ip), 'w')
    file.write(f.read())
    file.close()
    file = open('/home/data/ping/%s ping.txt' % (ip), "r")

    averageTimeList = []
    sumOfTime = 0
    count = 0

    for line in file:

        begin = line.find("time=")
        end = line.find("ttl")
        if begin != -1 and end != -1:
            time = get_int_after(line, "time=")
            TTL = get_int_after(line, "ttl=")
            averageTimeList.append(time)
            sumOfTime = sumOfTime + time
            count = count + 1

    if count != 0:
        averageTime = sumOfTime / count
    elif count == 0:
        averageTime = 0
        TTL = 0  # 如果全部超时，平均time和TTL都记为0

    file.close()
    list = []
    list.append(ip)
    list.append(averageTime)
    list.append(TTL)

    return list  # 返回一个保存有ip,平均时间，TTL的列表

