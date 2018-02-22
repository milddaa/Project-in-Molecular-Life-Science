def labels(seq,wind_sz):
    dictA={'E':0, 'B':1}
    window_list=[]
    for x in range (0,len(seq)):
        window=seq[x:x+wind_sz]
        if len(window)==wind_sz:
            window_list.append(window)
    Y_list=[]
    print (window_list)
    for x in window_list:
        if wind_sz != 1:
            central_number=int(wind_sz/2)
            central_residue=x[central_number]
            Y_list.append(dictA[central_residue])
        else:
            Y_list.append(dictA[x])
    print (Y_list)

print(labels ('EBBEBEBEBEEEE',9))   
        
        