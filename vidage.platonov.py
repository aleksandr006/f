from random import *
s=[]
def arvud_loendis():
    print("Данные:")
    n=abs(int(input("Сколько целых чисел генерируем в список? => ")))
    mini=int(input("Введите минимальное число диапазона => "))
    maxi=int(input("Введите максимальное число диапазона => "))
    if mini>=maxi:#mini=100, maxi=5-> mAXI=100
        mini,maxi=vahetus(mini,maxi)
        generator(n,loend,a,b)
        print()
        print("Результаты:")
        print("Полученный список от",mini,"до",maxi,s)
        s.sort()
        print("Отсортированный список",s)
        jagamine(s,pos,neg,null)
        print("Список положительных элементов",pos)
        print("Список отрицательных элементов",neg)
        print("Список нулевых элементов",null)
        kesk=keskmine(pos)
        lisamine(s,kesk)
        print("Среднее положительных:",kesk)
        kesk=keskmine(neg,n)
        lisamine(s,kesk)
        print("Среднее отрицательных:",kesk)
        print("Добавляем средние в изначалный массив:")
        print(s)
def vahetus(a:int,b:int):
    """kui min suuurim kui max siis vahetame neid omavahel
    :parem :  int a:minimalne arv, mis on suurem kui max
    :parem int b:maximalne arv, mis on väikesem kui mi
    :trype : int, int
    """
    abi=a
    a=b
    b=abi
    return a,b
    

def generator(n:int,loend,a:int,b:int):
    """
    """
    for i in range (n):
        loend.append(randint(a,b))
def jagamine(loend:list,p:list,n:list,nol:list):
    """сортирует по спискам если больше нуля то в один если меньше то в другой
    """
    for el in loend:
        if el>0:
            p(append(el))
        elif el<0:
            n(append(el))
        else:
            nol(append(el))

def keskmine(loend,n):
    n=len(loend)
    if n==0:
        kesk=0
    else:
        sum=0
        for i in loend:
            sum+=i
        kesk=round(sum/n,2)
    return kesk

def lisamine(loend,el):
    loend.append(el)
    loend.sort()
arvud_loendis()