# %% Imports
import codecs
import crypto_lib as cl
# %% input
input = '1c0111001f010100061a024b53535009181c'
key = '686974207468652062756c6c277320657965'
# %% change them into byte format
hex = codecs.decode(input, encoding = 'hex')
key = codecs.decode(key, encoding = 'hex')
# %% xor encryption
output = cl.xor(hex, key)

# %% 
print(output) # bytearray(b"the kid don\'t play")
# %%
final = codecs.encode(output, encoding = 'hex')
# %%
print(final) # b'746865206b696420646f6e277420706c6179'


# %%
