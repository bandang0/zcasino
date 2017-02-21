"""Core functions module for the zcasino program."""

def welcome():
    print """
    Welcome to the Z Casino, where you can make a fortune by playing
    the roulette!
    """

def tellRules():
    print """
        The rules here are simple. You'll choose an initial amount of money
    to play with, then at each turn you'll bet a certain amount
    of money and choose a number between 1 and 50, even numbers are red
    and odd numbers are black.
        Then we'll roll the roulette. If the ball ends up on the number you
    chose, you'll gain three times your bet. If not, either it ends up on
    a number the same color as yours and you'll gain half your bet, either
    the colors are different and you'll loose your bet.
    """

def start():
    print "Alright let's get random!"

def askMoney(): # initial amount (when you get to the casino)
    print "So how much money do you want to play with?"
    money = -1
    while money < 0:
        print "You have to enter a positive integer.",
        ans = raw_input()
        try :
            money = int(ans)
        except ValueError :

            money = -1
            continue

    return money


def askBet(money):  # how much do you bet?
    print "\nHow much do you want to bet this time?"
    bet = 0
    while bet > money or bet <1:
        print "At least 1$ and no more than all you have!",
        ans = raw_input()
        try :
            bet = int(ans)
        except ValueError :
            bet = 0
            continue

    if bet == money:
        print "Alright, all in!"

    return bet

def askChoice():
    print "What number are you betting on (between 1 and 50)?"
    choice = 0
    while choice > 50 or choice < 1:
        print "Please enter an integer between 1 and 50.",
        ans = raw_input()
        try :
            choice = int(ans)
        except ValueError :
            choice = 0
            continue

    return choice - 1

def sameNumber(bet):
    print "Congrats you got the same number!"
    print "You get your bet back (it's %d$) plus 2 times!" % bet


def sameColor(bet):
    print "Nice you got the same color!"
    print "You get your bet back (it's %d$) plus one half!" % bet

def noGain(bet):
    print "Sorry man, wrong color and wrong number."
    print "You lost your bet of %d$." % bet

def noMoreMoney():
    print "Sorry my friend, looks like you're bankrupt,",
    print "come back some other time!"

def tellState(money):
    print "You currently have %d$." % money

def askExit():
    print "Would you like to continue playing?",
    ans = raw_input()
    if ans == '' or ans[0] == 'y' or ans[0] == 'Y':
        return False
    else :
        return True

def goodbye(init_money,money):
    print "So sad to see you go!"
    if money > 0:
        print "You're leaving with %d$ (you started with %d$)." % (money,
                                                                init_money)
