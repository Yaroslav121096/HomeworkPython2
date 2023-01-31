# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

def Random(args):
    import random
    for i in range(number):
        numbers.append(random.randint(0, 1))


number = int(input("Введите количество монет: "))
numbers = []
Random(numbers)
print(numbers)
count0 = 0
count1 = 0
for i in range(number):
    if numbers[i] == 1:
        count1 += 1
    else:
        count0 += 1
if count0 > count1:
    print(count1)
else:
    print(count0)
