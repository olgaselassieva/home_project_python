a = int(input('Результат за 1 день: '))
b = int(input('Желаемый резултат: '))
c = 1
n = a
d = 0
i = 0
while n <= b:
    c = n * 10 / 100
    n = c + n
    i += 1
print('На', i + 1, 'день ваш результат будет достигнут')


