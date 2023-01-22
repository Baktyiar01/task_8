# Функции 

# Напишите функцию, которая будет генерировать случайный пароль. 
# В пароле должно быть от 8 до 15 символов Юникода из диапазонов 
# 48-57 (цифры), 
# 65-90 (буквы латинского алфавита в верхнем регистре)
# и 97-122 (буквы латинского алфавита в нижнем регистре). 
# Сгенерируйте и выведите на экран три пароля.

import random

#создание списка цифр

list_of_numbers = []
list_of_numbers = [str(i) for i in range(10)]

#создание списка букв

list_of_letters = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W',\
'E','R','T','Y','U','I','O','P','A', 'S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']

#создание списка букв по таблице ASCII и их вывод

letters_from_table = [chr(i) for i in range(65, 90)] + [chr(i) for i in range(97, 123)]

#получение случайного элемента из списка

import string

letters = string.ascii_letters
digits = string.digits
symbol = string.punctuation
str_elements = letters + digits + symbol
random_symbol = random.choice(string.punctuation)
list_of_elements = letters_from_table + list_of_numbers

#получение комбинации случайных элементов

length = 10
password_list = [random.choice(list_of_elements) for i in range(length)]

# пароль + добавление символа

password = ' '

for elem in password_list:
    password = password + elem

result = password + random_symbol

print(result)


