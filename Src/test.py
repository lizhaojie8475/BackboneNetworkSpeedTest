import threading
from readFile import readFile
import os, sys
from Tools.MySQLHelper import MySqlHelper

if __name__ == "__main__":
    thread = []  # 线程列表，存放线程
    dirPath = os.path.join(os.path.dirname(__file__), "..")
    dirPath += "/Data/splitedDNS"
    fileList = os.listdir(dirPath)
    fileList = filter(lambda file: file.startswith("data") and file.endswith(".txt"), fileList)
    fileList = list(fileList)

    for file in fileList:
        file = dirPath + "/" + file
        helper = MySqlHelper()
        helper.connect()
        t = threading.Thread(target=readFile, args=(file, helper))
        thread.append(t)

    for i in thread:
        i.start()
