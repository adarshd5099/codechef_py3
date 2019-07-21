n = int( input() )
ans = []
for i in range (0,n):
	num  = int( input())
	d = 5
	s = 0
	if num <= 3:
			ans.append(0)
	else:		
		while(num // d >= 1 ):
			q = num // d
			s = s+q
			d = d * 5
		ans.append(s)
for s in ans:
	print( int(s) )
		
