#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
n = int(input('Введите десятичное число: '))
b = ''
while n > 0:
    b = str(n % 2) + b
    n = n // 2
print(b)#а можно решить в одну строчку(print(bin()))