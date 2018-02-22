my_dict={'ID1':['ACD','EBB'],
        'ID2':['QRA','BBE']}

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

dictA={'E':0, 'B':1}

def two_lists_iteration(input_dict, wind_sz):
    X_list_all=[]
    Y_list_all=[]
    for x in input_dict.values():
        window_list1=[]
        window_list2=[]
        seq=x[0]
        lab=x[1]
        "This part of function will create list X, which contains the encoded amino acids."
        "-First it will create a list of windows in the sequence based on the window size."
        for x in range (0,len(seq)):
            window=seq[x:x+wind_sz]
            if len(window)==wind_sz:
                window_list1.append(window)
        "-Then it will create a list with nested lists with encoded amino acids for each window."
        X_list=[]
        for x in window_list1:
            new_list=[]
            for y in x:
                new_list.extend(amino_acids[y])
            X_list.append(new_list)
        "This part of function will create a list Y, which contains all the labels"
        "-First it will create a list of windows in the label sequence based on the window size."
        for x in range (0,len(lab)):
            window=lab[x:x+wind_sz]
            if len(window)==wind_sz:
                window_list2.append(window)
        "-Then it will create a list with labels for central residues in each window, encoded by binary number."
        Y_list=[]
        for x in window_list2:
            if wind_sz != 1:
                central_number=int(wind_sz/2)
                central_residue=x[central_number]
                Y_list.append(dictA[central_residue])
            else:
                Y_list.append(dictA[x])
        "As a final step, the function will append the two lists to the major one."
        X_list_all.extend(X_list)
        Y_list_all.extend(Y_list)
    return (X_list_all, Y_list_all)
    
print (two_lists_iteration(my_dict,3))
        