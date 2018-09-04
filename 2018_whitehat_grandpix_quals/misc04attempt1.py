from pwn import *
while True:
    r = remote('misc04.grandprix.whitehatvn.com', 1337)
    r.send(':-)')
    print r.recvuntil('So, what is the most friendly face?\n')
#r.send(':-)')
    answer = r.recvline()
    print answer
    if("friendly point" in answer):
    	print r.recvall()
    	break 
#r.send(':-)')
    
