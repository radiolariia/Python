import math

print('Lab 2 \nSofiia Hrynevych \nIПЗ-11 \nTASK 1')
def s():
    print('\n')
s()
while True: 
	a = float(input('Основа рівнобедренного трикутника = '))
	b = float(input('Бічна сторона трикутника = '))

	if (a > 0 and b > 0) and ((2 * b) > a): 
		break
	s()
	print('It`s an impossible triangle! \nTry again!')

area = round((a/2)*math.sqrt((b**2)-((a**2)/4)))
s()
print(area)
s()
if area % 2 == 0:
	print(area/2)
else:
	print('Не можу ділити на 2!')
