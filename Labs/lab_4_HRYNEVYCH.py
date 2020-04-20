print('lab4\nSofiia Hrynevych \nІПЗ-11 \nVariant 3')

import math

def result(x, minIterations = 20):

    term = x
    term_prev = math.nan
    n = 1
    result = 1 

    while not(abs(term - term_prev) <= accuracy and (minIterations <= 0)):
        term_prev = term
        result += term
        n += 1
        term *=  x / n
        minIterations -=1
    return result


x = float(input('Початкове значення X:'))
x_end = float(input('Кінцеве значення X:'))
accuracy_step = float(input('Точність розрахунків, 10^(-n), де n='))
accuracy = pow(10,(-1) * accuracy_step)

print(70 * '=')
print('      x     y              standart           error')
print(70 * '=')

while x <= x_end:
    if x >= 0 and x <= 2:
        y1 = math.exp(-x) + math.exp((-2)*x)
        y2 = result(-x) + result((-2)*x)
        dif = abs(abs(y1) - abs(y2))
    elif x > 2:
        y1 = math.exp((x + 5))
        y2 = result((x + 5))
        dif = abs(y1 - y2)
    else:
        print('     %4.1f  ' % (x), 'Undefined')
        x += 0.5
        continue
    print('     %4.1f   %4.9f    %4.9f        %4.9f' % (x, y2, y1, dif))
    x += 0.5
print('END')
