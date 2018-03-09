#!/usr/bin/env python2

from pwn import *

shellcode = open("shellcode").read()

print("length: " + str(len(shellcode)))

assert("\0" not in shellcode)
assert("\r" not in shellcode)
assert("\n" not in shellcode)

print("")
print("x86 disas:")
context.arch = "i386"
print(disasm(shellcode))


print("")
print("x86-64 disas:")
context.arch = "amd64"
print(disasm(shellcode))

with open("test.c", "w") as f:
	code = "const char main[] = \"\\x" + "\\x".join("%02x" % ord(x) for x in shellcode) + "\";"
	print("")
	print(code)
	f.write(code)
