import os
import re
import platform
import socket


def windows_getIP():
    s=os.popen('ipconfig').read()
    ips=re.findall("IPv4\s地址\W.*?子网掩码",s,re.S)
    ip=[]
    for i in ips:
        ip+=(re.findall("\d+\.\d+\.\d+\.\d+",i))
    return ip


def linux_getIP():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return ip


def getHostname():
    s=os.popen('hostname').read()
    return s


if __name__=="__main__":
    sys_type=platform.system()
    if sys_type=="Linux":
        ip_L=linux_getIP()
        print("ip:", ip_L)
    elif sys_type == "Windows" or "Darwin":
        ip_W = windows_getIP()
        print("ip:", ip_W)
    else:
        print("其他系统")
