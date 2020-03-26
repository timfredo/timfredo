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
    # print(i)
    if (i % 2) == 0:
        # print('Player 1 number is %d' % number)
        if number < y:
            cups = cups - 1
            #i = i - 1
            print('Team 1 has %d cups left' % cups)
        if number11 < y:
            cups = cups - 1
            print('Team 1 has %d cups left' % cups)
        if number < y and number11 < y:
            i = i-1
            print('Team 1 has made both shots!')
            #print(number)
            #print(number11)
    else:
        # print('Player 2 number is %d' % number2)
        if number2 < y2:
            cups2 = cups2 - 1
            #i = i - 1
            print('Team 2 has %d cups left' % cups2)
        if number21 < y2:
            cups2 = cups2 - 1
            print('Team 2 has %d cups left' % cups2)
        if number2 < y2 and number21 < y2:
            i = i-1
            print('Team 2 has made both shots!')
            #print(number2)
            #print(number21)
    if cups2 <= 0:
        print('It is over! Player 2 has won!')
        cups = 0
