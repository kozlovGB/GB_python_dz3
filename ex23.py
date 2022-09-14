#Напишите программу, которая найдёт произведение пар чисел списка.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import math
some_list=[2, 3, 5, 4, 7]
prod=[]
i=0
j=len(some_list)
while i < (math.ceil(len(some_list)/2)): #math.ceil- округление в большую сторону
    prod.append(some_list[i]*some_list[j-1])
    i+=1
    j-=1
print(some_list,"->",prod) 