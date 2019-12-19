from ping import ping
from traceRoute import tracert
from functions import write_json, read_json
import socket
from Tools.MySQLHelper import MySqlHelper
import numpy as np

def insertDB(foundation, routers, sourceIP, helper):
    targetIP = foundation[0]
    TTL = foundation[1]
    time = foundation[2]
    stability = ";".join(["1"] * len(routers))
    routers = ";".join(routers)


    sql = "INSERT INTO trace_route VALUES (%s, %s, %s, %s, %s, %s)"
    helper.insert(sql, targetIP, sourceIP, TTL, time, routers, stability)
    helper.close()

def updateDB(foundation, routers_new, helper, tableName = "trace_route"):
    targetIP = foundation[0]
    TTL = foundation[1]
    time = foundation[2]

    routers_sql = 'SELECT routers FROM %s WHERE target_ip = "%s" ' % (tableName, targetIP)
    stability_sql = 'SELECT stability FROM %s WHERE target_ip = "%s" ' % (tableName, targetIP)

    routers_old = helper.search(routers_sql)
    routers_old = np.array(routers_old)
    routers_old = routers_old[:, 0]
    routers_old = routers_old[0]
    routers_old = routers_old.split(";")

    stability = helper.search(stability_sql)
    stability = np.array(stability)
    stability = stability[:, 0]
    stability = stability[0]
    stability = stability.split(";")
    stability = list(map(lambda s: int(s), stability))

    for i, router in enumerate(routers_old):
        if router in routers_new:
            stability[i] += 1
    stability = list(map(lambda s: str(s), stability))
    stability = ";".join(stability)

    fieldList = ["TTL", "time", "stability"]
    valueList = [TTL, time, stability]
    helper.update(fieldList, valueList, "trace_route", "target_ip", targetIP)

def getInfo(ip, helper):
    foundation = ping(ip)
    routers = tracert(ip)
    sourceIp = socket.gethostbyname(socket.gethostname())

    # print("foundation: ", foundation)
    # print("routers: ", routers[:5])
    # print(sourceIp)
    # print("-----------------------------------------------------", "\n")
    # insertDB(foundation, routers, sourceIp, helper)
    updateDB(foundation, routers, helper)