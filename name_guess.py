"""This is a game in which the user has to make an accurate guess of a number in a range to
advance onto the next level. It has 10 levels"""
import random #imports the random module
import turtle as tr #imports the turtle module for turtle graphics

game_board = tr.Screen() #creates our game board
game_board.bgcolor("black")
llx = -200
lly = -100
urx = 200
ury = 100
game_board.setworldcoordinates(llx,lly,urx,ury)
menu = tr.Turtle() #creates our first turtle which will be used to provide feedback to the player
menu.color("white")
menu.up() #raises the turtle off the board
menu.ht() #hides the turtle and provides the player with a distraction free board
elements = tr.Turtle() #a turtle to display game elements on the board
elements.up() #raises the elements turtle off the board
elements.ht() #hides the elements turtle
elements.color("white")
state = tr.Turtle()
state.color("white")
state.ht()
state.up()
strike = tr.Turtle()
strike.color("white")
strike.ht()
def level_gen(i,levels):
    level=levels[i]
    return level
def guess_value(level_upper):
    guess=random.randrange(0,level_upper)
    return guess
def  menu_gen(level, guesses):
    menu.clear()
    menu.goto((llx+3),ury-3)
    menu.write("LEVEL: "+str(level))
    menu.goto((llx+3),(ury-7))
    menu.write("GUESSES: "+str(guesses))
    return level, guesses

"""def numbers(level):
    elements.up()
    for i in range(10):
        for j in range((level-1)*10,level*10):
            elements.goto(-50+(10*i),30-(6*(level-1)))
            elements.write(j)
       # for j in range(((level-1)*10),level_upper):

    #elements.goto(-15,20-(4*i))
"""
def numbers(level,y_index):
    elements.penup()
    for num in range((level-1)*10,level*10):
        if num< 10:
            location = num
        else:
            location = num%10
        elements.goto(-50 +location*10,y_index)
        elements.write(num)
def guessStrike(player):
    if player< 10:
        x = player
        y = 0
    else:
        x = player%10
        y = player//10
    strike.up()
    strike.goto(-51 +x*10,(30-y*10)+3)
    strike.down()
    strike.forward(5)

def game_progression():
    levels=[1,2,3,4,5,6,7,8,9,10]
    guesses = 4
    game_over = False
    for i in range(0,10):
        level = level_gen(i,levels)
        level_upper = level *10
        y_index = 30-((level-1)*10)
        numbers(level, y_index)
        guess = guess_value(level_upper)
        while guesses >= 0 and game_over ==False:
            menu_gen(level,guesses)
            player = int(game_board.numinput("What is the number generated? ","Enter your guess: ",0,0,99))
            if player==guess and level<10:
                guesses += 4
                state.clear()
                state.goto(-50,50)
                state.write("Congratulations, you proceed!!")
                strike.clear()
                game_over = False
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
                print("GAME OVER, YOU LOSE!!!")
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
                print("YOU WIN!")
                game = "win"
                game_over = True
    return game

def main():
    game = "neutral"
    if game == "lose":
        return
    else:
        while game != "win":
            game = game_progression()
if __name__ == "__main__":
    main()
