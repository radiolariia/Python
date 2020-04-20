print('lab5\nSofiia Hrynevych \nІПЗ-11 \nVariant 3')

def binomial_coefficient(n, k):
		if n < k:
			return (print('It`s impossible to calculate a factorial value of negative number!'))
		if k == 0 or k == n:
			return 1
		else:
			return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)

while True:
	n = int(input(' n = '))
	if n > 0:
		break
	else:
		print(' n must be a natural number!')

k = int(input(' k = '))

print('Value of C(%d,%d) is (%s)' % (n , k , binomial_coefficient(n , k)))
