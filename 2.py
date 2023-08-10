# Задача 16:
# list_1 = [1, 2, 3, 4, 5]
# k = 3
# count=0
# for i in range(len(list_1)):
#     if list_1[i] == k:
#         count+=1
# print(count)

# 2 Mode

# count = 0
# for i in range(len(list_1)):
#     if list_1[i] == k:
#         count += 1
# print(count)


# Задача 18: 
# list_1 = [1, 2, 3, 4, 5]
# k = 6
# min=abs(k-list_1[0])
# index=0
# for i in range(1, len(list_1)):
#     count=abs(k-list_1[i])
#     if count < min:
#         min=count
#         index=i
# print(list_1[index])

# 2 mode

# m = abs(k - list_1[0])  # модуль числа
# number = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - k):
#         m = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)

# Задача 20:
# dict = {1:'AEIOULNSTRАВЕИНОРСТ',
#       	2:'DGДКЛМПУ',
#       	3:'BCMPБГЁЬЯ',
#       	4:'FHVWYЙЫ',
#       	5:'KЖЗХЦЧ',
#       	8:'JXШЭЮ',
#       	10:'QZФЩЪ'}
# k = 'lizard'
# k=k.upper()
# print(sum([key for i in k for key, v in dict.items() if i in v]))

# 2 

# points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
# points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
# word = k.upper()  # переводим все буквы в верхний регистр
# count = 0
# for i in word:
#     if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
#         for j in points_en:
#             if i in points_en[j]:
#                 count = count + j
#     else:
#         for j in points_en:
#             if i in points_ru[j]:
#                 count = count + j
# print(count)