DIMENSIONS = 6 # board dimensions 
EMPTY_CHAR = 'E'

# check space above and below of the current space | return case val and its corresponding coordinates
def check_vertical(x, y, board, player, opponent):
	coordinates = [(x,y)]
	vertical = 1
	empty_spaces = 0
	j = y
	counter = 0
	while(j != 0): # check above space 
		counter += 1
		curr = board[x][j-1] # current character space 
		if curr == player:
			vertical += 1
			j-=1
			coordinates.append((x,j))
			continue
		elif curr == opponent:
			break
		elif curr == EMPTY_CHAR:
			empty_spaces += 1
			break

	# check spaces below 
	j = y
	while(j != DIMENSIONS-1):
		counter += 1
		curr = board[x][j+1]
		if curr == player:
			vertical += 1
			coordinates.append((x,j))
			j+=1
			continue
		elif curr == opponent:
			break
		elif curr == EMPTY_CHAR:
			empty_spaces += 1
			break

	# sort list using x coordinate values 
	coordinates = sorted(coordinates, key=lambda coord_char: coord_char[0])
	if vertical >= 4:
		return 4, coordinates, counter
	elif vertical <= 1 or empty_spaces == 0:
		coordinates = []
		return 0, coordinates, counter
	elif vertical == 2:
		return 3, coordinates, counter
	elif vertical == 3:
		if empty_spaces == 1:
			return 2, coordinates, counter
		elif empty_spaces == 2:
			return 1, coordinates, counter

def check_horizontal(x, y, board, player, opponent):
	coordinates = [(x,y)]
	horizontal = 1 # counter variable for horizontal values
	empty_spaces = 0 # num of empty spaces 

	# check spaces left of current space
	i = x
	counter = 0
	while(i != 0):
		counter += 1
		curr = board[i-1][y] # current character space 
		if curr == player:
			horizontal = horizontal + 1
			coordinates.append((i,y))
			i = i - 1
			continue
		elif curr == opponent:
			break
		elif curr == EMPTY_CHAR:
			empty_spaces = empty_spaces + 1
			break

	# checking right spaces 
	i = x
	while(i != DIMENSIONS-1):
		counter = counter + 1
		curr = board[i+1][y]
		if curr == player:
			horizontal = horizontal + 1
			coordinates.append((i,y))
			i = i + 1
			continue
		elif curr == opponent:
			break
		elif curr == EMPTY_CHAR:
			empty_spaces = empty_spaces + 1
			break

	# return case and coordinates list 
	coordinates = sorted(coordinates, key=lambda coord_char: coord_char[0])
	if horizontal >= 4:
		return 4, coordinates, counter
	elif horizontal <= 1 or empty_spaces == 0:
		coordinates = []
		return 0, coordinates, counter
	elif horizontal == 2:
		return 3, coordinates, counter
	elif horizontal == 3:
		if empty_spaces == 1:
			return 2, coordinates, counter
		elif empty_spaces == 2:
			return 1, coordinates, counter

def check_diagonal_down(x, y, board, player, opponent):
	coordinates = [(x,y)]
	diagonal = 1
	empty_spaces = 0
	counter = 0
	# check left-up spaces
	i, j = x, y
	while(i != 0 and j != 0):
		counter += 1
		curr = board[i-1][j-1]
		if curr == player:
			diagonal += 1
			coordinates.append((i,j))
			i-=1
			j-=1
			continue
		elif curr == opponent:
			break
		elif curr == EMPTY_CHAR:
			empty_spaces += 1
			break
	# check right-down space
	i, j = x, y
	while(i != DIMENSIONS-1 and j != DIMENSIONS-1):
		counter += 1
		curr = board[i+1][j+1]
		if curr == player:
			diagonal += 1
			coordinates.append((i,j))
			i+=1
			j+=1
			continue
		elif curr == opponent:
			break
		elif curr == EMPTY_CHAR:
			empty_spaces += 1
			break

	# return case number and coordinate list
	coordinates = sorted(coordinates, key=lambda coord_char: coord_char[0])
	if diagonal >= 4:
		return 4, coordinates, counter
	elif diagonal <= 1 or empty_spaces == 0:
		coordinates = []
		return 0, coordinates, counter
	elif diagonal == 2:
		return 3, coordinates, counter
	elif diagonal == 3:
		if empty_spaces == 1:
			return 2, coordinates, counter
		elif empty_spaces == 2:
			return 1, coordinates, counter


