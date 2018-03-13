from sklearn import svm
import pickle

############ DEFINITIONS AND DICTIONARIES ###########

name_training= "../Datasets/training_dataset.txt"

window_size=19

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

################### STAGE 1. PARSER ##################

f = open(name_training,'r')
lines = f.readlines()
key_list=[]
value_list=[]
for x in lines:
    if x[0] == ">":
        key_list.append(x.strip())
    else:
        value_list.append(x.strip())
value_list=[value_list[i:i+2] for i in range (0, len(value_list),2)]
f.close()
my_dict={x:y for x, y in zip(key_list,value_list)}

############## STAGE 2. SVM INPUT MAKER #############

def SVM_input(input_dictionary, window_size):
    X_list_all=[]
    Y_list_all=[]
    for x in input_dictionary.values():
        window_list=[]
        seq=x[0]
        add_tails="B"*int(window_size/2)
        seq=add_tails+seq+add_tails
        lab=x[1]
        for x in range (len(seq)):
            window=seq[x:x+window_size]
            if len(window)==window_size:
                window_list.append(window)
        X_list=[]
        for x in window_list:
            new_list=[]
            for y in x:
                new_list.extend(amino_acids[y])
            X_list.append(new_list)
        Y_list=[]
        for x in lab:
            Y_list.append(dictA[x])
        X_list_all.extend(X_list)
        Y_list_all.extend(Y_list)
    return (X_list_all, Y_list_all)
    
X_array, Y_array = SVM_input (my_dict, window_size)

############## STAGE 3. MODEL BUILDER #############

clf = svm.LinearSVC(C=0.3)
clf.fit(X_array, Y_array)

pickle.dump(clf, open ("Model.sav",'wb'))