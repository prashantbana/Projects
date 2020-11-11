# Step 1: Print welcome message.
# Step 2: Display board
# Step 3: Ask Players to mark the position
# Step 4: Check if values player inputs are not overwritten
# Step 5: After every input, display updated board
# Step 6: After every input, check the ending conditions
# TODO: Check for wrong input values

sample = [1,2,3,4,5,6,7,8,9]

def welcome_message():
	"""prints the welcome message"""

	print("---------------WELCOME TO TIC TAC TOE---------------")
	
def display_board():
	"""marks/displays the board"""

	print('\n')
	print(" "+str(sample[0])+" | "+str(sample[1])+" | "+str(sample[2])+ " ")
	print("---|---|---")
	print(" "+str(sample[3])+" | "+str(sample[4])+" | "+str(sample[5])+ " ")
	print("---|---|---")
	print(" "+str(sample[6])+" | "+str(sample[7])+" | "+str(sample[8])+ " ")
	print('\n')
	
def validate_input(user_input):
	"""Validates the user input"""

	return 'X' == sample[user_input-1] or 'O' == sample[user_input-1]

def change_pointer(value, flag):
	"""Switches between X and O and displays the winner"""

	if value == 'X':
		next_value = 'O'
	else:
		next_value = 'X'
	
	if flag == False:
		print(f'{value} is the winner')
	else:
		return next_value

def check_ending_conditions():
	"""Checks the ending conditions of the game after each move"""

	# End game when 3 in a row or diagonal
	if (sample[0] == sample[1] == sample[2]) or (sample[3] == sample[4] == sample[5]) or (sample[6] == sample[7] == sample[8]):
		flag = False
	elif (sample[0] == sample[3] == sample[6]) or (sample[1] == sample[4] == sample[7]) or (sample[2] == sample[5] == sample[8]):
		flag = False
	elif (sample[0] == sample[5] == sample[8]) or (sample[3] == sample[5] == sample[6]):
		flag = False
	else:
		flag = True
	return flag

def game():
	"""Start playing the game"""
	
	welcome_message()
	flag = True
	value = 'X'
	display_board()
	while flag:
		user_input = int(input('Please choose an available position to mark (1-9): '))
		if not validate_input(user_input):
			sample[sample.index(user_input)] = value
			display_board()
			flag = check_ending_conditions()
			value = change_pointer(value, flag)

		else:
			print(f'Errr ! Position {user_input} is already taken. Please mark another position')

game()