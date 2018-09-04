
from Queue import Queue
import random

from pwn import *

context.log_level = 'debug'

def gcd ( a , b ):
    while b != 0: a, b = b, a % b
    return a

def rabin_miller(p):
    if(p<2): return False
    if(p!=2 and p%2==0): return False
    s=p-1
    while(s%2==0): s>>=1
    for _ in xrange(10):
        a=random.randrange(p-1)+1
        temp=s
        mod=pow(a,temp,p)
        while(temp!=p-1 and mod!=1 and mod!=p-1):
            mod=(mod*mod)%p
            temp=temp*2
        if(mod!=p-1 and temp%2==0): return False
    return True

def pollard_rho(n):
    if(n%2==0): return 2;
    x=random.randrange(2,1000000)
    c=random.randrange(2,1000000)
    y=x
    d=1
    while(d==1):
        x=(x*x+c)%n
        y=(y*y+c)%n
        y=(y*y+c)%n
        d=gcd(x-y,n)
        if(d==n): break;
    return d;

def primeFactorization(n):
    if n <= 0: raise ValueError("Fucked up input, n <= 0")
    elif n == 1: return []
    queue = Queue()
    factors=[]
    queue.put(n)
    while(not queue.empty()):
        l=queue.get()
        if(rabin_miller(l)):
            factors.append(l)
            continue
        d=pollard_rho(l)
        if(d==l):queue.put(l)
        else:
            queue.put(d)
            queue.put(l/d)
    return factors

def phi(n):

    if rabin_miller(n): return n-1
    phi = n
    for p in set(primeFactorization(n)):
        phi -= (phi/p)
    return phi

def fast_exponent(a, b, c, d, k):
    # ((a ** b) ** (c ** d)) % k
    x = pow(a, b, k)
    y = pow(c, d, phi(k))
    z = pow(x, y, k)
    return z


r = remote('misc04.grandprix.whitehatvn.com', 1337)

def solve():
    r.recvuntil('--------------------------------------\n')

    r.recvuntil('Face_index:')
    face_index = int(r.recvline().strip())

    data = r.recvuntil('So, what is the most friendly face?\n')

    friendly_scores = dict()

    for face_data in data.split('\n')[1:-2]:
        face, lip_point, nose_point, eyes_point, forehead_point = face_data.split()
        lip_point = int(lip_point)
        nose_point = int(nose_point)
        eyes_point = int(eyes_point)
        forehead_point = int(forehead_point)

        friendliness = fast_exponent(lip_point, nose_point, eyes_point, forehead_point, face_index)
        print((face, friendliness))
        friendly_scores[face] = friendliness

    print(friendly_scores)
    best_face = max(friendly_scores, key=lambda k: friendly_scores[k])
    r.sendline(best_face)
    r.recvuntil("It's friendly point\n")
    r.sendline(str(friendly_scores[best_face]))

for _ in range(5):
    solve()

r.interactive()
r.close()
