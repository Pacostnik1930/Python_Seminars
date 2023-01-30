print('Введите целое неотрицательное число:')

n = int(input())
count = 2
factorial = 1 
if n == 0:
    factorial =1
else:
    while count <= n:
        factorial *= count
        count += 1
print(factorial)        