def check_diagonal_up(x, y, board, player, opponent):
	coordinates = [(x,y)]
	diagonal = 1
	empty_spaces = 0

	# check left-down space
	i, j = x, y
	counter = 0
	while(j != DIMENSIONS-1 and i != 0):
		counter += 1
		curr = board[i-1][j+1]
		if curr == player:
			diagonal += 1
			coordinates.append((i,j))
			i-=1
			j+=1
			continue
		elif curr == opponent:
			break
		elif curr == EMPTY_CHAR:
			empty_spaces += 1
			break

	# Checking Right and Up
	i, j = x,y
	while(j != 0 and i != DIMENSIONS-1):
		counter += 1
		curr = board[i+1][j-1]
		if curr == player:
			diagonal += 1
			coordinates.append((i,j))
			i+=1
			j-=1
			continue
		elif curr == opponent:
			break
		elif curr == EMPTY_CHAR:
			empty_spaces += 1
			break

	# return corresponding case and coordinate list 
	coordinates = sorted(coordinates, key=lambda coord: coord[0])
	if diagonal >= 4:
		return 4, coordinates, counter
	elif diagonal <= 1 or empty_spaces == 0:
		coordinates = []
		return 0, coordinates, counter
	elif diagonal == 2:
		return 3, coordinates, counter
	elif diagonal == 3:
		if empty_spaces == 1:
			return 2, coordinates, counter
		elif empty_spaces == 2:
			return 1, coordinates, counter


"""
actions:
   action1: three-two-open
   action2: three-one-open
   action3: two-open
"""
def populate_lists(x,y, board, player, opponent, action1, action2, action3, win, check_function):
	nodes = 0
	case, coordinates, num_nodes = check_function(x, y, board, player, opponent)
	nodes += num_nodes
	if coordinates:
		if case == 1:
			if coordinates not in action1:
				action1.append(coordinates)
		elif case == 2:
			if coordinates not in action2:
				action2.append(coordinates)
		elif case == 3:
			if coordinates not in action3:
				action3.append(coordinates)
		elif case == 4:
			if coordinates not in win:
				win.append(coordinates)
	return nodes

"""
actions:
   action1: three-two-open
   action2: three-one-open
   action3: two-open
"""
def heuristic(x, y, board, player, opponent, player_win, opponent_win):
	player_action1 = []
	player_action2 = []
	player_action3 = []

	opponent_action1 = []
	opponent_action2 = []
	opponent_action3 = []

	total_nodes = 0

	for i in range(DIMENSIONS):
		for j in range(DIMENSIONS):
			if board[i][j] == EMPTY_CHAR:
				continue
			elif board[i][j] == player:
				total_nodes += populate_lists(i, j, board, player, opponent, player_action1, player_action2, player_action3, player_win, check_vertical) 
				total_nodes += populate_lists(i, j, board, player, opponent, player_action1, player_action2, player_action3, player_win, check_horizontal) 
				total_nodes += populate_lists(i, j, board, player, opponent, player_action1, player_action2, player_action3, player_win, check_diagonal_up) 
				total_nodes += populate_lists(i, j, board, player, opponent, player_action1, player_action2, player_action3, player_win, check_diagonal_down)
			elif board[i][j] == opponent:
				total_nodes += populate_lists(i, j, board, opponent, player, opponent_action1, opponent_action2, opponent_action3, opponent_win, check_vertical)
				total_nodes += populate_lists(i, j, board, opponent, player, opponent_action1, opponent_action2, opponent_action3, opponent_win, check_horizontal)
				total_nodes += populate_lists(i, j, board, opponent, player, opponent_action1, opponent_action2, opponent_action3, opponent_win, check_diagonal_up)
				total_nodes += populate_lists(i, j, board, opponent, player, opponent_action1, opponent_action2, opponent_action3, opponent_win, check_diagonal_down)


	#if there is a successful win condition on the board make it a large value
	# if player_win:
	# 	return 1000000000, total_nodes

	# #if there is a bad win condition on the board make it a low value
	# if opponent_win:
	# 	return -1000000000, total_nodes

	p_a1 = len(player_action1)
	p_a2 = len(player_action2)
	p_a3 = len(player_action3)

	o_a1 = len(opponent_action1)
	o_a2 = len(opponent_action2)
	o_a3 = len(opponent_action3)

	heuristic = (5 * p_a1) - (10 * o_a1) + (3 * p_a2) - (6 * o_a2) + p_a3 - o_a3

	return heuristic, total_nodes