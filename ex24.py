#Задайте список из вещественных чисел. Напишите программу,
#которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
some_list0=[2.1, 3.12, 5.08, 4.001, 7.78]
some_list1=[]
Len=[]
for i in range (len(some_list0)):
    some_list1.append(str(some_list0[i]).split('.')[-1])
    Len.append(len(some_list1[i]))
for i in range (len(some_list0)):
    some_list0[i]=int(some_list0[i]*10**(max(Len)))%10**(max(Len))
kon=(max(some_list0)-min(some_list0))/10**(max(Len))
print(kon)