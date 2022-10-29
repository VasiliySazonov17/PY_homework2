# Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр. Через строку нельзя решать.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11
     
def split_int(number):

    row = []          
    while number > 10:

        split_num = number % 10
        row.append(split_num)
        number = int(number / 10)

    else:
        row.append(number)

    print(row)
    return row


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


def split_number(number):

    if (float == type(number)):

        while(number % 10 != 0):
            number *= 10
        number /= 10
        number = int(number)
    
    row = []          
    while number > 10:

        split_num = number % 10
        row.append(split_num)
        number = int(number / 10)

    else:
        row.append(number)
        
    return row

        
def sum_row(row):

    sum_row = 0

    for i in row:
        sum_row += i
    
    return sum_row


print("Input number: ") 
number = input()
number = check_type(number)
row = split_number(number)
print(sum_row(row))

#number = convert_type(number)
# number = check_type(number)



# check_type(number)



