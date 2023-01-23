# Напишите программу, которая найдёт сумму четных элементов списка

data = [1, 3, 5, 34, 12, 1, 22, 545, 110, 13, 3, 7]
clean = list(filter(lambda i: not i % 2, data))
summ = sum(clean)
print(clean, '\n', summ)