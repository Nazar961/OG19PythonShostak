def function (a, b, c):

    while a < b :
        a += c
        nums.append(a)
    else:
        a += c
        i = 0
        while i < len(nums):
            print(nums[i], "<=", b)
            i += 1
    print (a, ">", b)

nums = []
a = int(input("Введіть значення a = "))
b = int(input("Введіть значення b = "))
c = int(input("Введіть значення c = "))
nums.append(a)
function(a, b, c)
