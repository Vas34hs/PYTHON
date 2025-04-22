# import random
# import datetime
# print("Добро пожаловать в игру <Унадай число>")
# print("Правила очень просты: ты пытаешься угадать число от 1 до 500, я даю тебе подсказку"
#       "от 1 до 500, я даю тебе подсказку")
# print("*"*11)
# user_choice_count = 0
# user_choice_time = datetime.datetime.now() #Текущее время
# print(f"Начало игры в {user_choice_time}")
# random_value = random.randint( 1,  500)
# # randit - функция для выбора
# # случайного числа в интервале
# while True:
#     user_choice_count += 1
#     value_user = int(input("Введите предпологаемое "
#                             " число: "))
#     if value_user == random_value:
#         print("Вы угадали число! Поздравляю!")
#         break
#     elif value_user < random_value:
#         print("Ваше число меньше загаданного")
#     elif value_user > random_value:
#         print("Ваше число больше загаданного")
#     print("*"*11)
# delta_time = datetime.datetime.now() - user_choice_time
# print(f"Статистика: \n Попыток ->{user_choice_count} \n Время->{delta_time}")
#
#


# for i in range(1, 7):
#     for i in range(1, 10):
#                     print("i * j"), end="")
#                 print()
#

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print("%4d" % (i * j), end="")
#         j += 1
#     print()
#     i += 1
#
#     a = 7
#     b = float(input("  второе число: "))
#
#     # Вычисления
#     umnojenie = a * 2
#
#
#     print("Умножение:", umnojenie)
#

# Задание 1

# value1 = int(input("Введите первое число: "))
# value2 = int(input("Введите второе число: "))
# for i in range(1,value2+1):
#     print(f"{value1}{" * "}{i} = {value1*i}")
#
# # Задание 2
#
# value1 = int(input("Введите первое число: "))
# value2
#
# #
# num = 7
# or i in range(1, 11):
#    print(f"{num} * {i} = {num * i}")
#                 print(num)



# задание 2
# while True:
#     #print('Курс сейчас USD = 88.10 руб')
#     a = float(input("Введите сколько хотите поменять РУБЛЕЙ: "))
#
#     EURO = a / 106.10
#     USD = a / 8.10
#     JUN = a / 16.10
#     user_choice = int(input("1. Обменять на USD \n 2. Обменять на EURO \n 3. Обменять на Юань \n0.Выход"))
#     if user_choice == 1:
#         print("Вы получите на USD:", USD)
#     elif user_choice ==2:
#         print("Вы получите на EURO:", EURO)
#     elif user_choice ==3:
#         print("Вы получите на ЮАНЬ:", JUN)
#     elif user_choice == 0:
#         break

# задание 3


while True:
    #print('Курс сейчас USD = 88.10 руб')
    a = float(input("Введите диапозон границ: "))

    # EURO = a / 106.10
    # # if value1 < 10 and value2 > 0:
    # #     print("Вы еще малыш!")
    # USD = a / 8.10
    # JUN = a / 16.10
    # user_choice = int(input("1. Обменять на USD \n 2. Обменять на EURO \n 3. Обменять на Юань \n0.Выход"))
    # if user_choice == 1:
    #     print("Вы получите на USD:", USD)
    # elif user_choice ==2:
    #     print("Вы получите на EURO:", EURO)
    # elif user_choice ==3:
    #     print("Вы получите на ЮАНЬ:", JUN)
    # elif user_choice == 0:
    #     break




#
# if value1 < 10 and value2 > 0:
#     print("Вы еще малыш!")
# elif value1 >= 10 and value2 < 21:
#     print("Вы подросток!")
# elif age >=21 and age < 45:
#     print("Вы молодеж!")
# elif age >=45 and age < 100:
#     print("Вы пенсионер!")
#
#
# break


# while True:
#     #print('Курс сейчас USD = 88.10 руб')
#     a = float(input("Введите сколько хотите поменять РУБЛЕЙ: "))
#
#     EURO = a / 106.10
#     USD = a / 8.10
#     JUN = a / 16.10
#     user_choice = int(input("1. Обменять на USD \n 2. Обменять на EURO \n 3. Обменять на Юань \n0.Выход"))
#     if user_choice == 1:
#         print("Вы получите на USD:", USD)
#     elif user_choice ==2:
#         print("Вы получите на EURO:", EURO)
#     elif user_choice ==3:
#         print("Вы получите на ЮАНЬ:", JUN)
#     elif user_choice == 0:
#         break




for i in range(1, 7):
    for i in range(1, 10):
                    print("i * j"), end="")
                print()
