solution = []

def read_file():
	ans = []
	print("Solving...")
	with open("input.txt", 'r') as f:
		t = int(f.readline())

		for j in range(t):
			details = [int(i) for i in f.readline().split()]
			columns, rows = [], []

			for i in range(3):
				columns.append([int(y) for y in f.readline().split()])

			for i in range(3):
				rows.append([int(y) for y in f.readline().split()])
		
			ans.append(solve(details, columns, rows, j))

	write_file(ans)

def write_file(ans):
	k = 1
	#print(ans)
	with open('output.txt','w') as f:
		for x in ans:
			f.writelines(f"Case #{k}: \n")
			for i in x:
				temp = ''
				for j in range(len(i)):
					temp += str(i[j]) + ' '
				f.writelines(temp)
				f.writelines('\n')
			k+=1

def solve(details, columns, rows, t):

	print(details, columns, rows)
	grid_size = details[0]
	global ship_min, ship_max
	ship_min, ship_max = details[1], details[2]

	# Trials - 

	'''
	output = []
	for x in range(grid_size): output.append([0 for y in range(grid_size)])
	
	output[1][1] = 1
	output[1][2] = 1
	output[1][3] = 1
	output[1][4] = 1
	output[1][6] = 1
	output[1][8] = 1
	output[2][6] = 1
	output[2][8] = 1
	output[3][0] = 1
	output[3][1] = 1
	output[3][2] = 1
	output[3][3] = 1
	output[3][8] = 1
	output[4][8] = 1
	output[5][2] = 1
	output[5][5] = 1
	output[5][6] = 1
	output[5][8] = 1
	output[6][2] = 1
	output[7][2] = 1
	output[7][4] = 1
	output[7][5] = 1
	output[8][2] = 1

	print(output)

	tile_counter(output)
	ship_counter(output)
	max_empty_cell(output)
	
	
	print(transpose(output))
	
	print(is_valid(output, nine, columns, rows))
	print(is_valid([[0,0,0,0,0,0,0,0,0],[0, 1, 1, 1, 1, 0, 1, 0, 1]], nine,  columns, rows))
	'''

	master_list = generate(columns, rows)


	#print('debug 1')
	verify(master_list, grid_size, columns, rows)
	#print(solution)
	ans = [[int(solution[t][i + grid_size*j]) for i in range(grid_size)] for j in range(len(solution[t])//grid_size)]
	#print('FINAL SOLUTION IS', ans)

	print(is_valid(ans, grid_size, columns, rows))
	return transpose(ans)
	
def max_empty_cell(input):
	temp = []
	
	for i in input:
		count = 0
		temp2 = 0
		for j in range(len(i)):
			if i[j] == 0: 
				count+=1
				if count > temp2: temp2 = count
			else:
				count = 0
				
		temp.append(temp2)
	#print(temp)
	return(temp)

def ship_counter(input):
	temp = []

	for i in input:
		ship_count = 0
		k = 0
		for j in range(len(i)):
			if i[j] == 1 and j > k-1:
				if k + 1 > len(i) - 1: break
				ship_count+=1
				k = j
				
				while i[k] == 1: 
					if k + 1 > len(i) - 1: break
					k+=1
		temp.append(ship_count)

	#print(temp)
	return temp


def tile_counter(input):
	temp = []

	for i in input:
		tile_count = 0
		for j in range(len(i)):
			if i[j] == 1:
				tile_count+=1
		temp.append(tile_count)

	#print(temp)
	return temp



def is_valid(input, size, columns, rows):
	#print('is valid input = ', input)
	#for i in range(len(input)):
	if input == [] or input == '': return True
	if type(input) == str: 
		input = [[int(input[i + size*j]) for i in range(size)] for j in range(len(input)//size)]
		length = len(input)
		#print('list to string = ', input)
	
	
	#print('length = ', length)
	else: 
		length = len(input)
		'''
		for l in range(length):
			if tile_counter(input)[l] > columns[0][:length][l]: return False
			if ship_counter(input)[l] > columns[1][:length][l]: return False
			if max_empty_cell(input)[l] > columns[2][:length][l]: return False		
		'''

		
		if tile_counter(input) != columns[0][:length]: 
		#print('loser case 1')
			return False

		if ship_counter(input) != columns[1][:length]: 
		#print('loser case 2')
			return False

		if max_empty_cell(input) != columns[2][:length]: 

		#print('loser case 3')
		#print(max_empty_cell(input))
		#print(columns[2][:length])
			return False

	
	input = transpose(input)
	if length == len(columns[0]):
		#print('hahahahaha')
		

		if tile_counter(input) != rows[0][:length]: return False
		if ship_counter(input) != rows[1][:length]: return False
		if max_empty_cell(input) != rows[2][:length]: return False

	length2 = len(input)
	for l in range(length2):
		if tile_counter(input)[l] > rows[0][:length2][l]: return False
		if ship_counter(input)[l] > rows[1][:length2][l]: return False
		if max_empty_cell(input)[l] > rows[2][:length2][l]: return False
	
	
	#print('yippiie')

	return True

	


def transpose(m):
	m = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
	return m

def generate(columns, rows):
	master_list = []
	length = len(columns[0])
	for i in range(length):
		global sub_list
		sub_list = []
		temp = []
		combinations(length)
		#print(sub_list)
		for j in sub_list: 
			#print('j = ', j)
			#print(tile_counter([j])) #is_valid([j], length, columns, rows): temp.append(j)
			tmp = ship_counter([j])[0]
			if tile_counter([j])[0] == columns[0][i] and tmp == columns[1][i] and max_empty_cell([j])[0] == columns[2][i] : temp.append(j)
		master_list.append(temp)#and ship_counter([j])[0] >= ship_min and ship_counter([j])[0] <= ship_max 
	print('The master list is ', master_list, '\n\n\n')
	return master_list

def combinations(max_depth, depth = 0, send = ''):
	#print('depth = ', depth)
	if depth < max_depth:
		for i in [0, 1]:
			#print(i)
			#print('send = ', send)
			combinations(max_depth, depth + 1, send + str(i))
	if depth == max_depth:
		#print('send = ', send)
		sub_list.append([int(j) for j in send])#[int(j) for j in send]]



def verify(input, size, columns, rows, depth=0, send=''):
    if is_valid(send, size, columns, rows):
        if depth < size:
        	#print(input[0])
        	#print(depth)
        	for i in input[depth]:
        		print(send+ list_to_string(i))
        		if verify(input, size, columns, rows, depth+1, send + list_to_string(i)):
        			return True
        	return False
        solution.append(send)
        return True   
    return False


def list_to_string(list_str):
	string_from_list = ''
	for i in list_str: string_from_list += str(i)
	return string_from_list

read_file()

#sub_list = []

#combinations(3)

#print(sub_list)

