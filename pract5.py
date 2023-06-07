def main(x=None, y=None):
    x = x or []
    y = y or []
    res = 0
    n = len(x)
    for i in range(n):
        res += (x[i] ** 3 - 92 * y[n - 1 - i] ** 2 - 92 * x[n - 1 - i]) \
               ** 7 / 80
    return 11 * res


print(main([0.65, -0.73, 0.8, 0.69, 0.55], [0.14, -0.34, 0.5, -0.08, 0.39]))
