# %% import
import codecs
import math
import base64
import crypto_lib as cl

import importlib
importlib.reload(cl)

# %% input

input = open("set_1_challenge_6_input.txt","r")

# There is 64 lines in the input
# line = input.readlines()
# totalLine = len(line)
# print('there is ', totalLine, 'lines')

input = input.read()
#print(input)

b_input = cl.convert_string_to_binary(input)

# %% Make bit into byte (1 -> 8)
byte_input = cl.create_list_of_bytes_from_bit_string(b_input, 8)
print(byte_input)

# %% Compute hamming distance between 2 strings

# initializing string 
str1 = 'this is a test'
str2 = 'wokka wokka!!!'

b_str1 = cl.convert_string_to_binary(str1)
b_str2 = cl.convert_string_to_binary(str2)

byte_str1 = cl.create_list_of_bytes_from_bit_string(b_str1, 8)
byte_str2 = cl.create_list_of_bytes_from_bit_string(b_str2, 8)

print(cl.hammingDist_from_binary(b_str1,b_str2))
print(cl.hammingDist_from_byte(byte_str1,byte_str2))

# %% iterate through keysize
dist_scores = {}
for n in range(2,42): # keysize from 2 to 41
    
    word1 = byte_input[0:n]
    word2 = byte_input[n:(n+n)]

    dist = cl.hammingDist_from_byte(word1,word2)
    norm_dist = dist/(n*8)

    print(word1, word2, dist, n, norm_dist)

    dist_scores[n] = norm_dist

# %% Find the key size that has the smallest hamming distance
    
top_3_key = cl.sort_list_lowest(dist_scores, 3)
print(top_3_key)
 
# 3 has the score of 2.3333333333333335
# 2 has the score of 0.875
# 7 has the score of 0.9

# %% Break the input into 3 blocks
# 1st character -> block 1, 2nd character -> block 2, 3rd character -> block 3,
# 4th character -> block 1, 5th character -> block 2, 6th character -> block 3
block1 = []
block2 = []
block3 = []        

length = len(byte_input)

# %% Break the input into selected keysize of 3
for byte in byte_input:

    if (length % 3) == 0:
        block1.append(byte)
    elif (length % 3) == 1:
        block2.append(byte)
    elif (length % 3) == 2:
        block3.append(byte)

    length -= 1

# %% Do single character key search for block 1
str_blk_1 = ''
list_str_blk_1 = [chr(int(byte, 2)) for byte in block1]
str_blk_1 = str_blk_1.join(list_str_blk_1)
scores1 = cl.single_character_key(str_blk_1)

# %%
best_3_keys = cl.sort_list_highest(scores1, 3)
print(best_3_keys)

        # 1, 11, 111 has the score of 0.7746153846153846

# %% Do single character key search for block 2
str_blk_2 = ''
list_str_blk_2 = [chr(int(byte, 2)) for byte in block2]
str_blk_2 = str_blk_2.join(list_str_blk_2)
scores2 = cl.single_character_key(str_blk_2)

# %%
best_3_keys = cl.sort_list_highest(scores2, 3)
print(best_3_keys)

        # 10 has score of 0.7561538461538462
        # 25 has score of 0.7546153846153846
        # 20 has score of 0.7546153846153846


# %% Do single character key search for block 3
str_blk_3 = ''
list_str_blk_3 = [chr(int(byte, 3)) for byte in block3]
str_blk_3 = str_blk_3.join(list_str_blk_3)
scores3 = cl.single_character_key(str_blk_3)

# %%
best_3_keys = cl.sort_list_highest(scores3, 3)
print(best_3_keys)

        # 99 has score of 0.0103397341211226
        # 93 has score of 0.009345794392523364

# %%
