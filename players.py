class Player:
    def __init__(self,name,accuracy):
        self.name = name
        self.accuracy = accuracy

p1 = Player("Tim",30)
p2 = Player("Vik",30)

#import sys
#sys.stdout = open('output.txt','wt')

print("%s has an accuracy of %d" % (p1.name,p1.accuracy))
print("%s has an accuracy of %d" % (p2.name,p2.accuracy))

import random

y = p1.accuracy
n1 = p1.name
cups = 15
i = 1

y2 = p2.accuracy
n2 = p2.name
cups2 = 15

while cups > 0:
    i += 1
    number = random.randint(1, 100)
    number2 = random.randint(1, 100)
    if (i % 2) == 0:
        if number <= y:
            cups = cups - 1
            #i = i - 1
            if cups == 1:
                print('%s has made the shot! %s has %d cup left.' % (n1,n1,cups))
            else:
                print('%s has made the shot! %s has %d cups left.' % (n1,n1,cups))
        else:
            print('%s has missed the shot!' % n1)
    else:
        if number2 <= y2:
            cups2 = cups2 - 1
            #i = i - 1
            if cups2 == 1:
                print('%s has made the shot! %s has %d cup left.' % (n2,n2,cups2))
            else:
                print('%s has made the shot! %s has %d cups left.' % (n2,n2,cups2))
        else:
            print('%s has missed the shot!' % n2)

    if cups <= 0:
        print('It is over! %s has won!' % n1)    
    if cups2 <= 0:
        print('It is over! %s has won!' % n2)
        cups = 0
