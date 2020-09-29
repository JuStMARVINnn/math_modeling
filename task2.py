import numpy as np

arr = np.zeros(5)

for i in range(4):
    arr[i] = float(input("Элемент {0} : ".format(i)))
print(arr)

pos = int(input("Позиция : "))
val = float(input("Значение : "))

arr_copy = arr
arr_copy[pos] = val
for i in range(pos, 4, 1):
    arr_copy[i+1] = arr[i]
print(arr_copy)