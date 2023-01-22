# 3. Даны три числа: 130, 25 и 70. Выведите на экран наименьшее из них, использовав для этого программную проверку.

a = 130
b = 25
c = 70

if a < b and a < c:
    print(a)
elif b < a and b < c:
    print(b)
elif c < a and c < b:
    print(c)
else:
    print()