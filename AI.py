#for ai code

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

#WORD_LIST_LEN = (len(validWords))
LCDict = {}
'''
lettercount
compare high letter by prime hashing to words.
use ord to break ties
'''
PopularityIndex = {}
def AI_Letter_Count(words):
	for key in LCDict:
		LCDict[key] = 0

	# LCDict = {'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0, 'e' : 0, 'f' : 0, 'g' : 0, 'h' : 0, 'i' : 0, 'j' : 0,\
	# 			'k' : 0, 'l' : 0, 'm' : 0, 'n' : 0, 'o' : 0, 'p' : 0, 'q' : 0, 'r' : 0, 's' : 0, 't' : 0, \
	# 			'u' : 0, 'v' : 0, 'w' : 0, 'x' : 0, 'y' : 0, 'z' : 0}
	for word in words:
		print(word)
		myWord = word[:]
		sorted(myWord)
		aDict = {}
		for letter in myWord:
			if(letter not in aDict):
				aDict[letter] = 0
			aDict[letter] += 1
		for key in aDict:
			while (aDict[key] > 0):
				coolKey = ""
				for i in range(aDict[key]):
					coolKey += key
				if (coolKey not in LCDict):
					LCDict[coolKey] = 0
				LCDict[coolKey] += 1
				aDict[key] -= 1
	print(LCDict)
def PopularityUpdate(words):
	AI_Letter_Count(words)
	for key in PopularityIndex:
		PopularityIndex[key] = 0
	for word in words:
		aInt = 0
		aDict = {}
		for letter in word:
			if(letter not in aDict):
				aDict[letter] = 0
			aDict[letter] += 1
		for key in aDict:
			pop = 0
			while (aDict[key] > 0):
				coolKey = ""
				for i in range(aDict[key]):
					coolKey += key
				if(word not in PopularityIndex):
					PopularityIndex[word] = 0
				PopularityIndex[word] += LCDict[coolKey]
				aDict[key] -= 1
	print(PopularityIndex)
def get_guess(board):
	myDict = {}
	index = 0
	while(board[index][LEGALITY][0] != UNSELECTED):
		for char in board[index][LETTER]:
			if (char not in myDict):
				myDict[char] = 0
			myDict[char] += 1
