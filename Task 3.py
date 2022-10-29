# Задача 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой. 
# COUNT или FIND или SPLIT нельзя юзать! говорил же на семинаре.

def create_array_str(str):

    array = []
    assistant_str = ''

    for i in str:
        if(' ' != i and ',' != i):
            assistant_str += i

        elif(assistant_str != ''):
            array.append(assistant_str)
            assistant_str = ''

        else:
            continue

    array.append(assistant_str)

    return array


def common_words(array1, array2):

    count = 0

    if (len(array1) <= len(array2)):
        for i in array1:
            if (i in array2):
                count += 1
            else:
                continue
    else:
        for i in array2:
            if (i in array1):
                count += 1
            else:
                continue

    print(count)


    
string_one = input('Ipnut string one: ')
string_two = input('Ipnut string two: ')
array_str1 = create_array_str(string_one)
array_str2 = create_array_str(string_two)
common_words(array_str1, array_str2)