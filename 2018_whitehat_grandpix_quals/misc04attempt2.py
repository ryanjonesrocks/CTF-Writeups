
from pwn import *

import fractions

context.log_level = 'debug'

def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            amount += 1
    return amount

def fast_exponent(a, b, c, d, k):
    # ((a ** b) ** (c ** d)) % k
    x = pow(a, b, k)
    y = pow(c, d, phi(k))
    z = pow(x, y, k)
    return z


while True:
    r = remote('misc04.grandprix.whitehatvn.com', 1337)

    r.recvuntil('------------------------------Stage 1--------------------------------------\n')

    r.recvuntil('Face_index:')
    face_index = int(r.recvline().strip())

    print(face_index)

    data = r.recvuntil('So, what is the most friendly face?')

    face_data  = data.split('\n')[1]
    face, lip_point, nose_point, eyes_point, forehead_point = face_data.split()
    lip_point = int(lip_point)
    nose_point = int(nose_point)
    eyes_point = int(eyes_point)
    forehead_point = int(forehead_point)

    r.recvline()
    r.sendline(face)
    if("friendly point" in r.recvline()):
        friendliness = fast_exponent(lip_point, nose_point, eyes_point, forehead_point, face_index)
        print(friendliness)
        r.sendline(str(friendliness))
        r.interactive()
    r.close()

r.close()
