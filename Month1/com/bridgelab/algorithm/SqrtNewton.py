def sqrt(c):
    t = c
    epsilon = 1e-15
    while abs(t - c / t) > epsilon:
        t = (c / t + t) / 2
    print("Square root of ", c, " is ", t)


n = int(input("Enter number : "))
sqrt(n)
