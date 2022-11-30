"""
Pentru cadourile pe care Moş Crăciun urmează să le cumpere copiilor cuminţi, Consiliul Polului Nord a alocat suma de S eureni. 
Ştiind că în comerţul polar se utilizează banctnote de 1,5,10,25,75,100,125,150,300,500,750,1000,2000 eureni 
să se determine numărul de bancnote din fiecare tip necesare pentru a forma suma S,si numarul total de bancnote.
"""
from random import randint,seed
seed(12)
s=randint(10,5000)
st=0
nr_de_bancnote=0
tipuri=[[1,0],[5,0],[10,0],[25,0],[75,0],[100,0],[125,0],[150,0],[300,0],[500,0],[750,0],[1000,0],[2000,0]]
while(st<s):
    for i in range(len(tipuri)-1,-1,-1):
        if(st+tipuri[i][0]<=s):
            st+=tipuri[i][0]
            tipuri[i][1]+=1
            nr_de_bancnote+=1
print(st)
print("vor fi utilizate in total:",nr_de_bancnote,"bancnote")
print("Lista fiecarui tip de bancnote si numarul acestora:")
print(tipuri)