lista=[]
lista2=[]
ncasos=int(raw_input())
numero=0
for i in range(ncasos):
    numero = int(raw_input())
    for z in range(1,numero):
        if numero%z==0:
            lista2.append(z)
    if numero%2==0:
        lista.append(lista2)
    lista2=[]    
for i in lista:
    var=0
    for z in i:
        var+=z
    print var
