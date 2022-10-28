# Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр. Через строку нельзя решать.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

# def check_type(number):

#     if (float == type(number)):

#         while(float == type(number)):

#             number = number * 10
#             print(number)
#         print(number)

#     elif (int == type(number)):
#         print(number)

#     else:
#         print("error, input number")

        
# def split_number(number):

#     row = []          
#     while number > 10:

#         split_num = number % 10
#         row.append(split_num)
#         number = int(number / 10)

#     else:
#         row.append(number)

#     print(row)
#     return row

def check_type(number):

    count = 0
    for i in number:

        if ('.' == i):
            count += 1
    
    if (count == 0):
        number = int(number)
    else:
        number = float(number)

    return number


def convert_type(number):

    number = float(number)
    while (number % 10 != 0):
        number *= 10
    number = str(number)
    number = int(number)
    number /= 10
    return number

print("Input number: ") 
number = float(input())
#number = convert_type(number)
print(int(number%10))
# number = check_type(number)



# check_type(number)



