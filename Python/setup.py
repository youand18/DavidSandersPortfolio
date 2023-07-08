#!/usr/bin/env python
import random
import config
random.seed()
import csv
#import actor
from os import system, name
import pandas as pd
import csv
import winner
import sys
import sqlite3
# import sleep to show output for some time period
from time import perf_counter
from time import sleep
#react
#zamarin
#swift data sqlite cards
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

year = []
categories = []
winner = []
show = []
syear = []
scategory = []
swinner = []
sshow = []
bmwinners = []
bpwinners = []
performancewinners = []

categoryOptions = [
"1. Best Play",
"2. Best Musical",
"3. Best Book of a Musical",
"4. Best Original Score",
"5. Best Revival of a Play",
"6. Best Revival of a Musical",
"7. Best Performance by an Actor in a Leading Role in a Play",
"8. Best Performance by an Actress in a Leading Role in a Play",
"9. Best Performance by an Actor in a Featured Role in a Play",
"10. Best Performance by an Actress in a Featured Role in a Play",
"11. Best Performance by an Actor in a Leading Role in a Musical",
"12. Best Performance by an Actress in a Leading Role in a Musical",
"13. Best Performance by an Actor in a Featured Role in a Musical",
"14. Best Performance by an Actress in a Featured Role in a Musical",
"15. Best Scenic Design of a Play",
"16. Best Scenic Design of a Musical",
"17. Best Costume Design of a Play",
"18. Best Costume Design of a Musical",
"19. Best Lighting Design of a Play",
"20. Best Lighting Design of a Musical",
"21. Best Sound Design of a Play",
"22. Best Sound Design of a Musical",
"23. Best Direction of a Play",
"24. Best Direction of a Musical",
"25. Best Choreography",
"26. Best Orchestrations",
"27. Best Author of a Play",
"28. Best Producer of a Play",
"29. Best Producer of a Musical",
"30. Conductor And Musical Director"
]

def setup():
#    clean()
#    create()
    with open("tonys.csv", newline='') as csvfile:
        rows = csv.reader(csvfile, delimiter=',')
        data = []
        for row in rows:
            data.append(row)
        
    for item in data:
        ts = item[0]
        year.append(item[1])
        categories.append(item[2]) 
        winner.append(item[3])
        show.append(item[4])

    with open("tonysSlash.csv", newline='') as csvfile:
        rows = csv.reader(csvfile, delimiter=',')
        data = []
        for row in rows:
            data.append(row)
        
    for item in data:
        ts = item[0]
        syear.append(item[1])
        scategory.append(item[2]) 
        swinner.append(item[3])
        sshow.append(item[4])
    bestMusicalSetup()

def cleanup():
    i = 0
    for people in winner:
        if ("/" in people): 
            #print(people.split('/', 1)[0])
            winner[i] = people.split('/', 1)[0]



def queryWins(string):
    wins = 0
    i = 0
    for people in winner:
        if (string in people):
            wins += 1
            info = (df.iloc[i-1])
            print("Year: " + str(info[0]))
            print("Award: " + info[1])
            print("Winner: " + info[2])
            print("Show: " + info[3])
            print()
        i+=1
    return wins

def queryShows(string):
    i = 0
    shows = 0
    for s in sshow:
        if (string in s):
            shows+=1
            #print(ds.iloc[i-1])
            info = (ds.iloc[i-1])
            print("Year: " + str(info[0]))
            print("Award: " + info[1])
            print("Winner: " + info[2])
            print("Show: " + info[3])
            print()
        i+=1
    return shows

def queryYears(string):
    i = 0
    awardsThatYear = 0
    for y in syear:
        if (y == string):
            awardsThatYear+=1
            info = (ds.iloc[i-1])
            print("Year: " + str(info[0]))
            print("Award: " + info[1])
            print("Winner: " + info[2])
            print("Show: " + info[3])
            print()
        i+=1
    return awardsThatYear
    
def analysis():
    print(df['Who'].value_counts().head(10))
    print('\n')
    print(ds['Show'].value_counts().head(10))

#def smartShowAnalysis():
#    for 




def guessCleaner(strs):
    strs = strs.lower()
    newstr = ""
    for i in strs:
        if ((ord(i) > 64 and ord(i) < 91) or (ord(i) > 96 and ord(i) < 123) or (ord(i) > 46 and ord(i) < 58)):
            newstr+=i
    return newstr

