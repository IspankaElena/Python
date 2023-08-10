# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно 
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

# N = int(input('Введите количество монет '))
# orel = reshka = 0
# for i in range(N):
#     x = int(input('Орел(1) или решка(0)? '))
#     if x == 1:
#         orel += 1
#     else:
#         reshka += 1
# if orel < reshka:
#     print(f'Переверните {orel} монет с орла на решку, их меньше всего')
# elif orel == reshka:
#     print(f'Количество орлов и решек одинаково, по {orel} штук')
# else:
#     print((f'Переверните {reshka} монет с решки на орла, их меньше всего'))
# print(count_o if count_o < count_r else count_r)

# 2 Mode

# n = int(input())
# count_o = 0
# count_r = 0
# for i in range(n):
#     x = int(input())
#     if x == 1:
#         count_o += 1
#     else:
#         count_r += 1
# if count_o < count_r:
#     print(count_o)
# else:
#     print(count_r)


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму 
# этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# s = int(input('Задай сумму двух чисел \n'))
# p = int(input('Задай произведение чисел \n'))
# for x in range(s):
#     for y in range(p):
#         if s == x + y and p == x * y:
#             print(f'первое число ="{x}", второе число ="{y}"')

# 2 mode

# def f(s, p):
#     for i in range(s + 1):
#         for j in range(s + 1):
#             if i + j == s and i * j == p:
#                 return i, j

# s = int(input())
# p = int(input())
# print(f(s, p))

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.

# N = abs(int(input('Введите число N ')))
# stop = 0
# P = 2
# for i in range(N):
#     if stop != 1:
#         P = P ** i
#         if P <= N:
#             print(P, end=' ')
#             P = 2
#         else:
#             stop = 1
#     else:
#         i = N

# n = int(input('Введи число N:'))
# i = 0
# while 2 ** i <= n:
#     print(f' 2 в степени {i} равна {2 ** i}')
#     i += 1

# mode 2
    
# n = int(input())
# i = 0
# while 2 ** i <= n:
#     print(2 ** i)
#     i += 1

