import random
m = int(input('Количество строк m = '))
n = int(input('Количество столбцов n = '))
a = int(input('Диапазон чисел от a = '))
b = int(input('до b = '))
matrix_1=[[random.randint(a, b) for j in range(n)] for i in range(m) ]
print('Matrix 1: ')
for i in range(m):
 print(matrix_1[i])
matrix_2 = [ [ random.randint(a, b) for j in range(n)] for i in range(m) ]
print('Matrix 2: ')
for i in range(m):
 print(matrix_2[i])
result = [[matrix_1[i][j] + matrix_2[i][j]  for j in range
(len(matrix_1[0]))] for i in range(len(matrix_1))]
print("Результат сложения двух матриц Matrix 3: ")
for r in result:
 print(r)