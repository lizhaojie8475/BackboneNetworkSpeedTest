import sys, getopt
import os


def parseCommand(argv):
    """
    解析脚本参数
    argv: 脚本在命令行接收的参数列表
    return: 返回待分割的文件名，切割后的文件夹名，以及切割份数
    """
    inputFile = ""
    outFileHeader = ""
    splitNume = 0

    try:
        opts, args = getopt.getopt(argv, "i:o:n:")
    except getopt.GetoptError:
        print("SplitFile.py -i <input> -o <output> -n num")
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-i':
            inputFile = arg
        elif opt == "-o":
            outFileHeader = arg
        elif opt == "-n":
            splitNume = arg
    return inputFile, outFileHeader, splitNume

def splitSth(inputFile, outputHeader, num):
    """
    分割文件函数
    inputFile: 待分割文件名。默认去Data文件夹内寻找
    outputHeader: 分割后的文件存放的文件夹名
    num: 分割份数
    """
    dirPath = os.path.abspath(os.path.join(os.getcwd(), "..", ".."))
    dirPath += "/Data/"
    if not os.path.exists(dirPath + inputFile):
        print("Your expected inputFile is " + dirPath + inputFile)
        print("This inputFile did not exist !")
        sys.exit()
    else:
        inFile = open(dirPath + inputFile, 'r')
        lines = inFile.readlines()
        cnt = len(lines)
        singalCnt = cnt // int(num)
        t = 0

        if not os.path.exists(dirPath + outputHeader):
            os.mkdir(dirPath + outputHeader)

        while(cnt > 0):
            outFile = open(dirPath + outputHeader + "/data%d.txt" % (t), 'w')
            if cnt < singalCnt:
                outFile.write("".join(lines[t:]))
            else:
                outFile.write("".join(lines[t : t + singalCnt]))
            outFile.close()
            t += singalCnt
            cnt -= singalCnt


if __name__ == "__main__":
    fileName, newName, num = parseCommand(sys.argv[1:])
    splitSth(fileName, newName, num)