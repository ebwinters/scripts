def isTriple(a,b,c):
	if ((a*a) + (b*b)) == c*c:
		return True
	else:
		return False




trips = []
for i in xrange(1, 1001):
	for j in xrange(1, 1001):
		for k in xrange(1, 1001):
			if isTriple(i,j,k) and i+j+k == 1000:
				print (i)
				print (j)
				print (k)
				



