import random
import time
from os import system, name
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def numberCheck(strong):
    for char in strong:
        if (char != '0' and char != '1' and char != '2' and char != '3' and char != '4' and char != '5' and char != '6' and char != '7' and char != '8' and char != '9' and char != '.'):
            return False
    return True

def diceAscii(face):
    #god help me
    if (face == 1):
        return("""
        -----------  
        |         |
        |    *    |
        |         |
        -----------
        """)
    if (face == 2):
        return("""
        -----------  
        | *       |
        |         |
        |       * |
        -----------
        """)
    if (face == 3):
        return("""
        -----------  
        | *       |
        |    *    |
        |       * |
        -----------
        """)
    if (face == 4):
        return("""
        -----------  
        | *     * |
        |         |
        | *     * |
        -----------
        """)
    if (face == 5):
        return("""
        -----------  
        | *     * |
        |    *    |
        | *     * |
        -----------
        """)
    if (face == 6):
        return("""
        -----------  
        | *     * |
        | *     * |
        | *     * |
        -----------
        """)
    else:
        return("Dice faces came up " + die1 + " and " + die2)
def menuGeneric(topText,bottomLeftText, bottomRightText):
    print(
        """
        |-------------------------------------------------------------------------------------------|
        | %s|
        | %s%s|
        |-------------------------------------------------------------------------------------------|
        """%(topText.ljust(90),(bottomLeftText).ljust(45), bottomRightText.rjust(45))
    )
#[0PASS,1DONTPASS,2COME,3DONTCOME,FOUR,FIVE,SIX,ANYSEVEN,EIGHT,NINE,TEN,11FIELD,12HARD4,13HARD6,14HARD8,15HARD10,16TWO,17THREE,18ELEVEN,19TWELVE,20ANYCRAPS,21COME4,22COME5,23COME6,24COME8,25COME9,26COME10]
def upgradeMenu(money,payouts,payoutUpgradeCosts):
    clear()
    menuGeneric("[1] Increase Payout of Pass Line by .01", "Current Payout: " + str(round(payouts[0],3)), "Cost: $" + str(round(payoutUpgradeCosts[0],2)))
    menuGeneric("[2] Increase Payout of Don't Pass Line by .01", "Current Payout: " + str(round(payouts[1],3)), "Cost: $" + str(round(payoutUpgradeCosts[1],2)))
    menuGeneric("[3] Increase Payout of all Come bets by .01", "Current Payout: " + str(round(payouts[2],3)), "Cost: $" + str(round(payoutUpgradeCosts[2],2)))
    menuGeneric("[4] Increase Payout of Four by .01", "Current Payout: " + str(round(payouts[4],3)), "Cost: $" + str(round(payoutUpgradeCosts[4],2)))
    menuGeneric("[5] Increase Payout of Five by .01", "Current Payout: " + str(round(payouts[5],3)), "Cost: $" + str(round(payoutUpgradeCosts[5],2)))
    menuGeneric("[6] Increase Payout of Six by .01", "Current Payout: " + str(round(payouts[6],3)), "Cost: $" + str(round(payoutUpgradeCosts[6],2)))
    menuGeneric("[7] Increase Payout of Any Seven by .01", "Current Payout: " + str(round(payouts[7],3)), "Cost: $" + str(round(payoutUpgradeCosts[7],2)))
    menuGeneric("[8] Increase Payout of Eight by .01", "Current Payout: " + str(round(payouts[8],3)), "Cost: $" + str(round(payoutUpgradeCosts[8],2)))
    menuGeneric("[9] Increase Payout of Nine by .01", "Current Payout: " + str(round(payouts[9],3)), "Cost: $" + str(round(payoutUpgradeCosts[9],2)))
    menuGeneric("[10] Increase Payout of Ten by .01", "Current Payout: " + str(round(payouts[10],3)), "Cost: $" + str(round(payoutUpgradeCosts[10],2)))
    menuGeneric("[11] Increase Payout of Field by .01", "Current Payout: " + str(round(payouts[11],3)), "Cost: $" + str(round(payoutUpgradeCosts[11],2)))
    menuGeneric("[12] Increase Payout of Hardways by .01", "Current Payout: " + str(round(payouts[12],3)), "Cost: $" + str(round(payoutUpgradeCosts[12],2)))
    menuGeneric("[13] Increase Payout of All Craps Bets (2,3,11,12) by .01", "Current Payout: " + str(round(payouts[16],3)), "Cost: $" + str(round(payoutUpgradeCosts[16],2)))
