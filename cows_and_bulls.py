import random

def cows_and_bulls():
	num = str(random.choice(range(1000, 9999)))
	prompts = 0
	print(num)
	while True:	
		guess = str(input('Try to guess: '))
		prompts += 1
		print(guess)
		cows = 0
		bulls = 0

		for i in range(len(num)):
			if guess == 'exit':
				break
			else:
				if guess[i] == num[i]:
					cows += 1
				elif (guess[i] != num[i]) and (guess[i] in num):
					bulls += 1

		if cows == 4:
			print('Exactly right!')
			break

		print(str(cows) + ' cows, ' + str(bulls) + ' bulls \nPrompts: ' + str(prompts))
		print('Try again!')
	return cows, bulls

cows_and_bulls()

