#Brandon Deo
#Mitchell Dennison
#MWF 2:30-3:20
#November 17, 2013

from random import *
import turtle

#this is a redefinition of turtle.goto
def goto(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

#input: blank list
#output: list of words
#reads in all the words in the file, ‘wordlist.txt’ and places all
#the words into a list, which is returned.

def readfile(listofwords):
    lines = open("wordlist.txt","r")
    for line in lines:
        listofwords.append(line.strip())
    lines.close()
    return(listofwords)

#input: list of words
#output: string (word)
#Test Case:
#   getword(['dog','cat','happy','mother']) -> 'happy'

def getword(listofwords):
    randword = randrange(len(listofwords))
    word = listofwords[randword]
    return(word)

#input: string(word), list of letters
#output: Boolean
#This function checks to see if each letter in the word
#is in the same place as it is in the list of letters
#Test Cases:
#   checkwin("dog",['d','o','g']) --> True
#   checkwin("yes",['-','e','s']) --> False

def checkwin(word,blank):
    storage = 0
    for x in range(len(blank)):
        if blank[x] == word[x]:
            storage += 1
    total = len(word)
    if storage == total:
        return(True)
    else:
        return(False)

#input: string/list
#output: nothing
#This function prints in the turtle window, "You won!" and
#then "You guessed the word in 'x' guesses!"

def wonGame(word,letters):
    guesses = len(letters)
    goto(-200,0)
    turtle.color("black")
    turtle.write("You won! \nYou guessed "+word+" in "+str(guesses)+" guesses.", font=("Georgia",28))
    return

#input: string(word)
#output: nothing
#This function prints to the turtle window, "You Lose", "The word was (word)"

def lostGame(word):
    goto(-150,0)
    turtle.write("You lose! \n The word was "+str(word)+".", font=("Georgia",28))
    return


#input: string(word)
#output: list with as many '-'s as there are chars in the word
#This function makes a list that is x elements long where each element is '-' and x is the
#number of chars in the word.
#Test Case:
#   makeBlank("today") --> ['-','-','-','-','-']
#   makeBlank("cat")   --> ['-','-','-']

def makeblank(word):
    blanksls = []
    for x in range(len(word)):
        blanksls.append('-')
    return(blanksls)



#input: none
#ouput: nothing
#This function clears the turtle window, sets the pen color, sets
#the background image and draws the hangman structure

def drawstruct():
    turtle.clear()
    turtle.setup(1024,640)
    turtle.bgpic("desert.gif")
    goto(200,-200)
    turtle.width(5)
    turtle.color("#663300")
    turtle.setheading(0)
    turtle.forward(250)
    turtle.rt(180)
    turtle.forward(125)
    turtle.rt(90)
    turtle.forward(350)
    turtle.lt(90)
    turtle.forward(75)
    turtle.lt(90)
    turtle.forward(20)
    return


#input: a list of blanks and two ints: the length of the blank to be
#       drawn, and the length of the space drawn in between each blank.
#output: nothing
#This function draws in the turtle window a blank for each blank in the list, with a space between
#each blank

def drawblanks(blank,size,space):
    goto(-425,-250)
    for x in range(len(blank)):
        turtle.setheading(0)
        turtle.forward(size)
        turtle.penup()
        turtle.forward(space)
        turtle.pendown()
    return

#input: list of letters guessed
#output: nothing
#This function writes the guessed letters at the top left of the turtle screen
#using a loop and turtle.write.

def writeguessed(letters):
    x = -450
    for y in letters:
        x += 25
        goto(x,250)
        turtle.write(y, font=("Georgia",24))
    return

#Sets the Body Pen Attributes
def man():
    turtle.width(4)
    turtle.color("black")
    turtle.setheading(0)

#Draws Head
def drawhead():
    goto(250,129)
    man()
    turtle.forward(5)
    for x in range(18):
        turtle.rt(20)
        turtle.forward(10)
    turtle.setheading(0)
    goto(0,0)
    return

#Draws Body
def drawtorso():
    goto(250,70)
    man()
    turtle.setheading(270)
    turtle.forward(120)
    turtle.setheading(0)
    return

#Draws Right Arm
def drawrightarm():
    man()
    goto(250,55)
    turtle.setheading(0)
    turtle.rt(60)
    turtle.forward(60)
    return

#Draws Left Arm
def drawleftarm():
    man()
    goto(250,55)
    turtle.setheading(180)
    turtle.lt(60)
    turtle.forward(60)
    return

#Draws Right Leg
def drawrightleg():
    goto(250,-50)
    turtle.setheading(0)
    turtle.rt(75)
    turtle.forward(60)
    return

#Draws Left Leg
def drawleftleg():
    man()
    goto(250,-50)
    turtle.setheading(180)
    turtle.lt(75)
    turtle.forward(60)
    return

#Draws Left Foot
def drawleftfoot():
    man()
    goto(234.47,-107.96)
    turtle.setheading(180)
    turtle.forward(15)
    goto(0,0)
    return

#Draws Right Foot
def drawrightfoot():
    man()
    goto(265.53,-107.96)
    turtle.setheading(0)
    turtle.forward(15)
    return

#Draws Left Hand
def drawlefthand():
    man()
    goto(220,3.04)
    turtle.setheading(180)
    turtle.circle(5)
    return

#Draws Right Hand
def drawrighthand():
    man()
    goto(280,3.04)
    turtle.setheading(180)
    turtle.circle(5)
    return

#input: int (# wrong)
#output: int (# wrong)
#This function draws the appropriate body parts of the hangman according
#to the number of guesses the user has guessed wrong.

def drawbody(wrong):
    if wrong == 1:
        drawhead()
        return(wrong)
    elif wrong == 2:
        drawtorso()
        return(wrong)
    elif wrong == 3:
        drawleftarm()
        return(wrong)
    elif wrong == 4:
        drawrightarm()
        return(wrong)
    elif wrong == 5:
        drawleftleg()
        return(wrong)
    elif wrong == 6:
        drawrightleg()
        return(wrong)
    elif wrong == 7:
        drawleftfoot()
        return(wrong)
    elif wrong == 8:
        drawrightfoot()
        return(wrong)
    elif wrong == 9:
        drawlefthand()
        return(wrong)
    elif wrong == 10:
        drawrighthand()
        return(wrong)
    else:
        return(wrong)

#input: a string(word), a list(letters guessed), int (#wrong)
#output: nothing
#This function draws the structure, makes the list of blanks, draws the blanks, and then loops
#until the word is guessed or the hangman is hanged. Within the loop it calls writeguessed, uses
#turtle.textinput to ask the user to guess a letter. If the letter is in the word, placeletter is
#called, the letter is appended to the letters already guessed, and if the checkwin function
#indicates the word has been successfully guessed, the wonGame func is called. Otherwise, if the
#letter is not in the word, the drawbody function is called, the letter appended to the guessed
#list and if wrong guesses is up to 10, lostgame is called.

def playround(word,letters,wrong):
    invalid = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=','{','}','[',']','"',"'",";",":",',','.','?','>','<',' ']
    drawstruct()
    blankslist = makeblank(word)
    drawblanks(blankslist,30,10)
    while((checkwin(word,blankslist)==False) and (wrong!=10)):
        writeguessed(letters)
        goto(-512,320)
        letter = turtle.textinput("Hangman","Guess a letter")
        if letter.lower() in letters or letter in invalid:
            letter = turtle.textinput("Error","Please enter a letter you haven't used \nthat isn't a special character. Try Again.")
        if letter.lower() in word.lower():
            placeletter(letter,word,blankslist,30,10)
            letters.append(letter)
            if checkwin(word,blankslist):
                return(wonGame(word,letters))
        else:
            wrong+=1
            drawbody(wrong)
            letters.append(letter)
            if wrong == 10:
                return(lostGame(word))

#input: guessed letter, word, blank (list of blanks), size (int length of blank line), space
#output: blank
#This function modifies the blank by substituting the letter for the '-'. It also writes in turtle
#over the appropriate blank line the letter guessed at the appropriate places.
#Test Case:
#   placeletter('p','puppy',['-','-','-','-','-'],30,10) --> ['p','-','p','p','-']

def placeletter(letter,word,blank,size,space):
    man()
    count = 0
    for x in word:
        if x.lower() == letter.lower():
            blank[count] = x
            turtle.penup()
            a = -415 + count*size + space*count-1
            turtle.goto(a,-240)
            turtle.write(x, font=("Georgia",36))
        count+=1
    return(blank)

#input: list of words
#output: nothing
#This function asks the user if they want to play again, and continues until no is entered.

def game(listofwords):
    choice = "yes"
    while (choice.lower() == "yes"):
        letters = []
        word = getword(listofwords)
        print(word)
        playround(word,letters,0)
        choice = turtle.textinput("Hangman",'Play Again? ("yes" or "no")')
    if choice == "no":
        turtle.bye()
    return

#Starts game by calling the readfile function

def main():
    turtle.hideturtle()
    turtle.speed(10)
    ls = readfile([])
    game(ls)

main()
