from idaapi import *

def xor_decrypt_one_key(effective_address, key, size):
	counter = 0

	while counter < size:
		PatchByte(effective_address+counter, Byte(effective_address+counter) ^ key)
		counter += 1

def xor_decrypt_key_array(effective_address, keys, size):
	counter = 0
	key_counter = 0

	while counter < size :
		key_counter = counter % 20
		PatchByte(effective_address+counter, Byte(effective_address+counter)^keys[key_counter])
		counter += 1

def main():
	#array of keys for decrypt PE in memory
	key_array = [0x31, 0x32, 0x30, 0x31, 0x31, 0x37, 0x37, 0x34, 0x36, 0x33, 0x31, 0x32, 0x32, 0x33, 0x39, 0x38, 0x32, 0x34, 0x39, 0x00]

	# decrypt first block
	xor_decrypt_one_key(0x00401516, 0x83, 0x4)

	#decrypt second block
	xor_decrypt_one_key(0x00401524, 0x8D, 0xC1)

	#decrypt third block
	xor_decrypt_one_key(0x0040143C, 0x85, 0x6B)

	#decrypt fourth block
	xor_decrypt_one_key(0x004013EB, 0xAD, 0x2D)

	#decrypt fifth block
	xor_decrypt_one_key(0x00401011, 0xEF, 0x2F1)

	#decrypt sixth block
	xor_decrypt_one_key(0x004013AB, 0xF3, 0x2F)

	#decrypt PE-file in memory
	xor_decrypt_key_array(0x00406000, key_array, 0x4800)

if __name__ == "__main__":
    main()