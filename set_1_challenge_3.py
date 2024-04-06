# %% import
import codecs

from crypto_lib import english_metric, hex_to_utf_8, xor

# %% input
input = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

# %% decode hex into raw byte
decode = codecs.decode(input, encoding = 'hex')

length = len(decode)

# %% Count the % of input are letters/ common symbols
scores = {}

# Do this for all the single characters
for i in range(0,128,1):

    key = f"{i}" * length

    # decode key into raw bytes
    decoded_key = codecs.decode(key, encoding = 'hex')

    # XOR the 2 strings
    temp = xor(decode, decoded_key)

    # transform into utf-8
    temp = temp.decode('utf_8', errors = 'replace')

    # score the string against the english metric I created
    score = english_metric(temp) 

    scores[i] = score

# %% Pick the key with the best score
for key, score in scores.items():
    if score > 0.95:
        print(key) # 58

# %% Decode the message

chosen_key = f"58" * length
decoded_chosen_key = codecs.decode(chosen_key, encoding = 'hex')
raw_msg = xor(decode, decoded_chosen_key)
msg = raw_msg.decode('utf_8')
print(msg) # Cooking MC's like a pound of bacon

# %%
