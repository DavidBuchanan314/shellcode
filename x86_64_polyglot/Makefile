all:
	nasm shellcode.asm -o shellcode
	./test.py
	gcc test.c -m32 -o test32
	gcc test.c -o test64
