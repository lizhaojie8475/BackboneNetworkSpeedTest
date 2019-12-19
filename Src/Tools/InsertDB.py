import os, sys, re
pwd = os.path.dirname(__file__)
parentPath = os.path.abspath(os.path.join(pwd, ".."))
sys.path.append(parentPath)
from Tools.MySQLHelper import MySqlHelper


def insertChinaDNS(fileName):
    helper = MySqlHelper()
    helper.connect()

    dirPath = os.path.abspath(os.path.join(os.getcwd(), "..", ".."))
    dirPath += "/Data/"
    fileName = dirPath + fileName

    inFile = open(fileName, 'r')
    dataList = inFile.readlines()
    inFile.close()

    for data in dataList:
        fields = data.split(",")
        sql = "INSERT INTO china_dns VALUES (%s, %s, %s, %s)"
        helper.insert(sql, *fields)
    helper.close()


if __name__ == "__main__":
    tableName = sys.argv[1]
    fileName = sys.argv[2]

    if tableName == "china_dns":
        insertChinaDNS(fileName)