def guessSimplifier(guess, answer):
    if (guess == answer):
        return True
    i = 0
    if ((answer[0] + answer[1] + answer[2]).lower() == "the"):
        cleanAnswer = answer[3:]
        if (guess == cleanAnswer):
            return True
        answer = cleanAnswer
    requiredSame = 8
    while ((i < len(answer)-1) and (i < requiredSame)):
            if(len(guess) < requiredSame or guess[i] != answer[i]):
                return False
            i+=1
    return True


def bestMusicalSetup():
    i = 0
    for award in categories:
        if (award == "Best Musical"):
            bmwinners.append([year[i],winner[i],show[i]])
        elif (award == "Best Play"):
            bpwinners.append([year[i],winner[i],show[i]])
        elif (award == "Best Performance by an Actor in a Leading Role in a Musical" or award == "Best Performance by an Actor in a Leading Role in a Play" 
        or award == "Best Performance by an Actor in a Featured Role in a Musical" or award == "Best Performance by an Actor in a Featured Role in a Play" 
        or award == "Best Performance by an Actress in a Leading Role in a Musical" or award == "Best Performance by an Actress in a Leading Role in a Play" 
        or award == "Best Performance by an Actress in a Featured Role in a Musical" or award == "Best Performance by an Actress in a Featured Role in a Play"):
            performancewinners.append([year[i],categories[i],winner[i],show[i]])
        i+=1
    #print(bmwinners)

def copyArray(array1):
    array2 = []
    for element in array1:
        array2.append(element)
    return array2


def bestMusicalGuess(streak, notUsed):
    clear()
    file1 = open("highscore.txt","r")
    highscore = file1.read()
    file1.close()
    if (len(notUsed) == 0):
            print("Holy crap you got all " + str(streak) + " of 'em...Well Congratulations I suppose.")
            sleep(6)
            file2 = open("highscore.txt","w")
            file2.write(str(streak))
            file2.close() 
            menu()
    if (len(notUsed) == 1):
        i = 0
    else:
        i = random.randrange(0,len(notUsed))
    if (notUsed[i][0] == "1960"):
        if (notUsed[i][1] == "The Sound of Music"):
            guess = input("In " + notUsed[i][0] + " what musical won Best Musical?(not Fiorello!): ")
        else:
            guess = input("In " + notUsed[i][0] + " what musical won Best Musical?(not The Sound of Music): ")
    else:
        guess = input("In " + notUsed[i][0] + " what musical won Best Musical?")
        if (guess == ""):
            clear()
            print("Please be careful with the enter key, this is your only warning!")
            guess = input("In " + notUsed[i][0] + " what musical won Best Musical?")
    guess = guessCleaner(guess)
    if (guessSimplifier(guess,guessCleaner(notUsed[i][1]))):
        streak+=1
        print(notUsed[i][1] + " is Correct! \nTotal Streak: " + str(streak))
        sleep(3)
        notUsed.pop(i)
        bestMusicalGuess(streak, notUsed)
    elif (guess == "e" or guess == "E"):
        menu()
    elif (guess == "h" or guess == "H"):
        print(str(highscore))
        sleep(3)
        menu()
    else:
        print("Incorrect, the correct answer is " + notUsed[i][1] + "\n You just lost a streak of " + str(streak))
        if (streak > int(highscore)):
            sleep(2)
            x = 0
            while(x < 5):
                print("->  New highscore of " + str(streak) + "!  <-\nThe old highscore was " + str(highscore))
                sleep(.5)
                clear()
                print("--> New highscore of " + str(streak) + "! <--\nThe old highscore was " + str(highscore))
                sleep(.5)
                clear()
                print("--->New highscore of " + str(streak) + "!<---\nThe old highscore was " + str(highscore))
                sleep(.5)
                clear()
                x+=1
            file2 = open("highscore.txt","w")
            file2.write(str(streak))
            file2.close()
            menu()
        sleep(5)
        notUsed = copyArray(bmwinners)
        bestMusicalGuess(0, notUsed)

