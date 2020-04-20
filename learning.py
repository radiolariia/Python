list_1 = [1,2,3,4,5,6]
list_1 = list()
list_1 = [1] * 3 == [1,1,1]

list_generator = [ i for i in range(5) if i % 2 == 0]
# list_generator = [0,2,4]			  # we can add conditions
list_1[0:2] # = [1,3,5] [start: stop: step]
list_1[::-1] # = [6,5,4,3,2,1]

# list.insert(i,x) 				- вставляет х на место і
# list.pop([i])	   				- удаляет и возвращает і-й элемент
# list.index(x,[start [, end]]) - returns положение 1st element with value x( searching from start to end)
# list.sort([key = функция])				- sorts a list according to function



TUPLE - КОРТЕЖ и он неизменный!

tuple_1 = ( 0, ...)
tuple_1 = tuple()

tuple_1 = ([], [])
tuple_1[0].append(0) # tuple_1 = ([0], [])




STRING - unchangeable!

string = 'It`s a string' # + * 
print(string[::-1])      # reverse


# string.upper()
# 	  .lower() 
# 	  .isdigit()  

# 'a b c'.replace(' ', '')         # 'abc'

# 'a b c'.split()                  # ['a', 'b', 'c'] - разбиение строки по разделителю в список, по умолчанию пробел.

# 'bar'.isalpha() 				 # True

# 'hello, world'.title()           # 'Hello, World'

# 'Hello, World'.swapcase()        # 'hELLO, wORLD'

# ', '.join(['a', 'b', 'c'])       # 'a, b, c'




dictionary = {1: 'a', 2: 'b'}
dictionary = dict(1: 'a', 2: 'b')

dictionary = dict([(1, 'a'), (2, 'b')]) 
# Также в функцию можно передать список, состоящий из кортежей длиной 2 - ключ и значение.

dictionary = {i: i * 2 for i in range(5)}
{0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

dictionary['3'] = 'c' # {1: 'a', 2: 'b', 3: 'c'}
dictionary[1] = 'd'   # {1: 'd', 2: 'b', 3: 'c'}

# dict.fromkeys(seq[, value]) # seq - keys, value - values (по умолчанию None)
# dict.get(key[, default])
# dict.pop(key[, default])
# dict.setdefault(key[, default])



SET - МНОЖИНА

a = set()
a = set('hello')  			   # {'o', 'h', 'l', 'e'}
a = {'a', 'b', 'c'}

a = {i ** 2 for i in range(5)} # {0, 1, 4, 9, 16}

!!!   a = { } 	# It`s a dictonary

FROZENSET - unchangeable

a = frozenset([1, 'b', 78])

# x in s 		# Is x in s? True/False

# set.isdisjoint(other) # True if set and other don`t contain joint elements

# set.issubset(other)   =   set <= other # set вливається в other
# set.issuperset(other)   =   set >= other 


# set.union(other, ...)   =   set | other | ... 		# Uniting set, other ...
# set.intersection(other, ...)   =   set & other & ...  # Intersection of...
# set.difference(other, ...)   =   set - other - ... 
# set.symmetric_difference(other)   =   set ^ other
# set.copy() - копия множества.
# # These operators CREATE NEW sets
# |=
# &= 
# -= 
# ^=  # These operators CHANGE sets

# set.add(elem) 
# set.remove(elem) 
# set.discard(elem) 
# set.pop()




MODULES` PRIORITY

- home directory
- PYTHONPATH directories
- Standard library directories
- paths from .pth files
- other developers` packages

from module import variable as newVariableName



FUNCTIONNNN
 
# Static typization
def add(a: int, b: int) -> int:
	  # Arguments` types	Return`s type 
	  #   definition		 definition
    return a + b

print(add(10, 15))                # 25
print(add('still', 'works'))      # 'still works'

def add(a, b, c = 0): # c - optional argument
    return a + b + c

print(add(2, 3))            # 5
print(add(2, 3, 5))         # 10