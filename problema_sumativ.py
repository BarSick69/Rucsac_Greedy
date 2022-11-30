"""Moș Crăciun pregătește cadourile pentru acest an. El cunoaște prețurile a n 
cadouri și are la dispoziție o sumă de bani S. Ajutați-l să aleagă un număr maxim de cadouri a căror preț total
 să nu depășească S și determinați suma minimă de care mai are nevoie Moș Crăciun pentru a cumpăra încă un cadou."""
from random import randint
from random import seed
seed(5)
n=randint(1,5)
s=randint(1,5)
preturile_cadourilor=[]
st=0
nr_de_cadouri=0
trebuie_sa_mai_dea=0
index_to_delete=0
for i in range(n):
    preturile_cadourilor.append(randint(1,10))
preturile_cadourilor_temp=preturile_cadourilor.copy()
print("suma disponibila:",s)
print("numarul de cadouri:",n)

preturile_cadourilor_temp=sorted(preturile_cadourilor_temp)
print(preturile_cadourilor_temp)
i=0
while(st<s and i<len(preturile_cadourilor_temp)):
    if((s-st)-preturile_cadourilor_temp[i]>=0):
        nr_de_cadouri+=1
        st+=preturile_cadourilor_temp[i]
        i+=1
    else:
        print(f"poate cumpara {nr_de_cadouri} cadouri,si pentru a lua urmatorul cadou ii trebuie {preturile_cadourilor_temp[i]-(s-st)} lei")
        break
if(i>=len(preturile_cadourilor_temp)):
    print(f"Poate cumpara toate cadourile {nr_de_cadouri}")






