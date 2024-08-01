# rows = 6
# # if you want user to enter a number, uncomment the below line
# # rows = int(input('Enter the number of rows'))
# # outer loop
# for i in range(rows):
#     # nested loop
#     for j in range(i):
#         # display number
#         print(i, end=" ")
#     # new line after each row
#     print("")
# #-------------------------


# # read test.txt
# with open("test.txt", "r") as fp:
#     # read all lines from a file
#     lines = fp.readlines()

# # open new file in write mode
# with open("new_file.txt", "w") as fp:
#     count = 0
#     # iterate each lines from a test.txt
#     for line in lines:
#         # skip 5th lines
#         if count == 4:
#             count += 1
#             continue
#         else:
#             # write current line
#             fp.write(line)
#         # in each iteration reduce the count
#         count += 1

# -----------------------------------------
# name, age, marks = input("Enter your Name, Age, Percentage separated by space ").split()
# print("\n")
# print("User Details: ", name, age, marks)

# ---------------------------------------
# import os

# path = "p.txt"


# def validator(a):
#     file_size = os.stat(a).st_size
#     if file_size == 0:
#         print("this file is empty")
#     else:
#         print("this file has data")


# validator(path)
# -----------------------------------------------------

# # first two numbers
# num1, num2 = 0, 1

# print("Fibonacci sequence:")
# # run loop 10 times
# for i in range(10):
#     # print next number of a series
#     print(num1, end="  ")
#     # add last two numbers to get next number
#     res = num1 + num2

#     # update values
#     num1 = num2
#     num2 = res

# -----------------------------------------------------


# num = int(input("dame un numero: "))


# def factorial(num):
#     fact = 1
#     for i in range(1, num + 1):
#         fact *= i
#     return fact


# print(factorial(num))


# # ---------------------------------------------------


# num = int(input("dame un numero: "))


# def reverser(num):
#     num_str = str(num)  # Convert the integer to a string
#     reversed_str = num_str[::-1]  # Reverse the string
#     new_number = int(reversed_str)  # Convert the reversed string back to an integer
#     return new_number


# print(reverser(num))

# # ---------------------------------------------------


# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


# def oddnator(array):
#     odd = []
#     for i, value in enumerate(array):
#         if i % 2 == 0:
#             odd.append(value)
#     return odd


# print(oddnator(my_list))
# -------------------------


# rows = 5
# # if you want user to enter a number, uncomment the below line
# # rows = int(input('Enter the number of rows'))
# # outer loop
# col = 6

# for i in range(rows):

#     for j in range(i):
#         # display number
#         print("*", end=" ")

#     # new line after each row
#     print("")
# for i in range(rows):
#     # nested loop
#     col -= 1
#     for j in range(col):
#         # display number
#         print("*", end=" ")

#     # new line after each row
#     print("")
# ---------------------------------

# def func1(*args):
#     for i in args:
#         print(i)

# func1(20, 40, 60)
# func1(80, 100)

# #----------------------------------

# # function with default argument
# def show_employee(name, salary=9000):
#     print("Name:", name, "salary:", salary)

# show_employee("Ben", 12000)
# show_employee("Jessa")

# #---------------------------------
# recursive function
# def addition(num):
#     if num:
#         # call same function by reducing number by 1
#         return num + addition(num - 1)
#     else:
#         return 0

# res = addition(10)
# print(res)
# ----------------------------

# a = 4
# b = 30

# S = []


# def generator(min, max):
#     for i in range(min, max + 1):
#         if i % 2 == 0:
#             S.append(i)

#     return S


# print(generator(a, b))


# print(list(range(4, 30, 2)))

# ----------------------------------


# x = [200, 4, 6, 8, 24, 12, 2]


# def biggest(x):
#     x.sort()
#     a = x[-1]
#     return a


# print(biggest(x))

# x = [4, 6, 8, 24, 12, 2]
# print(max(x))

# #------------------------------


# str1 = "P@#yn26at^&i5ve"


