#0, 1, 1, 2, 3, 5, 8, 13, 21, 34
def fibanacci(n):
    a=0
    b=1
    if n <0:
        print("incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return b
    else:
        for i in range(1,n):
            c = a + b
            print(c)
            a = b
            b = c
        return b

print(fibanacci(9))
