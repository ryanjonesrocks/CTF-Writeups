#A Tour of x86 - Part 1

##Introduction to Reverse Engineering (RE)
This challenge is meant as an introduction to RE. For those unfamilar with Reverse engineering, it is defined as the dissection and understanding of SYSTEMS, not of CODE. Meaning that it's more about understanding how the system interacts instead of understanding 100% of the assembly code. This challenge is less of a vulnerability and more about learning RE. 

##Approaching the problem
This challenge presents us with three files: `Makefile stage-1.asm  stage-2.bin`. By reading through the files, only `stage-1.asm` is needed to solve this challenge. We're presented with an annotated assembly file that walks us through the challenge. 

##Solution
When we netcat into the server `nc rev.chal.csaw.io 9003`. We're presented with a long delay of text. This is meant to prevent bruteforcing and actually understand the problem. 

###Stage1: What is the value of dh after line 129 executes? (Answer with a one-byte hex value, prefixed with '0x')
At line 129 we see that, the assembly instruction is `xor dh, dh  ; <- Question 1`. xoring a number with itself is always 0, this is used to clear registers in assembly. Notice is asks for a one byte number. 0x0 would be incorrect because it is only 4 bits or half a byte. The correct answer is `0x00`

###Stage2: What is the value of gs after line 145 executes? (Answer with a one-byte hex value, prefixed with '0x'

```
  mov dx, 0xffff  ; Hexadecimal
  not dx

  cmp dx, 0
  jne .death  ; This time jumping backwards to a label we passed... Saves duplicate code.

  ; Alright, recruits! New registers!
  ; These are called segment registers and are all 16-bits only.
  ; ...Yeah...
  ; Fuckin' useless.

  mov ds, ax ; Oh yeah so this time since
  mov es, bx ; the other registers are
  mov fs, cx ; already zero, I'm just going
  mov gs, dx ; to use them to help me clear     <- Question 2
```

In this stage, we need to trace through the `dx` register. We see initially it has a value of `0xffff`. The next instruction is `not dx`. The `not` instruction preforms a bit-wise inversion of the number. `not 0xffff` equals 0, so dx equals 0. `mov gs, dx` stores the value of dx into gs, so the answer will also be `0x00`

###Stage3: What is the value of si after line 151 executes? (Answer with a two-byte hex value, prefixed with '0x')

We need to find the value of si, by tracing the value of sp, which leads to `cx`. `cx` also has a value of 0 but the challenge asks for a two byte hex value so the answer will be `0x0000`
```
mov cx, 0 ; The other two values get overwritten regardless, the value of ch and cl (the two components that make up cx) after this instruction are both 0, not 1.
...
  ; Many of these registers actually have names, but they're mostly irrelevant and just legacy.
  mov sp, cx ; Stack Pointer
  mov bp, dx ; Base Pointer
  mov si, sp ; Source Index       <- Question 3
```

###Stage4: What is the value of ax after line 169 executes? (Answer with a two-byte hex value, prefixed with '0x')

```
; New function
new_function:
  ; As you can see, it's not really a new function... Since whitespace and labels are effectively ignored, I'm just labeling a new spot in the source file.

  ; Goal: Let's print some text!

  ; First things first, we need to setup the screen such that it will allow us to display text..
  mov ax, 0x0003
  int 0x10          ; AH! Something new!

  ; Step two, a problem: we can only print one letter at a time, like so:
  mov al, 't'	
  mov ah, 0x0e      ; <- question 4
  int 0x10          ; The same new thing. Scawy!
```
Hint: `AH + 0x0e allows us to print the 8-bit ASCII letter stored in the low 8-bit portion of the a register: al.` The payload must contain 0x0e as the first 8 bits (1 byte) and the letter 't' as the second 8 bits. Characters in assembly are represented in ASCII in the form of hexadecimal. In Python, we can convert t to ASCII using `hex(ord('t'))`. This final payload will be `0x0e74`


###Stage5: What is the value of ax after line 199 executes for the first time? (Answer with a two-byte hex value, prefixed with '0x')
Print the first character of the string. Final Payload `0x0e61`.

```
.string_to_print: db "acOS", 0x0a, 0x0d, "
...
  mov al, [sils
    ]  ; Since this is treated as a dereference of si, we are getting the BYTE AT si... `al = *si`

    mov ah, 0x0e  ; <- Question 5!
    int 0x10      ; Actually print the character
 
    inc si        ; Increment the pointer, get to the next character
    jmp .print_char_loop
    .end:
```

##Flag
`flag{rev_up_y0ur_3ng1nes_reeeeeeeeeeeeecruit5!}`. I solved this challenge using pwntools, check out my script for the full exploit. 