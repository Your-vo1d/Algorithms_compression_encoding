#Функция подсчета частот символов в тексте
def count_frequencies(text):
    # Инициализируем пустой словарь, в котором будем хранить частоты символов.
    freq_dict = {}

    for char in text:  # Проходим по каждому символу в тексте.
        if char in freq_dict: # Проверяем, существует ли символ в словаре.
            freq_dict[char] += 1 # Если символ уже есть в словаре, увеличиваем его частоту на 1.
        else:
            freq_dict[char] = 1 # Если символ отсутствует в словаре, добавляем его в словарь с начальной частотой 1.

    # Возвращаем словарь, в котором ключи - символы, а значения - их частоты.
    return freq_dict

# Функция построение дерева Хаффмана
def build_huffman_tree(freq_dict):
    # Создаем начальные узлы для каждого символа в словаре частот.
    nodes = [(char, freq, []) for char, freq in freq_dict.items()]

    # Пока в списке узлов есть более одного узла, продолжаем объединять узлы.
    while len(nodes) > 1:
        # Сортируем узлы по частотам, чтобы объединить узлы с наименьшими частотами.
        nodes.sort(key=lambda x: x[1])

        # Извлекаем два узла с наименьшими частотами из начала списка.
        left = nodes.pop(0)
        right = nodes.pop(0)

        # Создаем новый узел, объединяя два выбранных узла, с частотой, равной сумме их частот,
        # и добавляем этот новый узел в список узлов для дальнейшего объединения.
        merged_node = (None, left[1] + right[1], [left, right])
        nodes.append(merged_node)

    # Возвращаем корень дерева Хаффмана, который является единственным элементом списка nodes.
    return nodes[0]

    
def build_huffman_codes(node, current_code, huffman_codes):
    char, freq, children = node
    if char is not None:
        huffman_codes[char] = current_code
    for child in children:
        build_huffman_codes(child, current_code + "0", huffman_codes)
    
    return huffman_codes

#Кодирование текста
def encode_text(text, huffman_codes):
    encoded_text = "".join(huffman_codes[char] for char in text)
    return encoded_text

# Декодирование текста  
def decode_text(encoded_text, huffman_tree):
    decoded_text = ""
    node = huffman_tree

    for bit in encoded_text:
        if bit == "0":
            node = node[2][0]
        else:
            node = node[2][1]

        if node[0] is not None:
            char, freq, _ = node
            decoded_text += char
            node = huffman_tree

    return decoded_text

if __name__ == "__main__":
    code_file = "code_file.txt"
    decode_file = "decode_file.txt"
    
    