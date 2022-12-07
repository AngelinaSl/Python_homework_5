# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# Алгоритм сжатия данных:

# def compress_string (first_str: str):
#     second_str = ''
#     my_lst = [0]
#     for i in range(1, len(first_str)):
#         if first_str[i] != first_str[i - 1]:
#             my_lst.append(i)
#
#     my_lst.append(len(first_str))
#     for j in range(0, len(my_lst) - 1):
#         second_str += (first_str[my_lst[j]:my_lst[j + 1]]) + ' '
#
#     second_str = second_str[:-1]
#     splitting_list = second_str.split(" ")
#     compressed_str = ''
#     for k in range(0, len(splitting_list)):
#         compressed_str += str(len(splitting_list[k])) + str(splitting_list[k][0])
#     return compressed_str
#
#
# with open('File_4.txt', "r") as origin_doc:
#     original_str = origin_doc.readline()
# print(original_str)
# print(compress_string(original_str))
# with open("Compress_File_4.txt", 'w') as compress_doc:
#     compress_doc.write(compress_string(original_str))


# Алгоритм восстановления данных

# def recovery_string(first_lst: list):
#     second_str = ''
#     i = 0
#     while i < len(first_lst):
#         second_str += int(first_lst[i]) * first_lst[i + 1]
#         i += 2
#     return second_str
# 
# 
# with open("Compress_File_4.txt", 'r') as compress_doc:
#     compress_lst = list(compress_doc.readline())
# print(compress_lst)
# 
# print(recovery_string(compress_lst))
# with open("Recovery_File_4.txt", 'w') as origin_doc:
#     origin_doc.write(recovery_string(compress_lst))
