from words import validWords
#for storing of functions relating to assigning variables to letters in the boardState

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

def isWordValid(guess):
	lowerCaseGuess = guess.lower()
	if len(lowerCaseGuess) > 5 or lowerCaseGuess not in validWords:
		return False
	return True

def evaluate(board, guess, secretWord):
	board.append([list(guess),[0,0,0,0,0]])
	boardIndex = board.index([list(guess),[0,0,0,0,0]])

	correct_position = {}
	incorrect_position = {}

	word_dict = {}

	for i in secretWord:
		if i in word_dict.keys():
			word_dict[i] += 1
		else:
			word_dict[i] = 1

	for i, letter in enumerate(secretWord):
		if guess[i] in secretWord and letter == guess[i] and word_dict[guess[i]] > 0:
			board[boardIndex][LEGALITY][i] = CORRECT_POSITION

			word_dict[guess[i]] -= 1

	for i, letter in enumerate(secretWord):
		if board[boardIndex][LEGALITY][i] == CORRECT_POSITION:
			continue
		elif guess[i] in secretWord:
			print(guess[i], word_dict[guess[i]])
			if guess[i] in secretWord and word_dict[guess[i]] > 0:
				board[boardIndex][LEGALITY][i] = CORRECT_WRONG_POSITION
				word_dict[guess[i]] -= 1
				print(guess[i], word_dict[guess[i]])


	for i, letter in enumerate(secretWord):
		if board[boardIndex][LEGALITY][i] == CORRECT_POSITION or board[boardIndex][LEGALITY][i] == CORRECT_WRONG_POSITION:
			continue
		else:
			board[boardIndex][LEGALITY][i] = WRONG





# evaluate(BoardState, "trues", "trues")
# draw_board(BoardState)

# #evaluate([], "shoer", "shoer")
# evaluate([], "shoer", "trues")
# evaluate([[['s', 'h', 'o', 'e', 'r'], [2, 2, 2, 1, 2]]], "hayer", "trues")
# evaluate([[['s', 'h', 'o', 'e', 'r'], [2, 2, 2, 1, 2]], [['h', 'a', 'y', 'e', 'r'], [3, 3, 3, 1, 2]]], "trues", "trues")
