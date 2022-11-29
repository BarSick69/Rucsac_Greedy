from random import randint
import random
n=randint(1,20)#nrul obiectelor
v=randint(5,50)#volumul rucsacului
lista_obiectelor=[]
vt=0
suma=0
max=0
index_to_delete=0
l=n
for i in range(0,n):
    lista_obiectelor.append([randint(1,10),randint(1,1000)])#volumul,pretul
#trebuie sa verificam la care obiect raportul pret/volum este mai mare,acesta va fi cel mai logic de il pus in
#rucsac
for i in range(0,n):
    lista_obiectelor[i].append(round(lista_obiectelor[i][1]/lista_obiectelor[i][0],2))
temp_lista_obiectelor=lista_obiectelor.copy()
lista_obiectelor_introduse=[]
print("Volumul:",v)
print("Numarul de obiecte:",n)
print("lista[volum,pret,raport]:",lista_obiectelor)
while vt<=v:
    if(temp_lista_obiectelor==[]):
        break
    for i in range(0,l):
        raport=temp_lista_obiectelor[i][2]
        if raport>max:
            index_to_delete=i
            max=temp_lista_obiectelor[i][2]
    max=0
    vt+=temp_lista_obiectelor[index_to_delete][0]
    suma+=temp_lista_obiectelor[index_to_delete][1]
    lista_obiectelor_introduse.append(temp_lista_obiectelor[index_to_delete])
    temp_lista_obiectelor.pop(index_to_delete)
    l-=1
print("Volumul total:",vt)
print("Pretul total:",suma)
print("Au fost introduse urmatoarele obiecte:")

for obiect in lista_obiectelor_introduse:
    print(obiect)
if(vt>v):
    print("Desi ultimul obiect nu incape complet in rucsac,raportul pret/volum ne arata ca impartind acest obiect ca acesta sa incapa,oricum pretul va ieshi mai bun decat oricare alt obiect ramas!")





