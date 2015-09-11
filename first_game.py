#This program draws a random number 0-100 and gives to player three choices for chance


from random import randint

right_choice = randint(0,101)

while 1:
    bet = []
    for x in range(3):
        bet.append(int(input("Insert your bet Nº%i: " %(x+1))))
    if right_choice in bet:
        print("The number is %s! Congratulations, you win!" %right_choice)
        break
    else:
        for p in bet:
            print("High!" if p > right_choice else "Low!")
            bet = []