def performanceGuess(streak):
    clear()
    #file1 = open("highscore.txt","r")
    #highscore = file1.read()
    #file1.close()
    i = random.randrange(1,len(performancewinners)) - 1
    if ("Actor in a Leading Role" in performancewinners[i][1]):
        print("Who won for his leading performance in \"" + performancewinners[i][3] + "\" in " + performancewinners[i][0] + "?")
        guess = input()
    elif ("Actor in a Featured Role" in performancewinners[i][1]):
        print("Who won for his featured performance in \"" + performancewinners[i][3] + "\" in " + performancewinners[i][0] + "?")
        guess = input()
    elif ("Actress in a Leading Role" in performancewinners[i][1]):
        print("Who won for her leading performance in \"" + performancewinners[i][3] + "\" in " + performancewinners[i][0] + "?")
        guess = input()
    elif ("Actress in a Featured Role" in performancewinners[i][1]):
        print("Who won for her featured performance in \"" + performancewinners[i][3] + "\" in " + performancewinners[i][0] + "?")
        guess = input()
    guess = guessCleaner(guess)
    if (guessSimplifier(guess,guessCleaner(performancewinners[i][2]))):
        streak+=1
        print(performancewinners[i][2] + " is Correct! \nTotal Streak: " + str(streak))
        sleep(3)
        performanceGuess(streak)
    elif (guess == "e" or guess == "E"):
        menu()
    else:
        print("Incorrect, the correct answer is " + performancewinners[i][2] + "\n You just lost a streak of " + str(streak))
        #if (streak > int(highscore)):
            #print("New highscore of " + str(streak) + ". \nThe old highscore was " + str(highscore))
            #file2 = open("highscore.txt","w")
            #file2.write(str(streak))
            #file2.close()
        sleep(5)
        performanceGuess(0)
def shuffled(used):
    clear()
    for award in bmwinners:
        i = random.randrange(1, len(bmwinners)) - 1
        loops = 0
        while i in used:
            if (loops > len(bmwinners)):
                menu()
            i = random.randrange(1, len(bmwinners)) - 1
            loops+=1
        print("\n"+bmwinners[i][0] + " - Best Musical Winner:")
        e = input("(Enter to Reveal)")
        if (e == "e" or e == "E"):
            menu()
        elif (e == "r" or e == "R"):
            used = []
            shuffled(used)
        clear()
        print (bmwinners[i][0] + " - Best Musical Winner: " + bmwinners[i][1])
        used.append(i)
    menu()

def shuffledAuto(used):
    clear()
    for award in bmwinners:
        i = random.randrange(1, len(bmwinners)) - 1
        loops = 0
        while i in used:
            if (loops > len(bmwinners)):
                menu()
            i = random.randrange(1, len(bmwinners)) - 1
            loops+=1
        print("\n"+bmwinners[i][0] + " - Best Musical Winner:")
        sleep(5)
        e = ""
        if (e == "e" or e == "E"):
            menu()
        elif (e == "r" or e == "R"):
            used = []
            shuffledAuto(used)
        clear()
        print (bmwinners[i][0] + " - Best Musical Winner: " + bmwinners[i][1])
        used.append(i)
    menu()

def flashcards():
    clear()
    i = 0
    for award in bmwinners:
        if (i > len(bmwinners)-1):
            break
        print("\n"+bmwinners[i][0] + " - Best Musical Winner:")
        e = input("(Enter to Reveal)")
        if (e == "e" or e == "E"):
            menu()
        elif (e == "r" or e == "R"):
            flashcards()
        elif(e == "y" or e == "Y"):
            year = int(input("Enter Year: "))
            if (year > 1948 and year < 2021):
                i = year - 1949
        elif(e == "b" or e == "B"):
            i = i-2
            clear()
            continue
        clear()
        print (bmwinners[i][0] + " - Best Musical Winner: " + bmwinners[i][1])
        if (i == len(bmwinners)-1):
            input("(Enter to Continue)")
        i+=1
    menu()

def categoryMatch(category):
    for c in categoryOptions:
        if (c.lower() == category.lower()):
            return c
    return category

def createList(r1, r2):
    return list(range(r1, r2+1))

def isInt(element) -> bool:
    try:
        int(element)
        return True
    except ValueError:
        return False

