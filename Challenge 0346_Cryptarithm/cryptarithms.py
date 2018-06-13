#!py -3
# cryptarithms.py
#	Solves a math puzzle.
#
#######################################
#	Input: Some strings & their sum
#		Example: "SEND + MORE == MONEY"
#		   SEND
#		+  MORE
#		-------
#		  MONEY
#	
#	Output: What each letter represents.
#		Example: O = 0,
#		         M = 1,
#		         Y = 2,
#		         E = 5,
#		         N = 6,
#		         D = 7,
#		         R = 8,
#		     and S = 9.
#			(i.e. 9567 + 1085 = 10652)
#	
#	Other samples:
#		THIS + IS + HIS == CLAIM
#		{"A"=>7, "C"=>1, "H"=>8, "I"=>5, "L"=>0, "M"=>6, "S"=>2, "T"=>9}
#		
#		WHAT + WAS + THY == CAUSE
#		{"A"=>0, "C"=>1, "E"=>4, "H"=>2, "S"=>3, "T"=>6, "U"=>7, "W"=>9, "Y"=>5}
#######################################

from collections import OrderedDict # To print output

# Converts a word to a number.
# Uses a mapping dictionary (keys = letters, values = numbers, as characters)
def wordToNumber(word, mapping):
	translation = str.maketrans(mapping) # Convert word to dictionary of numbers
	return int(  word.translate(translation)  )

# Convert a number to a word.
# Uses a mapping dictionary (keys = letters, values = numbers, as characters)
def numberToWord(num, mapping):
	numMapping = {numChar: letter for letter,numChar in mapping.items()} # Flip the mapping so key = number, value = letters
	translation = str.maketrans(numMapping)
	return str(num).translate(translation)

#######################################

def recurseAllMappings(mappingBlacklist, currMapping,lettersLeft,numbersLeft, iterateMapping):
	currLetter = lettersLeft.pop()
	for currNum in numbersLeft:
		# If currLetter can't be mapped to currNum, skip this mapping
		if currNum in mappingBlacklist.get(currLetter, []):
			continue
		
		# Reserve currNum in numbersLeft
		nextNumbersLeft = numbersLeft.copy()
		nextNumbersLeft.remove(currNum)
		# Add this letter & number to the mapping
		currMapping[currLetter] = currNum
		
		# Try to continue recursion
		if len(lettersLeft) > 0:
			recurseAllMappings(mappingBlacklist, currMapping,lettersLeft.copy(),nextNumbersLeft, iterateMapping)
		# When mapping is complete, run a function
		else:
			iterateMapping(currMapping)

#LETTERS_TEST = ['a','b','c','d']
NUM_STRS = [str(i) for i in range(0,10)] # Convert numbers [0 - 9] into one-character strings
#def ITER_TEST(mapping):
#	str = mapping['a'] +mapping['b'] +mapping['c'] +mapping['d']
#	print(str)
#recurseAllMappings({}, LETTERS_TEST, NUM_STRS, ITER_TEST)

#######################################

inStr = input('Input cryptarithm (Math equation using letters): ')
inStr = inStr.strip('"').strip("'") # Remove quotes from the input
print('')
# Break input into the left & right sides of equation
leftSide = inStr.partition('=')[0].strip()
sumStr = inStr.rpartition('=')[2].strip()
# Break input into the words to use
words = [word.strip() # Remove whitespace...
		for word in leftSide.split('+')]
# Find all letters used
lettersDict = {} # Stored in a dictionary so that repetitions don't make extra entries
for word in (words +[sumStr]):
	for letter in word:
		lettersDict[letter] = True
letters = list(lettersDict.keys()) # Convert dictionary to list
assert len(letters) <= 10,'Input uses too many letters. (We only have the numbers 0 - 9...)'

# Add blacklist: Can't start number with 0s
mappingBlacklist = {word[0]: ['0']      for word in (words +[sumStr])}

# Brute force: Guess & check all possible combinations
def iterateMapping(mapping):
	# Check the current mapping...
	sum = 0
	for word in words:
		sum += wordToNumber(word, mapping)
	# If the sums matched, this mapping works.
	if sum == wordToNumber(sumStr, mapping):
		print('mapping found: {'
				+ ', '.join(['"'+ word +'"' +'=>' +numChar # Print dictionary like the examples do
						for word,numChar
						in OrderedDict(sorted(mapping.items(), key=lambda t: t[0])).items() # Sort dictionary (code from Python docs)
				]) +'}')
		print('\t',
				' + '.join([str(wordToNumber(word, mapping)) for word in words]),
				'=',sum)
recurseAllMappings(mappingBlacklist,  {}, letters, NUM_STRS,  iterateMapping)
