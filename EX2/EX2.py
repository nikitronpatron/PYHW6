# Напишите программу, которая возведет в квадрат каждый элемент строки

str = '1 3 4 65 3 32 4 15 86 33 25 12 11 12'.split()
data = map(int, str)
data = list(map(lambda i: i**2, data))
print(data)