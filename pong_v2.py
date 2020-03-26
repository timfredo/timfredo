import random

y = 30  # 30% shot accuracy
cups = 15
i = 1

y2 = 30  # 30% shot accuracy
cups2 = 15

while cups > 0:
    i += 1
    number = random.randint(1, 100)
    number11 = random.randint(1,100)
    number2 = random.randint(1, 100)
    number21 = random.randint(1,100)
    if (i % 2) == 0:
        if number < y:
            cups = cups - 1
            print('Team 1 has %d cups left' % cups)
        if number11 < y and cups > 0:
            cups = cups - 1
            print('Team 1 has %d cups left' % cups)
        if number < y and number11 < y:
            i = i-1
            print('Team 1 has made both shots!')
    else:
        if number2 < y2:
            cups2 = cups2 - 1
            print('Team 2 has %d cups left' % cups2)
        if number21 < y2 and cups2 > 0:
            cups2 = cups2 - 1
            print('Team 2 has %d cups left' % cups2)
        if number2 < y2 and number21 < y2:
            i = i-1
            print('Team 2 has made both shots!')
    if cups <= 0:
        print('It is over! Team 1 has won!')
    if cups2 <= 0:
        print('It is over! Team 2 has won!')
        cups = 0
