from random import*

def lst(l, b, c):
    global numbers
    for i in range(l):
        numbers.append(randint(b, c))
    print('Список: ',numbers)
    print()

def serch(a):
    f = 0
    for i in range(l):
        if numbers[i] == a :
            print('Число', a, 'знаходиться в списку під номером',i)
            f = 1
    if f == 0 :
        print('Цього числа в списку не має')

numbers = []
l = int(input("Введіть довжину списку l = "))
print()
print('Введіть межі списку :')
b = int(input("Найменше значення b = "))
c = int(input("Найбільше значення c = "))
lst(l, b, c)
a = int(input("Введіть число яке хочете знайти a = "))
print()

serch(a)
