import math

print('Lab 2 \nSofiia Hrynevych \nIПЗ-11 \nVariant 3\n \nTASK 1')
def s():
    print('\n')
s()
r = float(input('R = '))
length = (2*math.pi)*r
area = math.pi*(r**2)
s()
print('Length of the circle: {0:5.3f} \nArea of the circle: {1:5.3f}'.format(length,area))
s()

print('TASK2')
s()
d2 = float(input('D ='))
area2 = math.pi*((d2/2)**2)
s()
print('Area of the circle: {0:5.3f}'.format(area2))
s()

print('TASK3')
s()
length3 = float(input('Length = '))
r3 = length3/(2*math.pi)
s()
print('Radius: {0:5.3f}'.format(r3))
s()

print('TASK4')
s()
area4 = float(input('Area of the circle = '))
d4 = math.sqrt((area4/math.pi))*2
print('Diameter: {0:5.3f}'.format(d4))
s()

print('TASK5')
s()
catA = float(input('Cathetus A = '))
catB = float(input('Cathetus B = '))
hyp = math.hypot(catA, catB)
print('Hypotenuse: {0:5.3f}'.format(hyp) )
s()

print('TASK6')
s()
catB6 = float(input('Cathetus B = '))
hyp6 = float(input('Hypotenuse = '))
catA6 = math.sqrt((math.pow(hyp6,2) - math.pow(catB6,2)))
print('Cathetus A = {0:5.3f}'.format(catA6))


