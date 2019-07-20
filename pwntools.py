#!/usr/bin/python2

from pwn import *
context.log_level = 'debug'

# binary
proc = process('/bin/sh')
proc.sendline('sleep 3; echo hello world;')
proc.recvline(timeout=1)
proc.recvline(timeout=5)
proc.interactive() 
proc.close()

# remote
conn = remote('ftp.ubuntu.com',21)
conn.send('USER anonymous\r\n')
conn.recvuntil(' ', drop=True)
conn.recvline()
conn.close()

# integer packing
print(p32(0xdeadbeef))

# (dis)assembly
print(asm('mov eax, 0').encode('hex'))
print(disasm('6a0258cd80ebf9'.decode('hex')))

# De Bruijn sequences
print(cyclic(20))
print(cyclic_find('faab'))

# ELF
libc = ELF('./libc')
print(hex(libc.address))
print(hex(libc.symbols['write']))
