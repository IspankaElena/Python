#арифм прогрессия
# a1 = int(input())
# d = int(input())
# n = int(input())
# #an = a1 + (n-1) * d.
# for i in range(a1,a1+(n-1)*d+1,d):
#     print(i,end = " ")


# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_n = int(input())
# max_n = int(input())
# print(list(filter(lambda x: min_n<=list_1[x]<=max_n, range(len(list_1)))))

# Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.

# Функция не должна ничего выводить, только возвращать значение.

# Пример:

# a = 3; b = 5 -> 243 (3⁵)
# a = 2; b = 3 -> 8

# Решение

# a = int(input('Введите число a \n'))
# b = int(input('Введите числ b \n'))

# def f(a, b):
#     if b == 0:
#         return 1
#     elif b == 1:
#         return a
#     elif b < 0:
#         return 1 / f(a, -b)
#     else:
#         return a * f(a, b-1)

# res = f(a, b)
# print(res)

# or

# def f(a, b):
#   if b == 0:
#     return 1
#   return f(a, b - 1) * a

# a = 3
# b = 5
# print(f(a, b))

# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# Функция не должна ничего выводить, только возвращать значение.

# Пример:
# sum(2, 2)
# # 4

# def sum(a, b):
#     if b == 0:
#         return a
#     elif a == 0:
#         return b
#     else:
#         return sum(a + 1, b - 1)
