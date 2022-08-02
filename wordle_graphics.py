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
	for i in range(6):
		print("___ ___ ___ ___ ___")
		line = ""
		if(i < len(board)):
			for char in board[i][LETTER]:
				line += str("|" + char + "|" + " ")
		else:
			line = "| | | | | | | | | |"
		print(line)
		line = ""
		print("TTT TTT TTT TTT TTT")
		if(i < len(board)):
			for item in board[i][LEGALITY]:
				line+= str(symbolDict[item] + " ")
		else:
			print()
		print(line)
		line = ""
	print("~~~~~~~~~~~~~~~~~~~~~~~")

def color_board(board):
	pass
