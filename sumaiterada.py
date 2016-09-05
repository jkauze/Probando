n=raw_input()
lista=n.split(" ")
n1=lista[0]
n2=lista[1]
n1=int(n1)
n2=int(n2)
suma=0
while n1<n2-1:
	suma+=n1*n1
	n1+=1
suma+=(n2-1)*(n2-1)
suma+=n2*n2
print suma
