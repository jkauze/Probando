n1=int(raw_input())
n2=int(raw_input())
suma=0
while n1<n2-1:
	suma+=n1*n1
	n1+=1
suma+=(n2-1)*(n2-1)
suma+=n2*n2
print suma