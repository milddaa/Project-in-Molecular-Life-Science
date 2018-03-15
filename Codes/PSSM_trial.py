import numpy as np
from itertools import chain
window_size=5
data = np.genfromtxt('Proteins/d1l42__.d.2.1.3.fasta.pssm', skip_header=3, skip_footer=5, usecols=range(22,42), autostrip=True)/100
data=data.tolist()
data=list(chain(*data))
add_tails=[0]*(20*int(window_size/2))
data = add_tails + data + add_tails

X_list=[]
for x in range (0,len(data),20):
    window=data[x:x+window_size*20]
    if len(window)==window_size*20:
        X_list.append(window)

print (len(X_list))
print (len(add_tails))

