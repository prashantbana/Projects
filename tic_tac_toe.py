# Step 1: Print welcome message.
# Step 2: Display board
# Step 3: Ask Players to mark the position
# Step 4: After every input, display updated board
# Step 5: After every input, check the ending conditions
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
	

def check_ending_conditions(value):
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

	if flag == False:
		print(f'{value} is the winner')
	if value == 'X':
		next_value = 'O'
	else:
		next_value = 'X'
	return (next_value, flag)

def game():
	"""Start playing the game"""
	
	welcome_message()
	flag = True
	value = 'X'
	while flag:
		user_input = int(input('Please choose a position to mark (1-9): '))
		sample[sample.index(user_input)] = value
		value, flag = check_ending_conditions(value)
		display_board()

game()