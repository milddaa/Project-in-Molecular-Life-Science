data = np.genfromtxt('Proteins/d1a04a2.c.23.1.1.fasta.pssm', skip_header=3, skip_footer=5, usecols=range(22,42), autostrip=True)/100
data=data.tolist()
data=list(chain(*data))
add_tails=[0]*(20*int(window_size/2))
data = add_tails + data + add_tails
Y_list=[]
for y in range (0,len(data)-(window_size*20),20):
    print (data[y:y+(20*window_size)])

