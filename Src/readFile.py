from getInfo import getInfo
from functions import getip


def readFile(nameOfFile, helper, command):
    file = open(nameOfFile, 'r')
    list = []  # 保存目标文件中的所有ip
    for line in file:
        list.append(getip(line)[0])
    file.close()

    for i in list:
        getInfo(i, helper, command)

    helper.close()
