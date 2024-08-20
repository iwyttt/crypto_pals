# %% import
import codecs
import math
import base64
import crypto_lib as cl
import statistics

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

b_input = cl.convert_base64_to_binary(input)


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
b_input_length = len(b_input)
dist_scores = {}
for n in range(2,42): # keysize from 2 to 41

    #Put all from b_input into blocks of works in keysize
    word = {}
    for words_index in range(0,int(b_input_length/n)):

        if b_input_length < (n*(words_index+1)):
            print('loop broken due to word index larger than length of b_input')
            break

        word[words_index] = b_input[n*words_index: n*(words_index+1)]
        # word[1] = b_input[0:n]
        # word[2] = b_input[n:n*2]
        # word[3] = b_input[n*2:n*3]
        # word[4] = b_input[n*3:n*4]
    
    #Calculate hamming distance for each 2 word blocks and normalise it
    word_hamming_dist = {}
    for hamming_index in range(0,int(b_input_length/n/2)):

        if (b_input_length/2) < (hamming_index*2+1):
            print('loop broken due to hamming index larger than length of b_input')
            break

        if len(word[hamming_index*2]) != len(word[(hamming_index*2+1)]):
            print('words are not of the same length')
            break
        
        word_hamming_dist[hamming_index] = cl.hammingDist_from_binary(word[hamming_index*2],word[(hamming_index*2+1)])/n
        # 0，1
        # 2，3
        # 4，5

    #Calculate the mean of the hamming distance
    avg_hamming_dist_normalised = sum(float(v) for v in word_hamming_dist.values()) / len(word_hamming_dist)

    dist_scores[n] = avg_hamming_dist_normalised

# %% Ploting the normalised hamming distance for each keysize
import pandas as pd

df = pd.DataFrame(list(dist_scores.items()),columns = ['keysize','hamming_distance'])
df.plot(x ='keysize', y='hamming_distance', kind = 'line')

# %% Find the key size that has the smallest hamming distance
    
top_3_key = cl.sort_list_lowest(dist_scores, 3)
print(top_3_key)
 
# The key should be 29

# %% Break the input into 29 blocks
# 1st character -> block 1, 2nd character -> block 2, ... ,
# 29th character -> block 29, 30th character -> block 1

char29 = []

for num in range(1, 30):
    char29.append(num)

print(char29)

# %% Define total length of input

length = len(b_input)

print(length)

# %% Split the string into 29 parts

# Create empty dictionary
word_dict = {}

# Loop through 1 to 29
for num in char29:

    # Create a row in the dictionary for each number
    word_dict[num] = []

# %% Break the input into selected keysize of 29
for byte in b_input:

    if (length % 29) == 0:
        word_dict[1].append(byte)
    elif (length % 29) == 1:
        word_dict[2].append(byte)
    elif (length % 29) == 2:
        word_dict[3].append(byte)
    elif (length % 29) == 3:
        word_dict[4].append(byte)
    elif (length % 29) == 4:
        word_dict[5].append(byte)
    elif (length % 29) == 5:
        word_dict[6].append(byte)
    elif (length % 29) == 6:
        word_dict[7].append(byte)
    elif (length % 29) == 7:
        word_dict[8].append(byte)
    elif (length % 29) == 8:
        word_dict[9].append(byte)
    elif (length % 29) == 9:
        word_dict[10].append(byte)
    elif (length % 29) == 10:
        word_dict[11].append(byte)
    elif (length % 29) == 11:
        word_dict[12].append(byte)
    elif (length % 29) == 12:
        word_dict[13].append(byte)
    elif (length % 29) == 13:
        word_dict[14].append(byte)
    elif (length % 29) == 14:
        word_dict[15].append(byte)
    elif (length % 29) == 15:
        word_dict[16].append(byte)
    elif (length % 29) == 16:
        word_dict[17].append(byte)
    elif (length % 29) == 17:
        word_dict[18].append(byte)
    elif (length % 29) == 18:
        word_dict[19].append(byte)
    elif (length % 29) == 19:
        word_dict[20].append(byte)
    elif (length % 29) == 20:
        word_dict[21].append(byte)
    elif (length % 29) == 21:
        word_dict[22].append(byte)
    elif (length % 29) == 22:
        word_dict[23].append(byte)
    elif (length % 29) == 23:
        word_dict[24].append(byte)
    elif (length % 29) == 24:
        word_dict[25].append(byte)
    elif (length % 29) == 25:
        word_dict[26].append(byte)
    elif (length % 29) == 26:
        word_dict[27].append(byte)
    elif (length % 29) == 27:
        word_dict[28].append(byte)
    elif (length % 29) == 28:
        word_dict[29].append(byte)

    length -= 1

# %% Print outputs
print(b_input)
print(word_dict[1])


# %% Do single character key search for block 1
str_blk_1 = ''
list_str_blk_1 = [chr(int(byte, 2)) for byte in word_dict[1]]
str_blk_1 = str_blk_1.join(list_str_blk_1)
scores1 = cl.single_character_key(str_blk_1)

# %%
best_3_keys = cl.sort_list_highest(scores1, 3)
print(best_3_keys)

        # 1, 11, 111 has the score of 0.7746153846153846

# %% Do single character key search for block 2
str_blk_2 = ''
list_str_blk_2 = [chr(int(byte, 2)) for byte in word_dict[2]]
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
