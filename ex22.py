#Задайте список из нескольких чисел. Напишите программу, 
#которая найдёт сумму элементов списка, стоящих на нечётной позиции.
some_list=[2, 3, 5, 9, 3]
sum=0
i=1
while i <= (len(some_list)-1): #нумерация идет с нуля поэтому из длинны надо вычесть 1
    sum+=some_list[i]
    i=i+2
print(some_list,"->",sum) 