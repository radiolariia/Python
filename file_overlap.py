def file_to_list_of_ints(filename):
	list_to_return = []

	with open(filename) as f:
		line = f.readline()
		
		while line:
			list_to_return.append(int(line))
			line = f.readline()
	return list_to_return

primeslist = file_to_list_of_ints('primenumbers.txt')
happieslist = file_to_list_of_ints('happynumbers.txt')

overlaplist = [elem for elem in primeslist if elem in happieslist]
print(overlaplist)

			