def onLine(value):
    if (value == 7):
        return("____________________________OFF________________________________________")
    else:
        if(value == 4):
            return("________ON_____________________________________________________________")
        if(value == 5):
            return("___________ON__________________________________________________________")
        if(value == 6):
            return("______________ON_______________________________________________________")
        if(value == 8):
            return("_________________ON____________________________________________________")
        if(value == 9):
            return("____________________ON_________________________________________________")
        if(value == 10):
            return("_______________________ON______________________________________________")

def clearTable(bets):
    emptyTable = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    return emptyTable

def hangmanStates(stateInt):
    if(stateInt == 0):
        print("""
|__________ 						
|/      | 
| 	    
|       
| 	
|
| 				              
------------- 	   
        """)
    elif(stateInt == 1):
        print("""
|__________ 						
|/      | 
|       O
|      
| 	
|
| 				              
------------- 	   
        """)
    elif(stateInt == 2):
        print("""
|__________ 						
|/      | 
|       O
|       |
| 	
|
| 				              
------------- 	   	   
        """)
    elif(stateInt == 3):
        print("""
|__________ 						
|/      | 
|       O
|      /|
| 	
|
| 				              
-------------   
        """)
    elif(stateInt == 4):
        print("""
|__________ 						
|/      | 
|       O
|      /|\\
| 
|
| 				              
-------------    
        """)
    elif(stateInt == 5):
        print("""
|__________ 						
|/      | 
|       O
|      /|\\
|      / 
|
| 				              
------------- 		   
        """)
    elif(stateInt == 6):
        print("""
|__________ 						
|/      | 
|       O
|      /|\\
|      / \\
|
| 				              
------------- 	    
        """)



def hangmanGuessLine(correctStringChecks, correctString):
    printString = ""
    i = 0
    for boole in correctStringChecks:
        if(boole == True):
            printString = printString + correctString[i]
        else:
            printString = printString + "_"
        i = i + 1
    print(printString)

def checkWin(correctString, correctStringChecks):
    for boole in correctStringChecks:
        if (boole == False):
            return False
    return True

def hangman(money, stateInt, correctString, correctStringChecks):
    clear()
    going = True
    lettersGuessed = []

    while (going):
        hangmanStates(stateInt)
        hangmanGuessLine(correctStringChecks,correctString)
        letterGuess = input("Enter Guess: ")
        if (letterGuess.isalpha()):
            lettersGuessed.append(letterGuess)
            guessString = "Guesses: "
            for letter in lettersGuessed:
                guessString = guessString + (letter + ",")
            print(guessString)
            changed = False
            i = 0
            for char in correctString:
                if (letterGuess == char):
                    correctStringChecks[i] = True
                    changed = True
                i = i + 1
            if (changed == False):
                stateInt = stateInt + 1
                if (stateInt >= 6):
                    hangmanStates(6)
                    print("You Lose! The correct word was %s"%(correctString) + ".")
                    time.sleep(3)
                    going = False
            elif (checkWin(correctString, correctStringChecks)):
                prize = random.randrange(4,50)
                hangmanGuessLine(correctStringChecks,correctString)
                print("Congratulations, You won %d dollars!!"%(prize))
                time.sleep(3)
                money = money + prize
                going = False
    return money

def tableTotal(bets):
    total = 0
    for bet in bets:
        total = total + bet
    return total

def runAway(bets, onValue):
    total = tableTotal(bets) 
    return (total)

