from wordle_graphics import draw_board
from wordle_logic import evaluate
from words import validWords
from wordle_logic import isWordValid
from wordle_logic import evaluate
from AI import *
import random

print("wordle time!!!!")

BoardState = []


#constants for use when decideing whether to look at letter or legality
LETTER = (0)
LEGALITY = (1)

'''
note that each boardState will be represented with a two item list with index
0 and 1, 0 for the letter and 1 for whether or not it's supposed to be there, according
to the below constants.
'''
#constants for use when deciding letter legality
UNSELECTED = (0)
CORRECT_POSITION = (1)
CORRECT_WRONG_POSITION = (2)
WRONG = (3)

WORD_LIST_LEN = (len(validWords))

validWords = ["toile","zombi","dewed","hooky", "alkyl","ixnay","dovey","holey","cubar","amyls","podia","chino","fatwa","egger","hempy","crink","moots","atilt","jukes","ender"]
def play_wordle():

    #s_word = validWords[int(random.randint(0, WORD_LIST_LEN-1))]
    s_word = "egger".upper()

    print("Welcome to Wordle!! \nIn order to play, input a valid five letter word for each round until you either " \
    + "guess the word or run out of guesses!" \
    "\n☺ means the letter was in the word and in the right position." \
    "\n? means the letter was in the word but in the wrong position." \
    "\nX means the letter was not in the word.")

    row = 1
    endgame = False
    guessed = False

    draw_board(BoardState)

    while row <=6 and not endgame:
        guess = input("Input a valid word: ")
        while not isWordValid(guess):
            if (guess == "LC"):
                AI_Letter_Count(validWords)
            elif(guess == "popIndex"):
                PopularityUpdate(validWords)
            elif(guess == "delete:"):
                target = input("which word to delete?")
                validWords.remove(target)
            guess = input("Input a valid word: ")
        guess = guess.upper()

        evaluate(BoardState, guess, s_word)

        draw_board(BoardState)

        guessed = True

        for i in BoardState[row-1][LEGALITY]:
            if i != CORRECT_POSITION:
                guessed = False
                break
        if guessed:
            endgame = True

        row += 1

    if guessed:
        print("Congratulations! You won in " + str(row-1) + " guesses!")
    if not guessed:
        print("word was: " + s_word)

play_wordle()

#draw_board([[['h','e','l','l','o'],[3,3,3,3,1]]])

# evaluate(BoardState, "shoer", "trues")
# draw_board(BoardState)
# evaluate(BoardState, "hayer", "trues")
# draw_board(BoardState)
# evaluate(BoardState, "trues", "trues")
# draw_board(BoardState)
#
