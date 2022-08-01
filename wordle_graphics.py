# for printing the boardState

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

def draw_board(board):
	symbolDict = {WRONG : " X ", \
	CORRECT_WRONG_POSITION : " ? ",\
	CORRECT_POSITION : " ☺ ", \
	UNSELECTED : " "}
	for i in board:
		print("___ ___ ___ ___ ___")
		line = ""
		for char in board[LETTER]:
			line += str("|" + char + "|" + " ")
		print(line)
		line = ""
		print("TTT TTT TTT TTT TTT")
		for item in board[LEGALITY]:
			line+= str(symbolDict[item] + " ")
		print(line)
		line = ""


def color_board(board):
	pass
