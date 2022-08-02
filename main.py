from wordle_graphics import draw_board
from wordle_logic import evaluate

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


#draw_board([[['h','e','l','l','o'],[3,3,3,3,1]]])
