"""
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

Блок-схема:
https://drive.google.com/file/d/128v8xvG2k2BOlx0Yjc6Zs87JmAgYYiTJ/view?usp=sharing
"""

alphabet = 'abcdefghijklmnopqrstuvwxyz'
letter_index = int(input('Введите номер буквы в алфавите (от 1 до 26): '))
if 1 <= letter_index < 27:
    letter = alphabet[letter_index - 1]
    print(f'Индексу {letter_index} соответствует буква {letter}')
else:
    print(f'Буквы с индексом {letter_index} не существует.')
