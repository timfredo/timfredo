import random

y = 30  # 30% shot accuracy
cups = 10
i = 1

y2 = 50 # 50% shot accuracy
cups2 = 10

while cups >0:
    i+=1
    number = random.randint(1,100)
    number2 = random.randint(1,100)
    #print(i)
    if (i % 2) == 0:
       #print('Player 1 number is %d' % number)
       if (number < y):
        cups = cups - 1
        i = i - 1
        print('Player 1 has %d cups left' % cups)
    else:
        #print('Player 2 number is %d' % number2)
        if (number2 < y2):
            cups2 = cups2 - 1
            i = i - 1
            print('Player 2 has %d cups left' % cups2)
    if (cups2 == 0):
        print('It is over! Player 2 has won!')
        cups = 0
        
