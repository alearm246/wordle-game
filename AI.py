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
		#print(word)
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
	#print(LCDict)
def PopularityUpdate(words):
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
	#print(PopularityIndex)


def deleteWords(board,words):
	wordArr = []
	legal = []
	for item in board:
		if(item[LEGALITY][0] == UNSELECTED):
			break
		else:
			print("made")
			wordArr = item[LETTER][:]
			legal = item[LEGALITY][:]
	myDict = {}
	print(len(wordArr), wordArr)
	for i in range(len(wordArr)):
		char = wordArr[i].lower()
		if char not in myDict:
			myDict[char] = 0
		if(legal[i] != WRONG):
			myDict[char] += 1
	i = 0
	result = []
	while(i < len(words)):
		dead = False
		word = words[i]
		if word == "dovey":
			print("dovey was checked")
		wordDict = {}
		for char in word:
			char = char.lower()
			if char not in wordDict:
				wordDict[char] = 0
			wordDict[char] += 1
		for key in myDict:
			if key not in wordDict:
				wordDict[key] = 0
			if(myDict[key] >=1):
				if (myDict[key] > wordDict[key]):
					dead = True
					break
			elif(myDict[key] == 0):
				if(wordDict[key] != 0):
					dead = True
					break

		print(myDict, wordDict, dead)

		if dead:
			# if word == "TZARS":
			# 	# print("HERE!")
			# 	# l = 0
			# 	# while l>-1:
			# 	# 	continue
			print("non-matching: " + word)
			words.remove(word)
			continue
		else:
			word = word.upper()
			print(dead)
			for n in range(len(wordArr)):
				if(legal[n] == CORRECT_POSITION):
					if(wordArr[n] != word[n]):
						print("guess: ", wordArr , " current word: " , word , " n value: " , n)
						dead = True
						break
				elif(legal[n] == CORRECT_WRONG_POSITION):
					if(wordArr[n] == word[n]):
						dead = True
						break

			if(wordArr == list(word)):
				print("other")
				dead = True
				break
			if(dead == True):
				# if word == "TZARS":
				# 	print("HERE!")
				# 	l = 0
				# 	while l>-1:
				# 		continue
				print(word)
				words.remove(word)
				continue
			else:
				# if word == "TZARS" and board != []:
				# 	print("HERE!")
				# 	#input("Hey, listen!")
				i+=1
				result.append(word)
	return result
def get_guess(board,words):
	words = deleteWords(board,words)
	AI_Letter_Count(words)
	PopularityUpdate(words)
	guess = ""
	guessNum = 0
	for key in PopularityIndex:
		if (PopularityIndex[key] > guessNum):
			guessNum = PopularityIndex[key]
			guess = key
	return words,guess
