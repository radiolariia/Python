counter_dict = {}

with open('Training_01.txt') as f:
	line = f.readline()

	while line:
		line = line.split('/', 3)[2]

		if line in counter_dict:
			counter_dict[line] += 1
		else:
			counter_dict[line] = 1
		line = f.readline()

	print(counter_dict)



