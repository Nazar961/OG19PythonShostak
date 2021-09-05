from random import*

def lst(l, b, c):
    global numbers
    for i in range(l):
        numbers.append(randint(b, c))
    print('Список:',numbers)
    print()

    a = int(input("Введіть значення від 0 до max номеру в списку = "))
    numbers[a] = a
    print("Змінений список:", numbers)

l = int(input("Введіть довжину списку l = "))
print()
print('Введіть межі списку :')
b = int(input("Найменше значення b = "))
c = int(input("Найбільше значення c = "))
numbers = []
lst(l, b, c)