def betCheck(die1,die2,onValue,bets,money,payouts, winnings):
    sum = die1+die2
    if(onValue != 7):
        if (sum == 7):
            money = money + (payouts[7]*bets[7])
            winnings = winnings + (payouts[7]*bets[7])  
            money = money + (payouts[1]*bets[1])
            winnings = winnings + (payouts[1]*bets[1])  
            bets = clearTable(bets)
            onValue = 7
        if (sum == onValue):
            money = money + (payouts[0]*bets[0])
            money = money + (bets[4] + bets[5] + bets[6] + bets[8] + bets[9] + bets[10])
            bets[4],bets[5],bets[6],bets[8],bets[9],bets[10] = 0,0,0,0,0,0
            winnings = winnings + (payouts[0]*bets[0])
            bets[0] = 0
            onValue = 7
        if (sum <= 6):
            money = money + (payouts[sum+17]*bets[sum+17])
            winnings = winnings + (payouts[sum+17]*bets[sum+17])
            bets[sum+17] = bets[2]
            bets[2] = 0
        elif (sum >= 8 and sum < 13):
            money = money + (payouts[sum+16]*bets[sum+16])
            winnings = winnings + (payouts[sum+16]*bets[sum+16])
            bets[sum+16] = bets[2]
            bets[2] = 0 
        else:
            print("dice sum is " + str(sum))
    else:
        if (sum == 7 or sum == 11):
            money = money + (payouts[0]*bets[0])
            winnings = winnings + (payouts[0]*bets[0])
            bets[0] = 0
        if (sum == 2 or sum == 3 or sum == 12):
            bets[0] = 0
    if(sum == 2):
        money = money + (payouts[16]*bets[16])
        money = money + (payouts[20]*bets[20])
        money = money + ((2*payouts[11])*bets[11])
        winnings = winnings + ((2*payouts[11])*bets[11])
        winnings = winnings + (payouts[16]*bets[16])
        winnings = winnings + (payouts[20]*bets[20])
    if(sum == 3):
        money = money + (payouts[17]*bets[17])
        money = money + (payouts[20]*bets[20])
        money = money + (payouts[11]*bets[11])
        winnings = winnings + (payouts[11]*bets[11])        
        winnings = winnings + (payouts[17]*bets[17])
        winnings = winnings + (payouts[20]*bets[20])
    if(sum == 4):
        money = money + (payouts[4]*bets[4])
        winnings = winnings + (payouts[4]*bets[4])
        money = money + (payouts[11]*bets[11])
        winnings = winnings + (payouts[11]*bets[11])    
        if (die1 == 2 and die2 == 2):
            money = money + (payouts[12]*bets[12])
            winnings = winnings + (payouts[12]*bets[12])
        else:
            bets[12] = 0
    if(sum == 5):
        money = money + (payouts[5]*bets[5])
        winnings = winnings + (payouts[5]*bets[5])
    if(sum == 6):
        money = money + (payouts[6]*bets[6])
        winnings = winnings + (payouts[6]*bets[6])
        if (die1 == 3 and die2 == 3):
            money = money + (payouts[13]*bets[13])
            winnings = winnings + (payouts[13]*bets[13])       
        else:
            bets[13] = 0  
    if(sum == 7):
        return (bets, money, onValue, winnings)      
    if(sum == 8):
        money = money + (payouts[8]*bets[8])
        winnings = winnings + (payouts[8]*bets[8])
        if (die1 == 4 and die2 == 4):
            money = money + (payouts[14]*bets[14])
            winnings = winnings + (payouts[14]*bets[14])
            winnings = winnings + (payouts[14]*bets[14])
        else:
            bets[14] = 0
    if(sum == 9):
        money = money + (payouts[9]*bets[9])
        winnings = winnings + (payouts[9]*bets[9])
        money = money + (payouts[11]*bets[11])
        winnings = winnings + (payouts[11]*bets[11])
    if(sum == 10):
        money = money + (payouts[10]*bets[10])
        winnings = winnings + (payouts[10]*bets[10])
        money = money + (payouts[11]*bets[11])
        winnings = winnings + (payouts[11]*bets[11])
        if (die1 == 5 and die2 == 5):
            money = money + (payouts[15]*bets[15])
            winnings = winnings + (payouts[15]*bets[15])
        else:
            bets[15] = 0
    if(sum == 11):
        money = money + (payouts[18]*bets[18])
        winnings = winnings + (payouts[18]*bets[18])
        money = money + (payouts[11]*bets[11])
        winnings = winnings + (payouts[11]*bets[11])
    if(sum == 12):
        money = money + ((3*payouts[11])*bets[11])
        winnings = winnings + ((3*payouts[11])*bets[11])
        money = money + (payouts[19]*bets[19])
        winnings = winnings + (payouts[19]*bets[19])
        money = money + (payouts[20]*bets[20])
        winnings = winnings + (payouts[20]*bets[20])
    bets[7] = 0
    bets[11] = 0
    bets[20] = 0
    bets[19] = 0
    bets[18] = 0
    bets[17] = 0
    bets[16] = 0
    return (bets, money, onValue, winnings)

