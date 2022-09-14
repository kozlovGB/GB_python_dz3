#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
def fib(n):
    if n==-1:
        return 1
    elif n==-2:
        return -1
    elif n<-2:
        return fib(n+2) - fib(n+1)
    elif n == 0:
        return 0
    elif n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)
res=[]
m=int(input('Введите число: '))
k=-m
while k!=m+1:
    res.append(fib(k))
    k+=1
print(res)