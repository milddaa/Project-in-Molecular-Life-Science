"Given a protein sequence, return a list with amino acid encodings."

amino_acids={'A':[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
'C':[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
'D':[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
'E':[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
'F':[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
'G':[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
'H':[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
'I':[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
'K':[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
'L':[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
'M':[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
'N':[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
'P':[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
'Q':[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
'R':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
'S':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
'T':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
'V':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
'W':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
'Y':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]}

def encoding (seq):
    encoded_list=[]
    for x in seq:
        encoded_list.append(amino_acids[x])
    return encoded_list

print (encoding('AC'))
        
