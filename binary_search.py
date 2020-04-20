import random

def binary():	
	a = random.randint(0, 100)
	a_list = [random.randint(0,100) for i in range(0, random.randint(10,17))]

	print(a)
	print(sorted(a_list))

	first = 0
	last = len(a_list) - 1

	found = False

	while( first <= last a nd not found):
		mid = (first + last) // 2

		if a_list[mid] == a :
			found = True
		else:
			if a < a_list[mid]:
				last = mid - 1
			else:
				first = mid + 1

	return found

print(binary())
