#!py -3

# Replaces a-z with other characters.
# Intended for ROT13.
#
# Cypher files must be in Unicode.
# Each line = one substitution.
#     Format:input letter>OUTPUT LETTER(s)

import string

# Ask for file to open
cypher_filename = input('cypher file: ')

# Read cypher from file
cypher = {}
with open(cypher_filename, 'r', encoding='utf-8') as cypher_file:
	for line in cypher_file:
		parts = line.rstrip('\n').partition('>')
		if len(parts[1]) > 0:
			cypher[ parts[0] ] = parts[2]


# Convert input, one letter at a time
while True:
	input_str = input('Input string: ')
	out_str = ''
	for letter in input_str:
		if letter in cypher:
			out_str += cypher[letter]
		else:
			out_str += letter

	print(out_str)
	print('')