def eChecks(e, yearList, winnerList, showList, categoryList):
    if (e == "e"):
        menu()
    if (e == "l"):
        i = 0
        for x in yearList:
            print(x)
            print(winnerList[i])
            print(showList[i])
            print(categoryList[i]) 
            print()
            i+=1  
        input("Enter to Continue")


def dynamicFlashcards():
    clear()
    yearList = []
    winnerList = []
    showList = []
    categoryList = []
    notUsedIndex = []
    lowerCategoryList = [category.lower() for category in categoryOptions]
    i = 0
    for category in lowerCategoryList:
        category = category.split('.')
        lowerCategoryList[i] = category[1].lstrip()
        i+=1
    #for l in lowerCategoryList:
    #    print(l)
    addingCategories = True
    while(addingCategories):
        clear()
        print("(enter \"list\" to see all the category options)")
        print("(enter \"done\" when you are done selecting categories)")
        category = input("Enter Category: ")
        eChecks(category, yearList, winnerList, showList, categoryList)
        category = category.lower()
        if (guessCleaner(category) == "list"):
            for category in categoryOptions:
                print(category)
            print()
            category = input("Enter Category or Category Number: ")
            eChecks(category, yearList, winnerList, showList, categoryList)
            category = category.lower()
        if (category in lowerCategoryList):
            i = 0
            for c in categories:
                if(i >= len(year)):
                    break
                if (c.lower() == category.lower()):
                    yearList.append(year[i])
                    winnerList.append(winner[i])
                    showList.append(show[i])
                    categoryList.append(categoryMatch(category))
                i+=1
            i = 0
        elif (isInt(category) and (int(category) > 0 and int(category) < 31)):
            for cOption in categoryOptions:
                cOption = cOption.split('.')
                #print(cOption)
                if (cOption[0] == category):
                    category = cOption[1].lstrip()
            i = 0
            for c in categories:
                if(i >= len(year)):
                    break
                if (c.lower() == category.lower()):
                    yearList.append(year[i])
                    winnerList.append(winner[i])
                    showList.append(show[i])
                    categoryList.append(categoryMatch(category))
                i+=1
            i = 0     
        elif("-" in category):
            category = category.split('-')
            skip = False
            for c in category:
                if (not isInt(c) or len(category) > 2 or int(c) < 1 or int(c) > 30):
                    skip = True
            if(not skip):
                start = int(category[0])
                end = int(category[1])
                numbersToAdd = createList(start, end)
                for number in numbersToAdd:
                    for cOption in categoryOptions:
                        cOption = cOption.split('.')
                        if (int(cOption[0]) == number):
                            category = cOption[1].lstrip()                
                    i = 0
                    for c in categories:
                        if(i >= len(year)):
                            break
                        if (c.lower() == category.lower()):
                            yearList.append(year[i])
                            winnerList.append(winner[i])
                            showList.append(show[i])
                            categoryList.append(categoryMatch(category))
                        i+=1

        elif(guessCleaner(category) == "done"):
            addingCategories = False
        else:
            continue
    shuffleCheck = input("Would you like to shuffle the flashcards? (Y/N): ")
    notUsedIndex = createList(0, len(winnerList)-1)
    if (shuffleCheck.lower() == "y" or shuffleCheck.lower() == "yes"):
        random.shuffle(notUsedIndex)
    for e in yearList:
        i = notUsedIndex[0]
        
        if (categoryList[i] == "Best Musical" or categoryList[i] == "Best Play" or categoryList[i] == "Best Revival of a Play" or categoryList[i] == "Best Revival of a Musical"):
            clear()
            print("\n"+ yearList[i] + " - " + categoryList[i] + ":")
            e = input("(Enter to Reveal)") 
            eChecks(e, yearList, winnerList, showList, categoryList)              
            clear()
            print("\n"+ yearList[i] + " - " + categoryList[i] + ":")  
            print(showList[i])
            e = input("(Enter to Continue)")
            eChecks(e, yearList, winnerList, showList, categoryList)
        else:
            clear()
            print("\n"+ yearList[i] + " - " + categoryList[i] + " for " + showList[i] + ":")
            e = input("(Enter to Reveal)")
            eChecks(e, yearList, winnerList, showList, categoryList)
            clear()
            print("\n"+ yearList[i] + " - " + categoryList[i] + " for " + showList[i] + ":")
            print(winnerList[i])
            e = input("(Enter to Continue)")
            eChecks(e, yearList, winnerList, showList, categoryList)
        notUsedIndex.pop(0)

    menu()    
    #input("{Enter to Continue}")

