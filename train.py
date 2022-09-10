import numpy as np
import re


def reading():
    name_path = str(input('Введите имя файла из которого делается модель: '))
    f = open('data/{}'.format(name_path))
    text = ''
    for line in f.readlines():
        text += str(line)
    f.close()
    return text


def formatting(text):
    text = text.lower()
    text = text.strip()
    text = re.split("[^a-zа-яё]+", text)
    return text


def tokenization(text):
    dictionary = {}
    for i in range(len(text)-1):
        if dictionary.get(text[i],0):
            pointer = dictionary.get(text[i])
            pointer.append(text[i+1])
            dictionary[text[i]]=pointer
        else:
            dictionary[text[i]]=[text[i+1]]
    return dictionary


def save(token):
    name_file = str(input('введите имя файла модели: '))
    return np.save('data/{}.npy' .format(name_file), token)


text = reading()
text_f = formatting(text)
token = tokenization(text_f)
name_file = save(token)
