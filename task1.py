def power(a, n):
    if n == 0:
        return 1
    elif n > 0:
        number = a
        for i in range(1, n, 1):
            number *= a
        return number
    elif n < 0:
        return 1 / power(a, -n)
    

print(power(0, -1))
        
