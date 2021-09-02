def check(A, B):
    
    if A > B :
        print('A Більше')
    elif A < B :
        print('A Меньше')
    else :
        print('Числа рівні')

a = int(input("Введіть значення A = "))
b = int(input("Введіть значення B = "))

check(a, b)