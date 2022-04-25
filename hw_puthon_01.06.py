while True:
    rev = int(input('Ваш доход: '))
    cost = int(input('Ваши расходы: '))
    p = 0
    loss = 0
    ren = 0
    pp = 0
    if rev > cost:
        p = rev - cost
        ren = int(p / rev * 100)
        print('Прибыль равна', p)
        print('Рентабельность равна', ren)
        people = int(input('Кол-во ваших сотрудников: '))
        pp = p // people
        print('Прибыль на 1 сотрудника равна', pp)

    elif rev < cost:
        loss = cost - rev
        print('Убыток равен', loss)