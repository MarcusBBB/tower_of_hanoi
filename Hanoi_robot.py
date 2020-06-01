def move(x,y):
    print("move disc from {} to {}!".format(x, y))

def hanoi(n, f, h, t):
    if n == 0:
        pass
    else:
        hanoi(n-1, f, t, h)
        move(f, t)
        hanoi(n-1, h, f, t)


hanoi(3, 1, 2, 3)
