import os
from functions import get_int_after
from threading import Thread


def ping(ip):  # 函数参数是ip地址
    outputText = os.popen('ping %s -n -c 5' % (ip,)).read()

    timeList = get_int_after(outputText, "time")
    TTL_List = get_int_after(outputText, "ttl")

    if len(TTL_List) == 0:
        TTL = 0
        averageTime = 0
    else:
        TTL = TTL_List[0]
        timeList = map(lambda time: float(time), timeList)
        timeList = list(timeList)
        averageTime = sum(timeList) / len(timeList)

    averageTime = round(averageTime, 3)

    TTL = str(TTL)
    averageTime = str(averageTime)
    return (ip, TTL, averageTime)  # 返回一个保存有ip,平均时间，TTL的列表

