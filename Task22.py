"""
Задача 22: 
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, 
которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
"""
from random import randint

n = int(input('Введите число n: '))
m = int(input('введите число m: '))
list_1 = []
list_2 = []


for i in range(n):
    list_1.append(randint(0, 10))
for i in range(m):
    list_2.append(randint(0, 10))

set_1 = set(list_1)
set_2 = set(list_2)

set_3 = set_2.intersection(set_1)
print(*list_1)
print(*list_2)
print(*set_3)