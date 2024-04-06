# %% Imports
import codecs
import crypto_lib as cl


# %% input
hex = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

# %% change from hex to base64
b64 = cl.hex_to_base64(hex)

# %% output
print(b64)

desired_output = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
# %% extra dumb challenge from rabbit
# change from hex to utf-8

ascii = bytes.fromhex(hex).decode('utf-8')

print(ascii) # I'm killing your brain like a poisonous mushroom

# %%