# def counter(a):
#     chars = 0
#     digits = 0
#     symbols = 0

#     for i in a:
#         if i.isalpha():
#             chars += 1
#         elif i.isnumeric():
#             digits += 1
#         else:
#             symbols += 1

#     return chars, digits, symbols


# # Call the counter function with the provided string
# chars, digits, symbols = counter(str1)

# # Print the counts
# print(f"chars: {chars}, digits: {digits}, symbols: {symbols}")

# #------------------------------


# def balance(a):
#     x = set(a)

#     y = set(a)  # Convert the sorted list to a set

#     inter = x & y

#     inter_l = list(inter)
#     inter_l.sort()

#     z = list(a)
#     z.sort()

#     count = []

#     for i in inter_l:
#         num = z.count(i)
#         count.append(num)

#     keys = inter_l
#     values = count

#     my_dict = {k: v for k, v in zip(keys, values)}

#     return my_dict


# str1 = "Apple"
# print(balance(str1))

# # easiest way

# str1 = "Apple"

# # create a result dictionary
# char_dict = dict()

# for char in str1:
#     count = str1.count(char)
#     # add / update the count of a character
#     char_dict[char] = count
# print('Result:', char_dict)


# ------------------------------


# def balance(a):
#     x = set(a)

#     y = set(a)  # Convert the sorted list to a set

#     inter = x & y

#     inter_l = list(inter)
#     inter_l.sort()

#     z = list(a)
#     z.sort()

#     count = []

#     for i in inter_l:
#         num = z.count(i)
#         count.append(num)

#     keys = inter_l
#     values = count

#     my_dict = {k: v for k, v in zip(keys, values)}

#     return my_dict


# sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

# print(balance(sample_list))

# # better way
# sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
# print("Original list ", sample_list)

# count_dict = dict()
# for item in sample_list:
#     if item in count_dict:
#         count_dict[item] += 1
#     else:
#         count_dict[item] = 1

# print("Printing count of each item  ", count_dict)

# =-----------------------------------


# set eliminates repeated values

# lista = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3]

# lista1 = list(set(lista))


# print(lista1)
# ------------------------------


# def f(a):

#     w = []
#     for i in a:
#         if len(i) > 0:
#             w.append(i)

#     return w


# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# print(f(list1))


# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# # remove None from list1 and convert result into list
# res = list(filter(None, list1))
# print(res)

# ----------------------------


# dict1 = {"Ten": 10, "Twenty": 20, "Thirty": 30}
# dict2 = {"Thirty": 30, "Fourty": 40, "Fifty": 50}

# dict3 = dict1 + dict2

# print(dict3)
# # ----------------------

# while True:
#             try:
#                 ot = int(input("¿Cómo definirías tu nivel de actividad física semanal?\n\n1) Sedentario – poco o ningún ejercicio\n2) Poco activo – ejercicio/deporte leve 1-3 días/semana\n3) Activo con moderación – ejercicio/deporte moderado 3-5 días/semana\n4) Activo – ejercicio/deporte duro 6-7 días/semana\n5) Muy activo – ejercicio/deporte diario muy duro y trabajo físico o entrenamiento 2 veces al día\n\nSelecciona una de nuestras opciones colocando un número del 1 al 5: "))
#                 if ot < 1 or ot > 5:
#                     raise ValueError("Debes ingresar un número entre 1 y 5.")
#                 break
#             except ValueError:
#                 print('⛔Opción inválida. Por favor, ingresa un número del 1 al 5.⛔')
# ---------------------------------
# hand = [["5", "♥️"], ["8", "♦️"], ["Q", "♦️"]]


# def calculate_hand(hand):
#     score = []
#     for sublist in hand:
#         value = sublist[0]  # The value of the card (e.g., "5", "8", "Q")
#         if value in ["J", "Q", "K"]:
#             score.append(10)
#         else:
#             score.append(int(value))
#     return sum(score)


# # Calculate the score of the hand
# total_score = calculate_hand(hand)
# print(total_score)
