import string
import random

size = input('How long is your password? ')

def gen_password(k):
	chars = string.ascii_letters + string.digits + string.punctuation
					
	return ''.join(random.choice(chars) for i in range(k))

while size != 'exit':
	print(gen_password(int(size)))

	size = input('How long is your password? ')


	