def roll():
    die1 = random.randrange(0,5) + 1
    die2 = random.randrange(0,5) + 1
    return [die1,die2]
    
#[0PASS,1DONTPASS,2COME,3DONTCOME,FOUR,FIVE,SIX,ANYSEVEN,EIGHT,NINE,TEN,11FIELD,12HARD4,13HARD6,14HARD8,15HARD10,16TWO,17THREE,18ELEVEN,19TWELVE,20ANYCRAPS,21COME4,22COME5,23COME6,24COME8,25COME9,26COME10]

def setup(money, die1, die2, onValue, Off, bets, payouts, payoutUpgradeCosts, winnings):
    clear()
    passLineBet = 0
    if (money > 0.0):
        moneyString = str(round(money,2))
    else:
        moneyString = "0.00"        
    if (winnings > 0.0):
        winString = str(round(winnings,2))
    else:
        winString = "0.00"
    if (tableTotal(bets) > 0.0):
        wagerString = str(tableTotal(bets))
    else:    
        wagerString = "0.00"      
    if (type(moneyString) != str):
        return ("moneyERROR")
    if (type(winString) != str):
        return ("winERROR")
    if (type(wagerString) != str):
        return ("wagerERROR")  
    i = 0
    for bet in bets:
        if (type(bet) != float and type(bet) != int):
            print(i)
        i = i + 1
    #ASCII ART FOR CRAPS TABLE FROM https://everything2.com/title/Craps
    print("Bank: $" + moneyString + ("Last Win: $" + winString).rjust(30) + ("Total Wager: $" + wagerString).rjust(30) + diceAscii(die1) + diceAscii(die2) +
    """
   #######################################################################
   """
   + onLine(onValue) +
   """
 # | d||DC| 4| 5| 6| 8| 9|10| +---------------+ | 4| 5| 6| 8| 9|10|DC||d | #
 # |Po||__|__|__|__|__|__|__| |  sevens %d 1->5| | %d| %d| %d| %d| %d| %d| %d||oP| #
 # |An| ____________________  +===============+  ____________________ |nA| #
 # |St||     C O M E   %d    | |hard4 %d║hard6 %d| | %d| %d| %d| %d| %d| %d|  ||tS| #
 # |Sp||____________________| |-------╚╗------| |____________________||pS| #
 # |La| ____________________  |hard10 %d║hard8 %d 2___________________3 |aL| #
 # |Is||2  3 4  9  10 11  12| +===============+ |2  3 4  9  10 11  12||sI| #
 # |Ns||_______FIELD________| |two %d  |%d three| |_______%d____________||sN| #
 # |E |_____________________  |-----HORN------|  _____________________| E| #
 # |      DONT_PASS         | |eleven %d|twelve %d|    %d                |  |  #
 #  \________PASS_LINE______| +===============+ |________%d______________/  #
 #                            |  any  %d craps |                            #
  #                           +---------------+                           #
   #                               /ROLL\                                #
    #####################################################################        
    BETTING EXAMPLE: PASS_LINE 10 = $10 on PASS_LINE
    CLEAR removes all clearable bets

    Winning big? Want to win bigger? UPGRADE will get you where you want to get
    Outta money? Play some HANGMAN to recoup some of your losses!
    """%(bets[7],bets[4],bets[5],bets[6],bets[8],bets[9],bets[10],bets[3],bets[2],bets[12],bets[13],bets[21],bets[22],bets[23],bets[24],bets[25],bets[26],bets[15],bets[14],bets[16],bets[17],bets[11],bets[18],bets[19],bets[1],bets[0],bets[20]))
    winnings = 0
    bet = input("Enter Bet Type and Amount: ")
    betArray = []
    betArray = bet.split()
    if (bet != ""):
        betArray[0] = betArray[0].upper()
    if (len(betArray) == 2):
        if (numberCheck(betArray[1]) == False):
            setup(money, die1, die2, onValue, Off, bets, payouts, payoutUpgradeCosts, winnings)
        fbetArray = float(betArray[1])
        if (betArray[0] == "PASS_LINE" and fbetArray <= money and onValue == 7):
            money = money - fbetArray
            bets[0] = bets[0] + fbetArray
        if (betArray[0] == "DONT_PASS" and fbetArray <= money):
            money = money - fbetArray
            bets[1] = bets[1] + fbetArray
        if (betArray[0] == "FIELD" and fbetArray <= money):
            money = money - fbetArray
            bets[11] = bets[0] + fbetArray
        if (betArray[0] == "COME" and fbetArray <= money and onValue != 7):
            money = money - fbetArray
            bets[2] = bets[2] + fbetArray
        if (betArray[0] == "FOUR" and fbetArray <= money and onValue != 7 and onValue != 4):
            money = money - fbetArray
            bets[4] = bets[4] + fbetArray
        if (betArray[0] == "FIVE" and fbetArray <= money and onValue != 7 and onValue != 5):
            money = money - fbetArray
            bets[5] = bets[5] + fbetArray
        if (betArray[0] == "SIX" and fbetArray <= money and onValue != 7 and onValue != 6):
            money = money - fbetArray
            bets[6] = bets[6] + fbetArray
        if (betArray[0] == "EIGHT" and fbetArray <= money and onValue != 7 and onValue != 8):
            money = money - fbetArray
            bets[8] = bets[8] + fbetArray
        if (betArray[0] == "NINE" and fbetArray <= money and onValue != 7 and onValue != 9):
            money = money - fbetArray
            bets[9] = bets[9] + fbetArray
        if (betArray[0] == "TEN" and fbetArray <= money and onValue != 7 and onValue != 10):
            money = money - fbetArray
            bets[10] = bets[10] + fbetArray
        if (betArray[0] == "HARD4" and fbetArray <= money):
            money = money - fbetArray
            bets[12] = bets[12] + fbetArray
        if (betArray[0] == "HARD6" and fbetArray <= money):
            money = money - fbetArray
            bets[13] = bets[13] + fbetArray
        if (betArray[0] == "HARD8" and fbetArray <= money):
            money = money - fbetArray
            bets[14] = bets[14] + fbetArray
        if (betArray[0] == "HARD10" and fbetArray <= money):
            money = money - fbetArray
            bets[15] = bets[15] + fbetArray
        if (betArray[0] == "TWO" and fbetArray <= money):
            money = money - fbetArray
            bets[16] = bets[16] + fbetArray
        if (betArray[0] == "THREE" and fbetArray <= money):
            money = money - fbetArray
            bets[17] = bets[17] + fbetArray
        if (betArray[0] == "ELEVEN" and fbetArray <= money):
            money = money - fbetArray
            bets[18] = bets[18] + fbetArray
        if (betArray[0] == "TWELVE" and fbetArray <= money):
            money = money - fbetArray
            bets[19] = bets[19] + fbetArray
        if (betArray[0] == "ANY_CRAPS" and fbetArray <= money):
            money = money - fbetArray
            bets[20] = bets[20] + fbetArray
        if (betArray[0] == "SEVENS" and fbetArray <= money):
            money = money - fbetArray
            bets[7] = bets[7] + fbetArray
    if (len(betArray) == 1):
        if (bet != ""):
            bet = bet.upper()
        if(bet == "ROLL"):
            dice = roll()
            die1 = dice[0]
            die2 = dice[1]
            sum = die1 + die2
            (bets, money, onValue, winnings) = betCheck(die1, die2, onValue, bets, money, payouts, winnings)
            if (onValue == 7 and Off and sum > 3 and sum != 7 and sum < 11):
                onValue = die1+die2 
                Off = False
            elif (onValue == 7 and Off == False):
                Off = True
        if(bet == "CLEAR"):
            chipTotal = 0
            chipTotal = runAway(bets, onValue)
            if(not(Off)):
                saved = [bets[0],bets[1]]
                bets = clearTable(bets)
                bets[0] = saved[0]
                bets[1] = saved[1]
                money = money + float(chipTotal) - bets[0] - bets[1] 
            elif(Off):
                bets = clearTable(bets)
                money = money + float(chipTotal)
        if(bet == "UPGRADE"):
            UPGRADECONSTANT = 0.1
            selection = ""
            while (selection != "exit" and selection != "EXIT"):
                upgradeMenu(money, payouts,payoutUpgradeCosts)
                selection = input("Enter [bracketed] number to purchase upgrade or type EXIT to return: ")
                if (selection == "1" and money >= payoutUpgradeCosts[0]):
                    payouts[0] = payouts[0] + 0.01
                    money = money - payoutUpgradeCosts[0]
                    payoutUpgradeCosts[0] = payoutUpgradeCosts[0] + (UPGRADECONSTANT*payoutUpgradeCosts[0])
                if (selection == "2" and money >= payoutUpgradeCosts[1]):
                    payouts[1] = payouts[1] + 0.01
                    money = money - payoutUpgradeCosts[1]
                    payoutUpgradeCosts[1] = payoutUpgradeCosts[1] + (UPGRADECONSTANT*payoutUpgradeCosts[1])
                if (selection == "3" and money >= payoutUpgradeCosts[2]):
                    payouts[2] = payouts[2] + 0.01
                    payouts[21] = payouts[21] + 0.01
                    payouts[22] = payouts[22] + 0.01
                    payouts[23] = payouts[23] + 0.01
                    payouts[24] = payouts[24] + 0.01
                    payouts[25] = payouts[25] + 0.01
                    payouts[26] = payouts[26] + 0.01
                    money = money - payoutUpgradeCosts[0]
                    payoutUpgradeCosts[2] = payoutUpgradeCosts[2] + (UPGRADECONSTANT*payoutUpgradeCosts[2])
                if (selection == "4" and money >= payoutUpgradeCosts[4]):
                    payouts[4] = payouts[4] + 0.01
                    money = money - payoutUpgradeCosts[4]
                    payoutUpgradeCosts[4] = payoutUpgradeCosts[4] + (UPGRADECONSTANT*payoutUpgradeCosts[4])
                if (selection == "5" and money >= payoutUpgradeCosts[5]):
                    payouts[5] = payouts[5] + 0.01
                    money = money - payoutUpgradeCosts[5]
                    payoutUpgradeCosts[5] = payoutUpgradeCosts[5] + (UPGRADECONSTANT*payoutUpgradeCosts[5])
                if (selection == "6" and money >= payoutUpgradeCosts[6]):
                    payouts[6] = payouts[6] + 0.01
                    money = money - payoutUpgradeCosts[6]
                    payoutUpgradeCosts[6] = payoutUpgradeCosts[6] + (UPGRADECONSTANT*payoutUpgradeCosts[6])
                if (selection == "7" and money >= payoutUpgradeCosts[7]):
                    payouts[7] = payouts[7] + 0.01
                    money = money - payoutUpgradeCosts[7]
                    payoutUpgradeCosts[7] = payoutUpgradeCosts[7] + (UPGRADECONSTANT*payoutUpgradeCosts[7])
                if (selection == "8" and money >= payoutUpgradeCosts[8]):
                    payouts[8] = payouts[8] + 0.01
                    money = money - payoutUpgradeCosts[8]
                    payoutUpgradeCosts[8] = payoutUpgradeCosts[8] + (UPGRADECONSTANT*payoutUpgradeCosts[8])
                if (selection == "9" and money >= payoutUpgradeCosts[9]):
                    payouts[9] = payouts[9] + 0.01
                    money = money - payoutUpgradeCosts[9]
                    payoutUpgradeCosts[9] = payoutUpgradeCosts[9] + (UPGRADECONSTANT*payoutUpgradeCosts[9])
                if (selection == "10" and money >= payoutUpgradeCosts[10]):
                    payouts[10] = payouts[10] + 0.01
                    money = money - payoutUpgradeCosts[10]
                    payoutUpgradeCosts[10] = payoutUpgradeCosts[10] + (UPGRADECONSTANT*payoutUpgradeCosts[10])
                if (selection == "11" and money >= payoutUpgradeCosts[11]):
                    payouts[11] = payouts[11] + 0.01
                    money = money - payoutUpgradeCosts[11]
                    payoutUpgradeCosts[11] = payoutUpgradeCosts[11] + (UPGRADECONSTANT*payoutUpgradeCosts[0])
                if (selection == "12" and money >= payoutUpgradeCosts[12]):
                    payouts[12] = payouts[12] + 0.01
                    payouts[13] = payouts[13] + 0.01
                    payouts[14] = payouts[14] + 0.01
                    payouts[15] = payouts[15] + 0.01
                    money = money - payoutUpgradeCosts[12]
                    payoutUpgradeCosts[12] = payoutUpgradeCosts[12] + (UPGRADECONSTANT*payoutUpgradeCosts[12])
                if (selection == "13" and money >= payoutUpgradeCosts[16]):
                    payouts[16] = payouts[16] + 0.01
                    payouts[17] = payouts[17] + 0.01
                    payouts[18] = payouts[18] + 0.01
                    payouts[19] = payouts[19] + 0.01
                    payouts[20] = payouts[20] + 0.01
                    money = money - payoutUpgradeCosts[16]
                    payoutUpgradeCosts[16] = payoutUpgradeCosts[16] + (UPGRADECONSTANT*payoutUpgradeCosts[16])
        if(bet == "HANGMAN"):
            lineCount = 0
            file = open('hangmanwords.txt')
            content = file.readlines()
            correctString = content[random.randrange(0,853)]
            correctStringChecks = []
            state = 0
            for char in correctString:
                if (char.isalpha()):
                    correctStringChecks.append(False)
            money = hangman(money, state, correctString, correctStringChecks)
        if(bet == "TEST"):
            money = money + 100
        if(bet == "SAVE"):
            savefile = open('save.txt', 'w')
            #savefile.write("test")
            values = [money, die1, die2, onValue, Off, bets, payouts, payoutUpgradeCosts]
            for v in values:
                if type(v) != list: 
                    v = str(v) + "\n"
                    savefile.write(v)
                else:
                    inputstr = ""
                    for item in v:
                        inputstr = inputstr + str(item) + ","
                    inputstr = inputstr[:-1]
                    inputstr = inputstr + "\n" 
                    savefile.write(inputstr)
                #savefile.write("penis")
            savefile.close()
        if(bet == "LOAD"):
            savefile = open('save.txt', 'r')
            money = float(savefile.readline())
            die1 = int(savefile.readline())
            die2 = int(savefile.readline())
            onValue = int(savefile.readline())
            Off = bool(savefile.readline())
            betsStr = savefile.readline()
            payoutsStr = savefile.readline()
            payoutUpgradeCostsStr = savefile.readline()

            bets = [list(map(float, betsStr.split(",")))]
            bets = bets[0]
            payouts = [list(map(float, payoutsStr.split(",")))]
            payouts = payouts[0]
            payoutUpgradeCosts = [list(map(float, payoutUpgradeCostsStr.split(",")))]
            payoutUpgradeCosts = payoutUpgradeCosts[0]

    setup(money, die1, die2, onValue, Off, bets, payouts, payoutUpgradeCosts, winnings)




if __name__ == '__main__':
    clear()
    money = 100.00
            #[0PASS,1DONTPASS,2COME,3DONTCOME,FOUR,FIVE,SIX,ANYSEVEN,EIGHT,NINE,TEN,11FIELD,12HARD4,13HARD6,14HARD8,15HARD10,16TWO,17THREE,18ELEVEN,19TWELVE,20ANYCRAPS,21COME4,22COME5,23COME6,24COME8,25COME9,26COME10]
    betsArray = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    payouts = [2.0,2.0,2.0,2.0,9/5,7/5,7/6,5,7/6,7/5,9/5,1.0,7.0,9.0,9.0,7.0,30.0,15.0,15.0,30.0,7.0,2.0,2.0,2.0,2.0,2.0,2.0]
    payoutUpgradeCosts = [100.00,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.00,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.00,100.0,100.0,100.0,100.0,100.0,100.0,100.0,100.0]
    winnings = 0.0
    setup(money,1,1,7, True, betsArray, payouts, payoutUpgradeCosts, winnings)