# 4. С клавиатуры вводится целое число. Необходимо вывести число, обратное введенному по порядку составляющих его цифр. 
# Например, если было введено число 12345, программа должна вывести пользователю на экран число 54321.

number = input('Enter the number: ')

reverse_number = []
new_number = ''

for n in number:
    reverse_number.insert(0, n)

for n in reverse_number:
    new_number += n

print(f'Перевернутый {new_number} ')
