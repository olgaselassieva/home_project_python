while True:
  n = int(input())
  maxx = 0
  while n != 0:
     c = n % 10
     if c > maxx:
        maxx = c
     n = n // 10
  print('Самое большая цифра равна', maxx)