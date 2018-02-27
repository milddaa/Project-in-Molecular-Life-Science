"Given a feature sequence, return a list with encodings."

dictA={'E':0, 'B':1}

def encoding (seq):
    encoded_list=[]
    for x in seq:
        encoded_list.append(dictA[x])
    return encoded_list

print (encoding('EBEB'))