# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


my_str = 'Я люблю Джавуабв абви Питон'
print(f"{my_str} -> ", end="")
print(*list(filter(lambda word: "абв" not in word, my_str.split(" "))))


# my_str = 'Я люблю Джавуабв абви Питон'
# lst = my_str.split(" ")
# print(*[i for i in lst if "абв" not in i])