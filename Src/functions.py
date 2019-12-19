import json
import re


def get_int_after(s, f):  # 提取某字符后的int，s为目标字符串，f为目标字符

    S = s.upper()
    F = f.upper()
    ans = re.findall(r"\b%s=(\d+(?:\.\d+)?)\b"%(F, ), S)
    return ans


def get_str_btw(s, f, b):  # 获取两个字符之间的内容，s为目标字符串，f、b为两个字符
    par = s.partition(f)
    return (par[2].partition(b))[0][:]


def getip(string):  # 直接从字符串中得到ip，返回值是列表
    result = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", string)
    return result


def write_json(jlist,ip):
    # 将bx列表写入json文件
    with open('/home/data/final/%s.json'%ip, 'w') as f_obj:
        json.dump(jlist, f_obj)


def read_json(ip):
    # 读取存储于json文件中的列表
    with open('/home/data/final/%s.json'%ip, 'r') as f_obj:
        jlist = json.load(f_obj)
    return jlist
