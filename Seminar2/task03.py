print('Введите число рассматриваемых дней')
day = int(input())
k = 0
max = 0
for i in range (day):
    temp = int(input())
    if temp > 0:
        k += 1
    else :
        if max < k:
           max = k
           k = 0
print (max)               