import math

print('Lab 3 \nSofiia Hrynevych \nIПЗ-11 \nVariant 3 \nTASK 1')

accuracy = float(input('Введіть точність: '))
result= 0

print('=================================================================================================')
print('        x                  k                          member                           sum       ')
print('=================================================================================================')
								   								   
for x in range(1, 6):
    k = 0
    member = x
    while abs(member) > accuracy :
        member = ((-1)**(k+1)*(x**(2*k-1)))/((2*k-1)*math.factorial(k))
        result += member
        
        space1 = (17-len(str(k)))*' '
        space2 = (28-len(str(member)))*' '
        space3 = (30-len(str(result)))*' '

        print(7*' ', x, space1, k, space2, member, space3, result)

        k += 1

print('==================================================================================================')
print('sum =', result)
