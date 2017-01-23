def collatz(num,l):
	if num == 1:
		l.append(num)
	else:
		if num%2 == 0:
			l.append(num)
			collatz(num/2,l)
		else:
			l.append(num)
			collatz((3*num)+1,l)

nums = []
for i in xrange(1,1000001):
	n = []
	collatz(i,n)
	nums.append(n)

maxlen = 0
num = 0
for l in nums:
	if len(l) > maxlen:
		maxlen = len(l)
		num = l[0]

print (num)


