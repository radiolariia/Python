while True:
    num = input('Enter your number: ')

    if num.isnumeric() == False:
        print('False')
    else:
        break
    
def parse_number(num):
    
    odds = 0
    evens = 0

    i = 0
    for i in range(0, len(num)):

    	if (int(num[i]) % 2) == 0:
    		evens +=1
    	else:
    		odds +=1
    	
    	
    dictionary = {}
    dictionary['odd'] = odds
    dictionary['even'] = evens
	    
    return dictionary

dictionary = parse_number(num)

print(dictionary)
            
