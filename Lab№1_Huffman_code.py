import heapq #Подключени библиотеки для создания дерева
from collections import defaultdict #

# Функция для построения дерева Хаффмана на основе частоты символов
def build_huffman_tree(symbols_freq):
    # Создаем начальную кучу (heap), где каждый элемент - список с весом и символом
    heap = [[weight, [symbol, ""]] for symbol, weight in symbols_freq.items()] 

    # Преобразуем список heap в мин-кучу (по весу символов)
    heapq.heapify(heap)

    # Пока в куче есть больше одного элемента
    while len(heap) > 1:
        # Извлекаем два элемента с наименьшими весами
        low = heapq.heappop(heap)
        high = heapq.heappop(heap)

        # Обновляем код символов внутри low и high, добавляя "0" и "1" соответственно
        for pair in low[1:]:
            pair[1] = '0' + pair[1]
        for pair in high[1:]:
            pair[1] = '1' + pair[1]
            
        # Создаем новый элемент, представляющий собой сумму весов low и high,
        # и объединение символов и их кодов из low и high
        new_node = [low[0] + high[0]] + low[1:] + high[1:]

        # Добавляем новый элемент в кучу с обновленными данными
        heapq.heappush(heap, new_node)

    # По завершении цикла в куче остается только один элемент - корень дерева Хаффмана
    # Возвращаем этот корневой элемент, который представляет собой дерево Хаффмана
    # с префиксными кодами для всех символов
    return heap[0]


# Функция для чтения текста из файла
def read_text_from_file(file_path):
    # Открываем файл по заданному пути в режиме чтения ("r") с указанием кодировки UTF-8
    with open(file_path, "r", encoding="utf-8") as file:
        # Читаем содержимое файла и сохраняем его в переменной text
        text = file.read()
    # Возвращаем прочитанный текст
    return text

# Функция для генерации Хаффмановских кодов на основе построенного дерева Хаффмана
def create_huffman_codes(huffman_tree):
    # Инициализируем пустой словарь для хранения символов и их соответствующих Хаффмановских кодов
    huffman_codes = {}
    
    # Обходим пары символов и кодов в дереве Хаффмана
    for pair in huffman_tree[1:]:
        symbol, code = pair
        # Добавляем символ и его Хаффмановский код в словарь
        huffman_codes[symbol] = code

    # Возвращаем словарь Хаффмановских кодов
    return huffman_codes



#Путь до файла с текстом
input_file_path = "input_text.txt"

#Текст, который хранится в файле
input_text = read_text_from_file(input_file_path)

# Подсчет частоты символов в тексте
symbols_freq = defaultdict(int)        

#Заполнение словаря частотами символов
for symbol in input_text:
    symbols_freq[symbol] += 1

#Создание дерева для генерации кодов Хаффмана
huffman_tree = build_huffman_tree(symbols_freq)

#Генерация кодов Хаффмана