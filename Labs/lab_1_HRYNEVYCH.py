print('lab1\nSofiia Hrynevych \nІПЗ-11\n')

print('TASK1')
lastname = input('Ваше прізвище: ')
city = input('Де Ви живете: ')

def space():
    print('\n')
space()
print('Ваше прізвище: ',lastname)
print('Ви живете в ',city)
space()

print('TASK2')
a = float(input('А = '))
b = float(input('B = '))

while True:
    c = float(input('C = '))
    if c > 0:
        break
    
d = float(input('D = '))

space()

print('A = {0:5.3f} B = {1:5.3e} C = {2:5.3f} D = {3:5.3f}'.format(a, b, c, d))

space()

print('X=(-2.25(A + 2C))/(B - D^0.5)')

space()

if (b - (d**0.5)) != 0:
    x = (-2.25*(a + (2*(b*c))))/(b - (d**0.5))

    print('X =', x)

    if x > 0:
        print('X - додатнє число!')
    elif x == 0:
        print('X - нуль!')
    else:
        print("Це від`'ємне число!")
else:
    print('Ділити на 0 не можна!')
