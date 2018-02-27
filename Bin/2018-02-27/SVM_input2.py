"Define the window size and name of the file for training and name of the file for testing."

window=3
name_training= "traindataset.txt"
name_testing="testdataset.txt"


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


"Open the text file with sequences and features, which will be used for testing, and create a dictionary from it."

f2 = open(name_testing,'r')
lines2 = f2.readlines()
key_list2=[]
value_list2=[]
for x in lines2:
    if x[0] == ">":
        key_list2.append(x.strip())
    else:
        value_list2.append(x.strip())
value_list2=[value_list2[i:i+2] for i in range (0, len(value_list2),2)]
f2.close()
my_dict2={x:y for x, y in zip(key_list2,value_list2)}


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


"Call out the function for the training dictionary and define the first item as X_array and the second item as Y_array."    

SVM_input = two_lists_iteration(my_dict,window)
X_array=SVM_input[0]
Y_array=SVM_input[1]

"Train the SVM with the created arrays as inputs to create a model called clf."

from sklearn import svm
clf = svm.SVC()
clf.fit(X_array, Y_array)

"Call out the function for the testing dictionary and define the first item as X_array and the second item as Y_array."

SVM_input2 = two_lists_iteration(my_dict2,window)
X_array2=SVM_input2[0]
Y_array2=SVM_input2[1]

"Predict the feature and calculate the percentage of correctly predicted features."
import numpy as np
Y_array2=np.asarray(Y_array2)
predicted_array=clf.predict(X_array2)
count=0
for x in range (len(Y_array)):
    if Y_array[x]==predicted_array[0]:
        count+=1
correct_predictions=count/len(Y_array)*100
print (correct_predictions)