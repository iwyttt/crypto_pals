# %% import
import codecs
import base64

# %% encoding

def hex_to_base64(hex):
    base64_output = codecs.encode(codecs.decode(hex, 'hex'), 'base64').decode()
    return base64_output

def hex_to_utf_8(hex):
    utf_8 = bytes.fromhex(hex).decode('utf-8')
    return utf_8


# %% XOR encryption
def xor(data:bytes, key:bytes) -> bytearray: 

    if ((type(data) == str) or (type(key) == str)):
        raise ValueError(f'your input: {data, key} is string, make it byte')
    
    return bytearray(a^b for a, b in zip(*map(bytearray, [data, key]))) 

# %% count no of XOR
def xor_count(data:bytes, key:bytes) -> bytearray: 

    if ((type(data) == str) or (type(key) == str)):
        raise ValueError(f'your input: {data, key} is string, make it byte')
    elif len(data) != len(key):
        raise ValueError(f'your input: {data, key} are not the same length, fix it')
    
    xor_results = {}

    for byte in range (len(data)):
        if data[byte] == key[byte]:
            xor_results[byte] = 1
        else:
            xor_results[byte] = 0


    return xor_results

# %% Evaluate how close the sentense is to English
def english_metric(input):

    good_letters = 0
    length = len(input)

    if (type(input) != str):
        raise ValueError(f'your input: {input} is not string, fix it.')

    for character in input:
        if character in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.?!\'\";- ':
            good_letters += 1

    return good_letters/length


# %% Repeating key XOR encryption
def repeated_key_xor(plain_text, key):
   
    # returns plain text by repeatedly xoring it with key
    pt = plain_text
    len_key = len(key)
    encoded = []
     
    for i in range(0, len(pt)):
        encoded.append(pt[i] ^ key[i % len_key])
    return bytes(encoded)

# %% decrypt string with single character fixed length key
def single_character_key(string):

    scores = {}
    length = len(string)
    string = bytes(string,'UTF-8')

    for i in range(0,128,1):

        key = f"{i}" * length

        # decode key into raw bytes
        decoded_key = bytes(key, 'UTF-8')

        # XOR the 2 strings
        temp = xor(string, decoded_key)

        # transform into utf-8
        temp = temp.decode('utf_8', errors = 'replace')

        # score the string against the english metric I created
        score = english_metric(temp) 

        scores[i] = score

    return scores

# %% pick the highest score
def pick_key_with_highest_score(scores):

    selected_key = 9999999

    for key, score in scores.items():
        if score > 0.95: # Can change the threshold
            selected_key = key

    if selected_key == 9999999:
        return print('Please change the threshold for the score')
    else:
        return selected_key

# %% decrypt message
def decrypt_message(chosen_key, length, encrypted_msg):
    chosen_key = f"{chosen_key}" * length
    decoded_chosen_key = codecs.decode(chosen_key, encoding = 'hex')
    raw_msg = xor(encrypted_msg, decoded_chosen_key)

    return raw_msg

# %% Calculate Hamming distance between 2 strings
# used in function below
def hammingDist_from_strings(str1, str2): 
    i = 0
    count = 0
  
    while(i < len(str1)): 
        #print(str1[i], str2[i])
        char1 = str1[i]
        char2 = str2[i]
        #print(char1, char2)
        int1 = ord(char1)
        int2 = ord(char2)
        #print(int1, int2)
        bin1 = bin(int1)[2:].zfill(8)
        bin2 = bin(int2)[2:].zfill(8)
        #print(bin1, bin2)
        for bit1, bit2 in zip(bin1, bin2):
            #print(bit1, bit2)
            if(bit1 != bit2): 
                count += 1

        i += 1

    # hello -> string
    # a string is a list of char/array
    # a char is a character (0 to 255)
    # 1 byte is 8 1/0s
    # 1 nibble is 4 0/1s
    # 1 bit is 1 1/0 (boolean)
        
    return count

# %% Calculate Hamming distance between 2 strings
# used in function below
def hammingDist_from_byte(list_of_bytes_1:list, list_of_bytes_2:list) -> int: 
    count = 0

    for byte1, byte2 in zip(list_of_bytes_1, list_of_bytes_2):
        for bit1, bit2 in zip(byte1, byte2):
            print(bit1, bit2)
            if(bit1 != bit2): 
                count += 1
    

        
    return count

# %% Calculate Hamming distance between 2 binary
# used in function below
def hammingDist_from_binary(bin1, bin2): 
    i = 0
    count = 0
  
    while(i < len(bin1)): 

        #print(bin1[i], bin2[i])
        if(bin1[i] != bin2[i]): 
            count += 1

        i += 1
        
    return count


# %% Convert string to binary
def convert_string_to_binary(str):
    # using join() + ord() + format()
    # Converting String to binary
    b_str = ''.join(format(ord(i), '08b') for i in str)

    return (b_str)

# %% Convert string to binary
def convert_base64_to_binary(base64_input: str):
    
    encoded_ascii = base64_input.encode("ascii")
    decoded = base64.decodebytes(encoded_ascii)

    binary_format = ["{:08b}".format(x) for x in decoded]

    return (binary_format)

# %% Pick top n number of matches with the lowest scores
def sort_list_lowest(dict, target_number):

    sort_dict = sorted(dict.items(), key = lambda item: item[1])

    return sort_dict[0:target_number]


# %% Pick top n number of matches with the highest scores
def sort_list_highest(dict, target_number):

    sort_dict = sorted(dict.items(), key = lambda item: item[1])

    return sort_dict[len(dict)-target_number-1:-1]


# %% Create list of bytes from bit string
def create_list_of_bytes_from_bit_string(bit_string: str, length:int) -> list:
    """
    Converts a bit string to a list of bytes
    :param bit_string: bit string to convert
    :return: list of bytes
    """
    bytes_list = []

    for i in range(0, len(bit_string), length):
        byte = bit_string[i:i+length]
        bytes_list.append(byte)

    return bytes_list
