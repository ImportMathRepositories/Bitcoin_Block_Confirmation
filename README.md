# Bitcoin_Block_Confirmation
Python script to confirm the hash of a bitcoin block.

# Running this code on your machine:
1. Have a functioning Python 2.7+ version installed
2. Clone this repository
3. Open a terminal and cd into src
4. Run python and import main (and optionally block_headers)
5. Run main.get_hash() on a block header (either make your own or use one from block_headers.py)

The function expects the block header as a dictionary object with the following keys:

1. 'version' (int: version number)
2. 'previous_block' (string: hex string of the hash of the previous block)
3. 'merkle_root' (string: hex string of the merkle root)
4. 'timestamp' (int: unix time, number of seconds since the epoch)
5. 'bits' (string: hex string representing the difficulty target)
6. 'nonce' (int: nonce value)

# Explanation of the Code
The block header is formatted, passed through two rounds of SHA256, and compared to the difficulty target.

This is not a program meant for mining, just for confirming blocks that have already been mined.

Although not recommended (due to speed/efficiency reasons), this could be used to mine by looping through nonce values in the block header.
