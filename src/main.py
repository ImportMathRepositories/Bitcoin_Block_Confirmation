# Uses a bitcoin block header to confirm the next block in the chain

import binascii
import hashlib

# Takes a hex string in either big or little endian and reverses it
def reverse_endian(hex_string):
	return binascii.hexlify(binascii.unhexlify(hex_string)[::-1])

# Takes an integer, converts to hex, formats/zero pads to 32 bits, and reverse endianness
def format_integer(current_int):
	return reverse_endian(hex(current_int)[2:].zfill(8))

# Compares the hash to the difficulty target to see if the block is confirmed
def check_target(current_hash, target):
	num_bytes = int(target[:2], 16)
	hex_target = target[-6:] + (2 * num_bytes - 6) * '0'
	if int(current_hash, 16) < int(hex_target, 16):
		print('Block confirmed!')
	else:
		print('Target missed!')

# Produces a hash of the given block header dictionary
def get_hash(block_header):
	# All of the header information is adjusted to the proper form
	version = format_integer(block_header['version'])
	previous_block = reverse_endian(block_header['previous_block'])
	merkle_root = reverse_endian(block_header['merkle_root'])
	timestamp = format_integer(block_header['timestamp'])
	bits = reverse_endian(block_header['bits'])
	nonce = format_integer(block_header['nonce'])

	# The adjusted information is now concatenated into a single message
	message = version + previous_block + merkle_root + timestamp + bits + nonce

	# The correctly formatted message is now passed through two rounds of sha256
	first_pass = hashlib.sha256(binascii.unhexlify(message)).digest()
	second_pass = hashlib.sha256(first_pass).digest()

	# Formatting the final result and confirming the hash
	formatted_result = binascii.hexlify(second_pass[::-1])
	check_target(formatted_result, block_header['bits'])
	return formatted_result
