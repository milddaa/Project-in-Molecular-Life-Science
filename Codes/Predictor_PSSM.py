import pickle
from itertools import chain
import numpy as np

############ DEFINITIONS AND DICTIONARIES ###########

name_testing= "../Datasets/example_sequence.txt"

window_size=13

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

dictB={0:'E', 1:'B'}

################### STAGE 1. PARSER ##################

f2 = open(name_testing,'r')
lines2 = f2.readlines()
key_list2=[]
value_list2=[]
for x in lines2:
    if x[0] == ">":
        key_list2.append(x.strip())
    else:
        value_list2.append(x.strip())
f2.close()
my_dict2={x:y for x, y in zip(key_list2,value_list2)}

############## STAGE 2. SVM INPUT MAKER #############

def SVM_input(input_dictionary, window_size):
    X_list_all=[]
    for x in input_dictionary.keys():
        x=x.strip('>')
        data = np.genfromtxt('Proteins/PSSM_prediction/'+ x +'.txt.pssm', skip_header=3, skip_footer=5, usecols=range(22,42), autostrip=True)/100
        data=data.tolist()
        data=list(chain(*data))
        add_tails=[0]*(20*int(window_size/2))
        data = add_tails + data + add_tails
        X_list=[]
        for x in range (0,len(data),20):
            window=data[x:x+window_size*20]
            if len(window)==window_size*20:
                X_list.append(window)
        X_list_all.extend(X_list)
    return (X_list_all)
    
X_array = SVM_input (my_dict2, window_size)

############## STAGE 3. PREDICTOR #################

model=pickle.load(open("Model_PSSM.sav",'rb'))
predicted_array=model.predict(X_array)

############# STAGE 4. OUTPUT MAKER ################

def array_to_feature (array_name):
    feature=''
    for x in array_name:
        feature+=dictB[x]
    return feature

feature_string=array_to_feature (predicted_array)

def seq_length(dict_name):
    lengths=[0,]
    for x in dict_name.values():
        lengths.append(len(x)+sum(lengths))
    return lengths
    
lengths=seq_length(my_dict2)

feature_list=[]
for x in range(len(lengths)-1):
    beginning=lengths[x]
    end=lengths[x+1]
    feature_list.append(feature_string[beginning:end])
    
for x in range (len(feature_list)):
    print (list(my_dict2.keys())[x]+ '\n' + list(my_dict2.values())[x] + '\n' + feature_list[x])
