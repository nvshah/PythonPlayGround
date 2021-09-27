#1.
def matrix(n):
	return (
		(i * j for j in range(1, n + 1)) for i in range(1, n + 1)
	)

def matrix_iterator(n):
	for r in matrix(n):
		yield from r

*mi, = matrix_iterator(3)
print(mi)

#2.
f1 = 'naruto.txt'
f2 = 'deathnote.txt'
f3 = 'onepiece.txt'
files = f1, f2, f3
animes = []

def get_clean_data(f):
	with open(f) as f:
		for l in f:
			yield l.strip('\n')

def animes(*files):
	for f in files:
		yield from get_clean_data(f)
