"""
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
Блок-схема:
https://drive.google.com/file/d/1B5NSi_UxFaQjCgewra_hKlHW9Li19qmk/view?usp=sharing
"""

user_number = input('Введите число: ')
numbers_sum = int(user_number[0]) + int(user_number[1]) + int(user_number[2])
numbers_mult = int(user_number[0]) * int(user_number[1]) * int(user_number[2])
print(f'{numbers_sum = }')
print(f'{numbers_mult = }')
