# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def factorial_num (number):

    factorial = []
    add_num = 1
    for i in range(1, number+1):
        
        factorial.append(add_num*i)
        add_num *= i
        
    print(factorial)   


number = int(input("input number: "))
factorial_num (number)

