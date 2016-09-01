#NSTEP SPOJ
ncasos=input()
int(ncasos)
variable=ncasos
listax=[]
listay=[]
for casos in range(variable):
	x=int(raw_input("introduce la coordenada X ")) 
	y=int(raw_input("introduce la coordenada Y "))
	listax.append(x)
	listay.append(y)
for n in range(variable):
	xs=listax[n]
	ys=listay[n]
	dx=xs%2
	dy=ys%2
	if xs < ys or dx != dy or xs >10000 or ys>10000:
		print "No Number"
	elif dx == 0 and dy == 0:
		if xs - ys == 2 or xs - ys == 0:
			print xs + ys
		else:
			print "No Number"
	elif dx == 1 and dy ==1:
		if xs - ys == 2 or xs - ys == 0:
			print xs + ys - 1
		else:
			print "No Number"


ncasos=input()
int(ncasos)
variable=ncasos
listax=[]
listay=[]
for casos in range(variable):
	x=int(raw_input("introduce la coordenada X ")) 
	y=int(raw_input("introduce la coordenada Y "))
	dx=x%2
	dy=y%2
	if x < y or dx != dy or x >10000 or y>10000:
		print "No Number"
	elif dx == 0 and dy == 0:
		if x - y == 2 or x - y == 0:
			print x + y
		else:
			print "No Number"
	elif dx == 1 and dy ==1:
		if x - y == 2 or x - y == 0:
			print x + y - 1
		else:
			print "No Number"

