from idaapi import *

ea = 0x00402140
key = 0x7d
size = 0x18
counter = 0

while counter < size:
	PatchByte(ea+counter, Byte(ea+counter)^key)
	counter += 1