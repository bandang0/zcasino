# ZCasino program main

from random import randrange
from math import ceil
from core import *

welcome()
tellRules()
init_money = askMoney()  # initial amount (when you get to the casino)
start()
money = init_money


while True:
    bet = askBet(money)  # how much do you bet?
    money = money - bet
    choice = askChoice()    # on what do you bet?
    outcome = randrange(50) # random number

    if choice == outcome :  # right number
        sameNumber(bet)
        money = ceil(money + 4*bet)
    elif (choice - outcome) % 2 == 0 :  # right color
        sameColor(bet)
        money = ceil(money + 1.5*bet)
    else :                          # all wrong
        noGain(bet)

    if money <= 0 : # if no more money then bye!
        noMoreMoney()
        money = 0
        break

    tellState(money)    # how much you have
    exit = askExit()

    if exit == True :  # exit or no
        break


goodbye(init_money,money)
#exit(0)
