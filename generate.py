import numpy as np
import random


def load():
    name_file = str(input('введите имя файла модели: '))
    read_dictionary = np.load('data/{}.npy' .format(name_file), allow_pickle=True).item()
    return read_dictionary


def generation(model):
    read_dictionary = model
    sequence = ''
    length_text = int(input('введите длину генерируемой последовательности: '))
    for i in range(length_text):
        if i == 0:
            elem_ahead = random.choice(list(read_dictionary.keys()))
            sequence += elem_ahead
            sequence += ' '
        else:
            elem_now = random.choice(read_dictionary.setdefault(elem_ahead))
            sequence += elem_now
            sequence += ' '
            elem_ahead = elem_now
    return sequence


model = load()
print(generation(model))
