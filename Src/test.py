import threading
import readFile

if __name__ == "__main__":
    counter = 1  # 控制ip的递增
    thread = []  # 线程列表，存放线程
    while counter <= 1:
        t = threading.Thread(target=readFile, args=('filetest%s' % counter,))
        thread.append(t)
        counter = counter + 1

    for i in thread:
        i.start()
