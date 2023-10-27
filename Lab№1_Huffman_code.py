#Функция подсчета частот символов в тексте
def count_frequencies(text):
    freq_dict = {}
    for char in text:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict


#def build_huffman_tree(freq_dict):
    
def huffman_code(input_file, output_file):
    freq_dict = count_frequencies(input_file)
#def huffman_decode:
    
if __name__ == "__main__":
    code_file = "code_file.txt"
    decode_file = "decode_file.txt"
    
    