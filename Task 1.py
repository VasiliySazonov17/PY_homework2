# Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр. Через строку нельзя решать.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11
def split_number(number):

    row = []

    while number > 10:

        split_num = number % 10
        row.append(split_num)
        number = int(number / 10)

    else:
        row.append(number)

    print(row)


print("Input number: ")
number = int(input())
split_number(number)



# def sum_number(number):
    

