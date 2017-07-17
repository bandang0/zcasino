"""Main module for the zcasino program."""

from random import randrange
from math import ceil
import core

print core.welcome
print core.rules
init_money = core.askMoney()  # initial amount (when you get to the casino)
print core.start
money = init_money

while True:
    bet = core.askBet(money)  # how much do you bet?
    money = money - bet
    choice = core.askChoice()    # on what do you bet?
    outcome = randrange(50) # random number

    if choice == outcome :  # right number
        print core.sameNumber % bet
        money = ceil(money + 4*bet)
    elif (choice - outcome) % 2 == 0 :  # right color
        print core.sameColor % bet
        money = ceil(money + 1.5*bet)
    else :                          # all wrong
        print core.noGain % bet

    if money <= 0 : # if no more money then bye!
        print core.noMoreMoney
        money = 0
        break

    print core.tellState % money    # how much you have
    exit = core.askExit()

    if exit == True :  # exit or no
        break

core.goodbye(init_money, money)
