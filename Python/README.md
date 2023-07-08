## Python Scripting Project
    The orgin of my Flashcard generator/database tool for Tony Award Winners.
    To run the program, simply navigate to the Final folder and execute the setup.py in a terminal
    **with the command "python setup.py"**
    After booting up you will see this list of options,
    which can be selected by entering their respective number:
   ![Program at Launch](Photos/landing.png)

    Let's first talk about the Query Tools, of which there are three:
   ![Query Tools Menu](Photos/qtmenu.png)
    
    The Show Query will take the name of a show and return a list of the award(s) said show won. 
    For example, when I put in Billy Elliot, it returns:
   ![Example Show Query](Photos/examplequery.png)
    
    The Winner and Year Queries work very similarly, just with their respective data instead.
    
    Next, let's look into the dynamic flashcard tool, which I am personally quite happy with.
    This is what greets you initially when selecting the tool:
   ![Flashcard Landing](Photos/dflash1.png)
    
    From here, you can enter list to pull up all the categories you can add to your flashcards:
   ![Categories List](Photos/dflash2.png)
    
    Once you have selected all your desired categories, you will be asked whether or not
    you'd like to shuffle the flashcards:
   ![Shuffle Option](Photos/dflash3.png)
    
    Definitely mess around a bit with this tool, the array manipulation 
    took me awhile to get working properly.
    
    Lastly, there are currently two guessing games that I've setup to help with 
    memorization beyond just flashcards:
   ![Guessing Games Menu](Photos/ggmenu.png)
    
    They are not super complex games, but they do have score tracking and a highscore.
    For example, here's a prompt you would encounter in the Best Musical Guessing Game:
   ![Guessing Game Example](Photos/ggexampleprompt.png)
    
    Moving forward with this project I would like to add in a way to create custom datasets within the program itself. 
    That would allow the tool to be more useful to a broader audience instead of just musical theatre nerds. 
    That being said, I do feel like the flashcards and the guessing games could easily be adapted to fit many
    different datasets.
