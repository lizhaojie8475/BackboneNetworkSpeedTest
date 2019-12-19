import os
import sys

print("=== 获取当前文件上层目录 ===")
path = os.path.abspath(os.path.join(os.getcwd(), "..", ".."))
path += "/Data"
print(path)