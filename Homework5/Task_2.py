# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
#

import random

# Игра на два игрока

# name_1 = str(input("Введите имя игрока_1: "))
# name_2 = str(input("Введите имя игрока_2: "))
# name_list = [name_1, name_2]
# lottery_num = random.randint(0, 1)
# print(f"Первым ходит {name_list[lottery_num]}")
#
#
# candies = 2021
# print(f"Есть {candies} конфет")
# count = 0
# while candies > 0:
#     count += 1
#     if count % 2 == 1:
#         candy_1 = int(input("Ход первого игрока: "))
#         if 0 < candy_1 < 29:
#             candies -= candy_1
#             if candies < 0:
#                 candies = 0
#                 print("Не думаю, что это законно, но ладно.")
#             elif candies == 0:
#                 candies = 0
#                 print("Конфет больше нет")
#         else:
#             print("Введите число больше 0, но меньше 29.")
#     else:
#         candy_2 = int(input("Ход второго игрока: "))
#         if 0 < candy_2 < 29:
#             candies -= candy_2
#             if candies < 0:
#                 candies = 0
#                 print("Не думаю, что это законно, но ладно.")
#             elif candies == 0:
#                 candies = 0
#                 print("Конфет больше нет")
#         else:
#             print("Введите число больше 0, но меньше 29.")
#     print(f"{candies} конфет осталось")
# if count % 2 == 1 and candies == 0:
#     print("Первый игрок выиграл")
# else:
#     print("Второй игрок выиграл")
#

# Игра против бота без интеллекта

# count = random.randint(0, 1)
# if count == 0:
#     print("Вы ходите первым.")
# else:
#     print("Первый ход за мной.")
#
# candies = 2021
# print(f"Есть {candies} конфет")
# while candies > 0:
#     count += 1
#     if count % 2 == 1:
#         candy_1 = int(input("Ваш ход: "))
#         if 0 < candy_1 < 29:
#             candies -= candy_1
#             if candies < 0:
#                 candies = 0
#                 print("Будем считать, что я ничего не видел.")
#             elif candies == 0:
#                 candies = 0
#                 print("Конфет больше нет")
#         else:
#             print("Введите число больше 0, но меньше 29.")
#
#     else:
#         comp_candy = random.randint(1, 10)
#         if candies >= comp_candy:
#             candies -= comp_candy
#             if candies > 0:
#                 print(f"Мой ход. Беру {comp_candy} конфет")
#             elif candies <= 0:
#                 print(f"Мой ход. Беру {comp_candy} конфет")
#                 candies = 0
#         else:
#             comp_candy = candies
#             candies = 0
#             print(f"Мой ход. Беру {comp_candy} конфет")
#
#     if candies > 0:
#         print(f"{candies} конфет осталось")
# # print(count)
# if count % 2 == 1 and candies == 0:
#     print("Вы выиграли")
# else:
#     print("Вы проиграли.")


# Игра против бота с интеллектом:

count = random.randint(0, 1)
if count == 0:
    print("Вы ходите первым.")
    n = 0
else:
    print("Первый ход за мной.")
    n = 1

candies = 2021
max_cand = 28
step = max_cand + 1

last_lst = step * int(candies / step)
lst = []
for i in range(step, last_lst + step, step):
    lst.append(i)

print(f"Есть {candies} конфет")
while candies > 0:
    count += 1
    if count % 2 == 1:
        candy_1 = int(input("Ваш ход: "))
        if 0 < candy_1 < 29:
            candies -= candy_1
            if candies < 0:
                candies = 0
                print("Будем считать, что я ничего не видел.")
            elif candies == 0:
                candies = 0
                print("Конфет больше нет")
        else:
            print("Введите число больше 0, но меньше 29.")

    else:
        if n != len(lst) and candies > 28:
            n += 1
            if candies < lst[-n]:
                n += 1
            comp_candy = candies - lst[-n]
            candies -= comp_candy
            print(f"Мой ход. Беру {comp_candy} конфет")
        elif n == len(lst):
            comp_candy = candies
            candies -= comp_candy
            print(f"Мой ход. Беру {comp_candy} конфет")
    if candies > 0:
        print(f"{candies} конфет осталось")
if count % 2 == 1 and candies == 0:
    print("Вы выиграли")
else:
    print("Вы проиграли.")
