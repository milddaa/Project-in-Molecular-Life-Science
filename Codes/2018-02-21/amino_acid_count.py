"How many unique amino acids are there in the dataset?"

f = open('testdataset.txt','r')
lines = f.readlines()
sequences=lines[1::3]
amino_acid_list=[]
for x in sequences:
    for y in x:
        amino_acid_list.append(y)
print (set(amino_acid_list))
f.close()