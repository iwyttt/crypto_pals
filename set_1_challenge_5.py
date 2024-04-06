# %% import
import codecs
from crypto_lib import repeated_key_xor


# %% input and key
input = b'Burning \'em, if you ain\'t quick and nimble\n I go crazy when I hear a cymbal'
key = b'ICE'

# %% encoding with repeated key XOR

output = repeated_key_xor(input, key)

output = output.hex()

print(output)

# 0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
# a282b2f2043630c69242a69203728393c69342d2c2d6500632d2c22376922652a3a282b2229
