import numpy as np

def fib(n):
        a = 0
        b = 1
        c = 0
        if n == 0:
            return 0
        elif n > 0:
            for i in np.arange(2, n, 1):
                c = a + b
                a = b
                b = c
            return c
        else:
            for i in np.arange(n, -2, 1):
                c = a - b
                a = b
                b = c
            return c

print(fib(-6))