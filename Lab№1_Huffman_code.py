import heapq #Подключени библиотеки для создания дерева
from collections import defaultdict #

#Функция для построение дерева Хаффмана
def build_huffman_tree(symbols_freq):
    heap = [[weight, [symbol, ""]] for symbol, weight in symbols_freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        low = heapq.heappop(heap)
        high = heapq.heappop(heap)
        for pair in low[1:]:
            pair[1] = '0' + pair[1]
        for pair in high[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [low[0] + high[0]] + low[1:] + high[1:])

    return heap[0]



def read_text_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    return text

#Путь до файла с текстом
input_file_path = "input_text.txt"

#Текст, который хранится в файле
input_text = read_text_from_file(input_file_path)

# Подсчет частоты символов в тексте
symbols_freq = defaultdict(int)        

#Заполнение словаря частотами символов
for symbol in input_text:
    symbols_freq[symbol] += 1