import sklearn
from sklearn import svm

"Turn your dataset into a dictionary where keys are the IDs and values are lists with first member being the aminoacid list and the second - the classification for each residue into one of the two states (exposed or burried)."

f = open('testdataset.txt','r')
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
my_dict={x:y for x in key_list for y in value_list}
print (my_dict)

