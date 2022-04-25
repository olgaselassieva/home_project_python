while True:
    rev = int(input())
    cost = int(input())
    p = 0
    loss = 0
    if rev > cost:
        p = rev - cost
        print('Прибыль равна', p)
    elif rev < cost:
        loss = cost - rev
        print('Убыток равен', loss)
