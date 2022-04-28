

a = int(input('input seconds:'))
while a > 86400:
    a = int(input('input seconds<86400:'))
    break
if a <= 86400:
      hh = a // 3600
      b = a % 3600
      mm = b // 60
      ss = b % 60

print(hh, ':', mm, ':', ss)








