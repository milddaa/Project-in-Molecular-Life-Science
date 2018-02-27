my_dict={'ID1':['ACDEF','EBBEB'],
        'ID2':['QRAEF','BBEBE']}
        
"Dictionary of amino acid encodings. An artificial amino acid is also encoded which is called B."

amino_acids={'B':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
'A':[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
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
        "Adding tails to the sequence based on window size in order to capture all the elements when window size is bigger than 1."
        add_tails="B"*int(wind_sz/2)
        seq=add_tails+seq+add_tails
        print (seq)
        lab=x[1]
        "This part of function will create list X, which contains the encoded amino acids."
        "-First it will create a list of windows in the sequence based on the window size."
        for x in range (len(seq)):
            window=seq[x:x+wind_sz]
            if len(window)==wind_sz:
                window_list1.append(window)
        print (window_list1)
        "-Then it will create a list with nested lists with encoded amino acids for each window."
        X_list=[]
        for x in window_list1:
            new_list=[]
            for y in x:
                new_list.extend(amino_acids[y])
            X_list.append(new_list)
        "This part of function will create a list Y, which contains all the labels"
        Y_list=[]
        for x in lab:
            Y_list.append(dictA[x])
        "As a final step, the function will append the two lists to the major one."
        X_list_all.extend(X_list)
        Y_list_all.extend(Y_list)
    return (X_list_all, Y_list_all)
    
print (two_lists_iteration(my_dict,3))