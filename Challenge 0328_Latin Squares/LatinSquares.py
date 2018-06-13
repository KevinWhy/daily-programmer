#!py -3
#
#Input Description
#Let the user enter the length of the array followed by n x n numbers. Fill an array from left to right starting from above.
#
#Output Description
#If it is a Latin square, then display true. Else, display false. 
#

num_lines = int(input('# of lines: '))
numbers = input('Input: ').split(' ')
numbers.reverse() # First number = end of array
print()

column_sets = [] # Index = index in the line. Value = set of chars in that index
for i in range(num_lines):
	column_sets.append(set())

# Read each line
errors = []
lines = [] # Used to print the square
for line_iter in range(num_lines):
	lines.append([])
	for column_iter in range(num_lines):
		curr_num = numbers.pop()
#		print('char:', curr_num, 'str index',column_iter,':', column_sets[column_iter]) # DEBUG
		# If number was already in this column, stop
		if curr_num in column_sets[column_iter]:
			errors.append('#{0} was in column {1} multiple times!'.format(curr_num, column_iter))
		else:
			column_sets[column_iter].add(curr_num)
		
		# Print the row
		lines[line_iter].append(curr_num)
	print(lines[line_iter])
print()
# If errors were found, print them (and then stop the program)
for error in errors:
	print(error)
if errors:
	exit()

# Columns are okay. Check each row
for set in column_sets:
	if set != column_sets[0]:
		print('Column', column_sets.index(set), 'does not have the same numbers!')
		exit()

print('Input is a Latin Square')
