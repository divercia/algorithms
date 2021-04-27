"""
Пользователь вводит две буквы.
Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

Блок-схема:
https://drive.google.com/file/d/17ErM4u8lSpCRuofieUOlq4TpffDv9K8U/view
"""

alphabet = 'abcdefghijklmnopqrstuvwxyz'
letter_1 = input('Введите первую букву: ')
letter_2 = input('Введите вторую букву: ')
position_1 = alphabet.find(letter_1) + 1
print(f'Первая буква {letter_1} стоит на позиции {position_1}')
position_2 = alphabet.find(letter_2) + 1
print(f'Вторая буква {letter_2} стоит на позиции {position_2}')
diff = abs(position_2 - position_1) - 1
print(f'Между буквами {letter_1} и {letter_2 } находится {diff} букв')
