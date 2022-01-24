

#Дан строка, она состоит только из букв английского алфавита.
#Первый участник пишет сбор статистики - какие буквы сколько
#раз встречаются.

name = input('Enter a suggestion:')
book = input('Enter the letter to count:')
s = 0
for i in name:
	if i in book:
		s += 1
print(s)

s = input('введите предложение:')
i = 0
letter = 0
letter1 = 0
while i < len(s):
	if s[i] in 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЮЯ':
		letter += 1
	elif s[i] in 'абвгдежзийклмнопрстуфхцчшщьюя':
		letter1 += 1
	i += 1
print('длина строки', len(s))
print ('прописных букв', letter)
print('строчных букв', letter1)





banner =  '''
########    ########   ###       ####   ########        #####        ###      ##   ##      ##   ##
 ##     ##   ##    ##   ## #     ## ##   ##     ##      ##   ##       ## #     ##   ##      ##   ##
##     ##   ##    ##   ##  #   ##  ##   ##     ##     ##     ##      ##  #    ##   ##      ##   ##
########    ##    ##   ##   # ##   ##   ########     ##       ##     ##   #   ##   ##      ##   ##
##     ##   ##    ##   ##    ##    ##   ##     ##   #############    ##    #  ##   ##      ##   ##
##     ##   ##    ##   ##          ##   ##     ##  ##           ##   ##     # ##   ##      ##   ##
########    ########   ##          ##   ########  ##             ##  ##      ###   ##########   #########
'''

print(banner)
        



vvod = input('enter a suggestion:')
dlina = 0
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0
l = 0
m = 0
n = 0
o = 0
p = 0
q = 0
r = 0
s = 0
t = 0
u = 0
v = 0
w = 0
x = 0
y = 0
z = 0


while dlina < len(vvod):
	if vvod[dlina] in 'a':
		a += 1
	elif vvod[dlina] in 'b':
		b += 1
	elif vvod[dlina] in 'c':
		c += 1
	elif vvod[dlina] in 'd':
		d += 1
	elif vvod[dlina] in 'e':
		e += 1
	elif vvod[dlina] in 'g':
		g += 1
	elif vvod[dlina] in 'h':
		h += 1
	elif vvod[dlina] in 'i':
		i += 1
	elif vvod[dlina] in 'j':
		j += 1
	elif vvod[dlina] in 'k':
		k += 1
	elif vvod[dlina] in 'l':
		l += 1
	elif vvod[dlina] in 'm':
		m += 1
	elif vvod[dlina] in 'n':
		n += 1
	elif vvod[dlina] in 'o':
		o += 1
	elif vvod[dlina] in 'p':
		p += 1
	elif vvod[dlina] in 'q':
		q += 1
	elif vvod[dlina] in 'r':
		r += 1
	elif vvod[dlina] in 's':
		s += 1
	elif vvod[dlina] in 't':
		t += 1
	elif vvod[dlina] in 'u':
		u += 1
	elif vvod[dlina] in 'v':
		v += 1
	elif vvod[dlina] in 'w':
		w += 1
	elif vvod[dlina] in 'x':
		x += 1
	elif vvod[dlina] in 'y':
		y += 1
	elif vvod[dlina] in 'z':
		z += 1
	elif vvod[dlina] in 'A':
		a += 1
	
	# верхний регистр

	elif vvod[dlina] in 'B':
		b += 1
	elif vvod[dlina] in 'C':
		c += 1
	elif vvod[dlina] in 'D':
		d += 1
	elif vvod[dlina] in 'E':
		e += 1
	elif vvod[dlina] in 'G':
		g += 1
	elif vvod[dlina] in 'h':
		h += 1
	elif vvod[dlina] in 'I':
		i += 1
	elif vvod[dlina] in 'J':
		j += 1
	elif vvod[dlina] in 'K':
		k += 1
	elif vvod[dlina] in 'L':
		l += 1
	elif vvod[dlina] in 'M':
		m += 1
	elif vvod[dlina] in 'N':
		n += 1
	elif vvod[dlina] in 'O':
		o += 1
	elif vvod[dlina] in 'P':
		p += 1
	elif vvod[dlina] in 'Q':
		q += 1
	elif vvod[dlina] in 'R':
		r += 1
	elif vvod[dlina] in 'S':
		s += 1
	elif vvod[dlina] in 'T':
		t += 1
	elif vvod[dlina] in 'U':
		u += 1
	elif vvod[dlina] in 'V':
		v += 1
	elif vvod[dlina] in 'W':
		w += 1
	elif vvod[dlina] in 'X':
		x += 1
	elif vvod[dlina] in 'Y':
		y += 1
	elif vvod[dlina] in 'Z':
		z += 1


	dlina += 1
print('string length', len(vvod))
print('quantity of letter A', a)
print('                   B', b)
print('                   C', c)
print('                   D', d)
print('                   E', e)
print('                   G', g)
print('                   H', h)
print('                   I', i)
print('                   J', j)
print('                   K', k)
print('                   L', l)
print('                   M', m)
print('                   N', n)
print('                   O', o)
print('                   P', p)
print('                   Q', q)
print('                   R', s)
print('                   T', u)
print('                   V', v)
print('                   W', w)
print('                   X', x)
print('                   Y', y)
print('                   Z', z)











