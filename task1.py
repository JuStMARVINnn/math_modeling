import numpy as np

n = int(input("Кол-во строк : "))
m = int(input("Кол-во столбцов : "))

arr1 = np.ndarray(shape=(n, m))
arr2 = np.ndarray(shape=(n, m))
arr3 = np.ndarray(shape=(n, m))

for i in range(n):
    for j in range(m):
        arr1[i, j] = float(input("Массив 1, строка {0}, столбец {1} : ".format(i, j)))
        arr2[i, j] = float(input("Массив 2, строка {0}, столбец {1} : ".format(i, j)))
        
        if arr1[i, j] > arr2[i, j]:
            arr3[i ,j] = arr1[i, j]
        else:
            arr3[i ,j] = arr2[i, j]

print(arr3)