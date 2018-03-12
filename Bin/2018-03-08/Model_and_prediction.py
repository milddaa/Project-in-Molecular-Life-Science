"Define the window size and name of the file for training and name of the file for testing."

window=3
name_training= "buried_exposed_alpha+beta.3line.txt"
name_testing= "sequences.txt"

"Open the text file with sequences and features, which will be used for training, and create a dictionary from it."

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

"Amino acid and label dictionaries. Amino acid dictionary contains an artificial amino acid B, which is encoded by zeros."

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

"Function to create an SVM input from dictionary."

def two_lists_iteration(input_dict, wind_sz):
    X_list_all=[]
    Y_list_all=[]
    for x in input_dict.values():
        window_list=[]
        seq=x[0]
        "Adding tails of Bs to the sequence based on window size in order to capture the first and last residues of the sequence."
        add_tails="B"*int(wind_sz/2)
        seq=add_tails+seq+add_tails
        lab=x[1]
        "This part of function will create list X, which contains the encoded amino acids."
        "-First it will create a list of windows in the sequence based on the window size."
        for x in range (len(seq)):
            window=seq[x:x+wind_sz]
            if len(window)==wind_sz:
                window_list.append(window)
        "-Then it will create a list with nested lists with encoded amino acids for each window."
        X_list=[]
        for x in window_list:
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
    
"Call out the function for the training dictionary and define the first item (list of amino acid encodings) as X_array and the second item (list of label encodings) as Y_array."    

SVM_input = two_lists_iteration(my_dict,window)
X_array=SVM_input[0]
Y_array=SVM_input[1]

"Train the SVM with the created arrays as inputs to create a model called clf."

from sklearn import svm
clf = svm.SVC()
clf.fit(X_array, Y_array)

"Open the text file with sequences in FASTA format, which will be used for testing, and create a dictionary from it."

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

"Modified function to create an SVM input from a dataset without the features"

def two_lists_iteration_modified(input_dict, wind_sz):
    X_list_all=[]
    for seq in input_dict.values():
        window_list=[]
        "Adding tails of Bs to the sequence based on window size in order to capture the first and last residues of the sequence."
        add_tails="B"*int(wind_sz/2)
        seq=add_tails+seq+add_tails
        "This part of function will create list X, which contains the encoded amino acids."
        "-First it will create a list of windows in the sequence based on the window size."
        for x in range (len(seq)):
            window=seq[x:x+wind_sz]
            if len(window)==wind_sz:
                window_list.append(window)
        "-Then it will create a list with nested lists with encoded amino acids for each window."
        X_list=[]
        for x in window_list:
            new_list=[]
            for y in x:
                new_list.extend(amino_acids[y])
            X_list.append(new_list)
        "As a final step, the function will append the two lists to the major one."
        X_list_all.extend(X_list)
    return (X_list_all)

"Call out the modified function for the testing dictionary and define the returned item as X_array2"
    
X_array2=two_lists_iteration_modified(my_dict2,window)

"Predict the feature for X_array2 using the built model"

predicted_array=clf.predict(X_array2)

"Transform the predicted array into a long string of features for all the sequences"

def array_to_feature (array_name):
    feature=''
    for x in array_name:
        feature+=dictB[x]
    return feature

feature_string=array_to_feature (predicted_array)

"Create a list of accumulated lengths of the sequences in the test file"

def seq_length(dict_name):
    lengths=[0,]
    for x in dict_name.values():
        lengths.append(len(x)+sum(lengths))
    return lengths
    
lengths=seq_length(my_dict2)

"Slice the long feature string based on the length list and make a list out of it."

feature_list=[]
for x in range(len(lengths)-1):
    beginning=lengths[x]
    end=lengths[x+1]
    feature_list.append(feature_string[beginning:end])

"Print the IDs, sequences and predicted features"

for x in range (len(feature_list)):
    print (list(my_dict2.keys())[x]+ '\n' + list(my_dict2.values())[x] + '\n' + feature_list[x])
    

    

