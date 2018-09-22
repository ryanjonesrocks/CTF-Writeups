from pwn import *

context.log_level = 'debug'
conn = remote('rev.chal.csaw.io',9003)
conn.recvline()
conn.sendline('0x00')
#conn.recvuntil('What is the value of gs after line 145 executes?')
conn.recvline()
conn.sendline('0x00')
conn.recvline()
conn.sendline('0x0000')
#What is the value of ax after line 169 executes? (Two byte hex val)
conn.recvline()
conn.sendline('0x0e74') #not 0x0074
conn.recvline()
conn.sendline('0x0e61') #not 0x0074

conn.interactive()
