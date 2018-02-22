filename="testdataset.txt"
wind_sz=1

"A function which converts the dataset text file into a dictionary where the keys are IDs and values are lists with the first item being the protein sequence and the second item being the label sequence."

def make_dict(filename):
    f = open(filename,'r')
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

