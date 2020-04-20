print('lab5\nSofiia Hrynevych \nІПЗ-11 \nVariant 3')
print('\n3.	З рядку вилучити всі слова на непарних порядкових позиціях, а слова на парних позиціях надрукувати перевернутими.')

line = input('Enter your sentence:')
line = line.split()
print(line)

new_line = []
for i in range(len(line)):
	if i % 2 == 1:
		new_line.append(line[i][::-1])
line = new_line

print(line)
