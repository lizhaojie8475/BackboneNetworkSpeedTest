from getInfo import getInfo
from functions import getip


def readFile(nameOfFile):
    file = open('D:\\%s.txt' % nameOfFile, 'r')
    list = []  # 保存目标文件中的所有ip
    for line in file:
        list.append(getip(line)[0])
    file.close()

    for i in list:
        print(getInfo(i))
