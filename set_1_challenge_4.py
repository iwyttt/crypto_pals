# %% import
import codecs
from crypto_lib import english_metric, hex_to_utf_8, xor
import pandas as pd

# %% input

input = open("set_1_challenge_4_input.txt", "r")

# There is 327 lines in the input
#line = input.readlines()
#totalLine = len(line)
#print('there is ', totalLine, 'lines')

input = input.read()
#print(input)

# %% decode hex into raw byte

decode = []

for line in input.split('\n'):
    decode.append(codecs.decode(line, encoding = 'hex'))


# %% Count the % of input are letters/ common symbols
scores = {}

num_line = 0

# %%iterate through all the strings

for line in decode:
    #print('next line')
    #print(line)
    #print(num_line, len(line))
    # Do this for all the single characters
    for i in range(0,128,1):
        
        length = 30  #len(line)
        key = f"{i}" * length

        print(key)

        # decode key into raw bytes
        decoded_key = codecs.decode(key, encoding = 'hex')
        #print(decoded_key)

        # XOR the 2 strings
        temp = xor(line, decoded_key)
        #print(temp)

        # transform into utf-8
        temp = temp.decode('utf_8', errors = 'replace')

        # score the string against the english metric I created
        score = english_metric(temp) 

        scores[(i) + num_line * 128] = score
    
    num_line += 1

# %% validate the size of scores

print('size of scores:',len(scores))

print('expected no of keys:',128*327)



# %% Pick the key with the best score
for key, score in scores.items():
    if score > 0.95:
        print(key) #21795, 27654

# %% Selected line and key

chosen_key = 21795
chosen_line = chosen_key//128
chosen_letter = chosen_key % 128

print('chosen line no:',chosen_line)
print('chosen letter no:',chosen_letter)

# %% Decode the message

chosen_key = f"35" * length
decoded_chosen_key = codecs.decode(chosen_key, encoding = 'hex')
raw_msg = xor(decode[170], decoded_chosen_key)
msg = raw_msg.decode('utf_8')
print(msg) # Now that the party is jumping (21795)



# %%
