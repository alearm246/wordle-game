from wordle_graphics import draw_board
from wordle_logic import evaluate
from words import validWords
from wordle_logic import isWordValid
from wordle_logic import evaluate
from AI import *
import random



#validWords = ["toile","zombi","dewed","hooky", "alkyl","ixnay","dovey","holey","cubar","amyls","podia","chino","fatwa","egger","hempy","crink","moots","atilt","jukes","ender"]

WORD_LIST_LEN = (len(validWords))
def play_wordle():
    #print("wordle time!!!!")

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


    #s_word = "Tzars".upper()

    # print("Welcome to Wordle!! \nIn order to play, input a valid five letter word for each round until you either " \
    # + "guess the word or run out of guesses!" \
    # "\n☺ means the letter was in the word and in the right position." \
    # "\n? means the letter was in the word but in the wrong position." \
    # "\nX means the letter was not in the word.")

    row = 1
    endgame = False
    guessed = False

    #draw_board(BoardState)

    words = validWords[:]

    s_word = (random.choice(words)).upper()



    #s_word = validWords[int(random.randint(0, WORD_LIST_LEN-1))].upper()


    while row <=6 and not endgame:
        #guess = input("Input a valid word: ")


        words, guess = get_guess(BoardState, words)
        if guess == "":
            guess = "OLDEN"

        while not isWordValid(guess):
            print(type(guess))
            print("^")
            if (guess == "LC"):
                AI_Letter_Count(validWords)
            elif(guess == "popIndex"):
                PopularityUpdate(validWords)
            elif(guess == "delete:"):
                target = input("which word to delete?")
                validWords.remove(target)
            print(s_word)
            guess = input("Input a valid word: ")
        guess = guess.upper()

        evaluate(BoardState, guess, s_word)

        #draw_board(BoardState)

        guessed = True

        for i in BoardState[row-1][LEGALITY]:
            if i != CORRECT_POSITION:
                guessed = False
                break
        if guessed:
            endgame = True

        row += 1

    if guessed:
        # print("Congratulations! You won in " + str(row-1) + " guesses!")
        return True, row-1
    if not guessed:
        # print(words)
        # print("word was: " + s_word)
        return False, row-1

play_wordle()

wins = 0
rounds = 0

guesses_total = 0

i=0
while i<1000:
    win, guesses = play_wordle()
    rounds +=1
    if win:
        wins +=1
        guesses_total+=guesses
    i+=1

print("rounds: ", rounds, " wins: ", wins)
print("The AI won:", str((wins/rounds)), "with an average guess rate of: ", str(guesses_total/wins))

#draw_board([[['h','e','l','l','o'],[3,3,3,3,1]]])

# evaluate(BoardState, "shoer", "trues")
# draw_board(BoardState)
# evaluate(BoardState, "hayer", "trues")
# draw_board(BoardState)
# evaluate(BoardState, "trues", "trues")
# draw_board(BoardState)
#
