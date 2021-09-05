def porahyi(a):
    p = 0
    while a > 0 :
        l = a % 10
        p += l
        a //= 10
    else:
        print(p)

a = int(input("Введіть значення a = "))

porahyi(a)