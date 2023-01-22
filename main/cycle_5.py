# 5. Выведите на экран таблицу умножения чисел от одного до девяти.

for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i * j:4}", end=' ')
    print()
