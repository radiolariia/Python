print('Let`s play a game! \nI`ll guess your number between 0 and 100!')

first = 0
last = 100

while True:
	mid = (first + last) // 2
	print('\nHmmm... I think your number is ' + str(mid))

	print('\nSay if my prediction is: too low \n\
		         too high \n\
		     or  right')
	answer = input('Your turn: ').lower()
	if answer == 'right':
		print('Wow! I did it!')
		break
	elif answer == 'too high':
		last = mid - 1
	elif answer == 'too low':
		first = mid + 1
	elif answer == 'exit':
		break







