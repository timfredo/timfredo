class Player:
    def __init__(self,name,accuracy):
        self.name = name
        self.accuracy = accuracy

p1 = Player("Tim",30) # placeholder
p2 = Player("Vik",30) # placeholder
p3 = Player("Carton",30) # placeholder
p4 = Player("Adam",30) # placeholder

import pandas as pd

data = pd.read_csv('stats for csv.csv')

W = data.Player
data.ShotAverage = 1000 * data.ShotAverage
Y = data.ShotAverage

d = {}
i = 0
while i < len(W):
    d[data.Player[i]] = data.ShotAverage[i]
    i+=1



def onevone():
    
    print("Player Selection")
    for name,acc in d.items():
        print(name,acc)

    choose_player1 = input("Pick Player 1:")
    for name,acc in d.items():
        if name == choose_player1:
            z1 = name
            z2 = acc

    choose_player2 = input("Pick Player 2:")
    for name,acc in d.items():
        if name == choose_player2:
            q1 = name
            q2 = acc

    p1.name = z1
    p1.accuracy = z2
    p2.name = q1
    p2.accuracy = q2

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
        number = random.randint(1, 1000)
        number2 = random.randint(1, 1000)
        if (i % 2) == 0:
            if number <= y:
                cups = cups - 1
                i = i - 1
                if cups == 1:
                    print('%s has made the shot! %s has %d cup left.' % (n1,n1,cups))
                else:
                    print('%s has made the shot! %s has %d cups left.' % (n1,n1,cups))
            else:
                print('%s has missed the shot!' % n1)
        else:
            if number2 <= y2:
                cups2 = cups2 - 1
                i = i - 1
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

def twovtwo():
    
    print("Player Selection")
    for name,acc in d.items():
        print(name,acc)

    choose_player1 = input("Pick Team 1 Player 1:")
    for name,acc in d.items():
        if name == choose_player1:
            z1 = name
            z2 = acc

    choose_player2 = input("Pick Team 1 Player 2:")
    for name,acc in d.items():
        if name == choose_player2:
            q1 = name
            q2 = acc

    choose_player3 = input("Pick Team 2 Player 1:")
    for name,acc in d.items():
        if name == choose_player3:
            x1 = name
            x2 = acc

    choose_player4 = input("Pick Team 2 Player 2:")
    for name,acc in d.items():
        if name == choose_player4:
            w1 = name
            w2 = acc

    p1.name = z1
    p1.accuracy = z2
    p2.name = q1
    p2.accuracy = q2
    p3.name = x1
    p3.accuracy = x2
    p4.name = w1
    p4.accuracy = w2

    import random

    y = p1.accuracy
    n1 = p1.name
    cups = 15
    i = 1

    y2 = p2.accuracy
    n2 = p2.name
    cups2 = 15

    y3 = p3.accuracy
    n3 = p3.name

    y4 = p4.accuracy
    n4 = p4.name

    while cups > 0:
        i += 1
        number = random.randint(1, 1000)
        number2 = random.randint(1, 1000)
        number3 = random.randint(1,1000)
        number4 = random.randint(1,1000)
        if (i % 2) == 0:
            if number < y:
                cups = cups - 1
                print('%s has made the shot! Team 1 has %d cups left.' % (n1,cups))
            if number > y:
                print('%s has missed the shot!' % n1)
            if number2 < y2 and cups > 0:
                cups = cups - 1
                print('%s has made the shot! Team 1 has %d cups left.' % (n2,cups))
            if number2 > y2:
                print('%s has missed the shot!' % n2)
            if number < y and number2 < y2:
                i = i-1
                print('Team 1 has made both shots!')
        else:
            if number3 < y3:
                cups2 = cups2 - 1
                print('%s has made the shot! Team 2 has %d cups left.' % (n3,cups2))
            if number3 > y3:
                print('%s has missed the shot!' % n3)
            if number4 < y4 and cups2 > 0:
                cups2 = cups2 - 1
                print('%s has made the shot! Team 2 has %d cups left.' % (n4,cups2))
            if number4 > y4:
                print('%s has missed the shot!' % n4)
            if number3 < y3 and number4 < y4:
                i = i-1
                print('Team 2 has made both shots!')

        if cups <= 0:
            print('It is over! Team 1: %s and %s have won!' % (n1,n2))    
        if cups2 <= 0:
            print('It is over! Team 2: %s and %s have won!' % (n3,n4))
            cups = 0


gamestart = int(input("Type 1 for 1 v 1 mode OR 2 for 2 v 2 mode:"))

if gamestart == 1:
    onevone()
elif gamestart == 2:
    twovtwo()  
else:
    print("Not valid! Choose 1 OR 2!")