def pandasTest():
    print(df.axes)

def spinny(delay):
    clear()
    print("""                    
        ╔═══╗        
        ║   ║     
        ╚═──╝     
        """)
    sleep(delay)
    clear()
    print("""                    
        ╔═══╗        
        ║   ║     
        └──═╝     
        """)
    sleep(delay)
    clear()
    print("""                    
        ╔═══╗        
        │   ║     
        └═══╝     
        """)
    sleep(delay)
    clear()
    print("""                    
        ┌═══╗        
        │   ║     
        ╚═══╝     
        """)
    sleep(delay)
    clear()
    print("""                    
        ┌─══╗        
        ║   ║     
        ╚═══╝     
        """)
    sleep(delay)
    clear()
    print("""                    
        ╔──═╗        
        ║   ║     
        ╚═══╝     
        """)
    sleep(delay)
    clear()
    print("""                    
        ╔═──╗        
        ║   ║     
        ╚═══╝     
        """)
    sleep(delay)
    clear()
    print("""                    
        ╔══─┐        
        ║   ║     
        ╚═══╝     
        """)
    sleep(delay)
    clear()
    print("""                    
        ╔═══┐        
        ║   │     
        ╚═══╝     
        """)
    sleep(delay)
    clear() 
    print("""                    
        ╔═══╗        
        ║   │     
        ╚═══┘     
        """)
    sleep(delay)
    clear()  
    print("""                    
        ╔═══╗        
        ║   ║     
        ╚══─┘     
        """)
    sleep(delay)
    clear()              

def printGuessingGames():
    print("""
    1. Best Musical Guessing Game
    2. Performance Winner Guessing Game
    """)   
def printQueryTools():
    print("""
    1. Query Show Database
    2. Query Winner Database
    3. Query Year Database    
    """)

def printMenu():
    print("""1. Dynamic Flashcards
2. Guessing Games
3. Query Tools
""")

def menu():
    clear()
    cleanup()
    notUsed = []
    used = []
    #print(winner)
    printMenu()
    selection = input("Enter Number of Desired Tool: ")
    if (selection == "1"):
        dynamicFlashcards()
    elif (selection == "2"):
        clear()
        printGuessingGames()
        newSelection = input("Enter Number of Desired Tool: ")
        if (newSelection == "1"):
            notUsed = copyArray(bmwinners)
            bestMusicalGuess(0, notUsed)
        elif (newSelection =="2"):
            performanceGuess(0)
        else:
            menu()
    elif (selection == "a"):
        analysis()
        input("{Enter to Continue}")
        menu()       
    elif (selection == "3"):
        clear()
        printQueryTools()
        newSelection = input("Enter Number of Desired Tool: ")
        if (newSelection == "1"):
            string = input("Enter Name of Show: ")
            shows = queryShows(string)
            if (shows > 0):
                print (str(shows) + " Mentions of " + string)
            input("{Enter to Continue}")
            menu()
        elif (newSelection == "2"):
            string = input("Enter Name of Tony Award Winner: ")
            print("\n")
            wins = queryWins(string)
            if (wins > 0):
                print (str(wins) + " Award Wins")
                input("(Enter to Continue)")
            menu()
        elif(newSelection == "3"):
            string = input("Enter Year: ")
            awards = queryYears(string)
            print(str(awards) + " Awards in " + string + ".")
            input("{Enter to Continue}")
            menu()
        else:
            menu()
    #testing options/old things
    elif (selection == "8"):
        shuffled(used)
    elif (selection == "9"):
        shuffledAuto(used)
    elif(selection == "10"):
        for c in categories:
            print(c)        


    elif (selection == "!"):
        x = 0
        while(x<11):
            spinny(.15)
            x = x + 1
        menu()
    else:
        menu()

    

if __name__ == '__main__':
    df = pd.read_csv('tonys.csv', index_col=0)
    ds = pd.read_csv('tonysSlash.csv', index_col=0)
    setup()
    x = 0
    #little spinny animation to make the program seem more impressive that it is
    #while(x<3):
    #    spinny(.15)
    #    x = x + 1
    menu()