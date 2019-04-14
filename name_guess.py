"""This is a game in which the user has to make an accurate guess of a number in a range to
advance onto the next level. It has 10 levels"""
import random #imports the random module
import turtle as tr #imports the turtle module for turtle graphics

game_board = tr.Screen() #creates our game board
game_board.bgcolor("black") #sets the game background color to black
llx = -200
lly = -100
urx = 200
ury = 100
game_board.setworldcoordinates(llx,lly,urx,ury) #creates boundaries for the game window

menu = tr.Turtle() #creates our first turtle which will be used to provide feedback to the player
menu.color("white")
menu.up() #raises the turtle off the board
menu.ht() #hides the turtle and provides the player with a distraction free board

elements = tr.Turtle() #a turtle to display game elements on the board
elements.color("white")
elements.up() #raises the elements turtle off the board
elements.ht() #hides the elements turtle
 
state = tr.Turtle() #a turtle to write the game states
state.color("white")
state.ht() #hides the turtle
state.up() #raises the turtle

strike = tr.Turtle() #a turtle to strike through wrongly selected numbers
strike.color("white")
strike.ht() #hides the turtle
def level_gen(i,levels): #the function that generates the game levels
    level=levels[i] #selects the level from the list of levels
    return level #returns the level
def guess_value(level_upper): #the function that generates the random number
    guess=random.randrange(0,level_upper) 
    return guess #returns the guessed value
def  menu_gen(level, guesses): #the function that generates the game menu
    menu.clear() #clears the menu
    menu.goto((llx+3),ury-3) 
    menu.write("LEVEL: "+str(level)) #writes the level
    menu.goto((llx+3),(ury-7))
    menu.write("GUESSES: "+str(guesses)) #writes the number of guesses left in the game
    return level, guesses
def numbers(level,y_index): #the function that writes out the numbers onto the game board
    elements.penup()
    for num in range((level-1)*10,level*10):
        if num< 10: 
            location = num #runs if the number is less than 10
        else:
            location = num%10 #runs if the number is bigger than or equal to 10
        elements.goto(-50 +location*10,y_index) #moves the elements turtle to the write location
        elements.write(num) #writes the number onto the game board
def guessStrike(player): #the function that crosses out a number when the user types it in
    if player< 10: #runs if the number is less than 10
        x = player
        y = 0
    else: #runs if the number is bigger than or equal to 10
        x = player%10
        y = player//10
    strike.up()
    strike.goto(-51 +x*10,(30-y*10)+3) #goes to the location of the number the player inputs
    strike.down()
    strike.forward(5) #strikes through the number
def game_progression(): #the function that runs the entire game
    levels=[1,2,3,4,5,6,7,8,9,10] #the levels are stored in a list
    guesses = 4 #the number of guesses is predefined
    game_over = False #a boolean value to determine the end of the game is assigned
    for i in range(10): #to run the game for the 10 levels of the video game
        level = level_gen(i,levels) #calls the function that generates the level
        level_upper = level *10
        y_index = 30-((level-1)*10)
        numbers(level, y_index) #calls the function to write down the numbers for each level on the game board
        guess = guess_value(level_upper) #assigns the randomly generated number
        print(guess)
        while guesses >= 0 and game_over ==False: #a while loop that runs as long as the number of guesses is greater than 0 and the value of the boolean variable is False
            menu_gen(level,guesses) #calls the menu function that writes the menu on the game board
            maxi = level_upper - 1
            player = int(game_board.numinput("What is the number generated? ","Enter your guess: ",0,0,maxi)) #prompts the player to enter a guess
            if player==guess and level<10: #
                guesses += 4
                state.clear()
                state.goto(-50,50)
                state.write("Congratulations, you proceed!!")
                strike.clear()
                break
            elif guesses > 0 and level < 10 and player < guess:
                guesses -= 1
                guessStrike(player)
                state.clear()
                state.goto(-50,50)
                state.write("Sorry, try a bigger number")
            elif guesses>0 and level<10 and player>guess:
                guesses -= 1
                guessStrike(player)
                state.clear()
                state.goto(-50,50)
                state.write("Sorry, try a smaller number")
            elif guesses == 0:
                state.clear()
                state.goto(-50,50)
                state.write("GAME OVER, YOU LOSE!!!")
                game_over = True
                game = "lose"
            elif level==10 and player!=guess and player<guess:
                guesses-=1
                guessStrike(player)
                state.clear()
                state.goto(-50,50)
                state.write("Sorry, try a bigger number")
            elif level==10 and player!=guess and player>guess:
                guesses-=1
                guessStrike(player)
                state.clear()
                state.goto(-50,50)
                state.write("Sorry, try a smaller number")
            elif player==guess and level==10:
                state.clear()
                state.goto(-50,50)
                state.write("YOU WIN!")
                game = "win"
                game_over = True
    return game

def main(): #the main function
    game = "" #blank string to store the value of the game state
    while game!="win":
        game=game_progression()
    start = game_board.textinput("would you like to play again?","(Type in Y for yes and N for no) :")
    start = start.upper()
    if start == "Y":
        game=game_progression()
    else:
        game_board.exitonclick()
if __name__ == "__main__":
    main()
