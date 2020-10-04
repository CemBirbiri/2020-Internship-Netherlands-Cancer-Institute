import numpy as np

def str_to_list(string):
	#print(string)
	#string= string[1:-1]
	listt= string.split(", ")
	
	listt2=[]
	for i in range(0,len(listt)):
		#print(listt[i])
		#listt2.append(float(listt[i][1:-1]))
		listt2.append(float(listt[i]))
	return listt2


def get_data_bumps(filename1, data_with_labels):

	file1 = open(filename1, 'r') 
	while True: 
	    line = file1.readline() 
	    if not line: 
	        break

	    line = line.strip()
	    line1 = line.split("*")
	    
	    for i in range(1, len(line1)):
	    	temp=[]
	    	tmp_line = line1[i][1:-1]
	    	if len(tmp_line) >2:

		    	tmp_line = str_to_list(tmp_line)
		    	temp.append(tmp_line)
		    	temp.append(1)
		    	data_with_labels.append(temp)
	  
	file1.close()

	return data_with_labels


def get_data_not_bumps(filename1,data):

	#data=[]
	file1 = open(filename1, 'r') 
	while True: 
	    line = file1.readline() 
	    if not line: 
	        break

	    temp=[]
	    line = line.strip()
	    line=line[1:-1]
	    line1= line.split(", ")
	    array=[]
	    for i in range(0,len(line1)):
	    	
	    	if(line1[i]!=""):
	    		array.append(float(line1[i]))
	    temp.append(array)
	    temp.append(0) #because not bump class label is 0
	    data.append(temp)

	    
	  
	file1.close()

	return data



import sklearn
print(sklearn.__version__)



bumps_path="/DATA/Cem_Internship/RNAproject/RNA_disorderedness_arrays_bumps4.txt"
bumps_path2="/DATA/Cem_Internship/disorderedness_arrays_bumps4.txt"  

data_bump=[]
data_bump = get_data_bumps(bumps_path, data_bump)
data_bump = get_data_bumps(bumps_path2, data_bump)
print(" LEN- BUMPS == ", len(data_bump))

#######################################################################

not_bumps_path="/DATA/Cem_Internship/RNAproject/RNA_disorderedness_arrays_not_bumps4.txt"
not_bumps_path2="/DATA/Cem_Internship/disorderedness_arrays_not_bumps4.txt"
data_notbump=[]
data_notbump = get_data_not_bumps(not_bumps_path,data_notbump) 
data_notbump = get_data_not_bumps(not_bumps_path2,data_notbump) 

print("data_notbump[0]=",data_notbump[0])

print(" LEN- NOT_BUMPS == ", len(data_notbump))

data_with_labels= data_bump+ data_notbump


print("\n")
print(data_with_labels[0])
print("len (data_with_labels)", len(data_with_labels))

X=[] #disorderedness arrays
y=[] #corresponding class labels

for i in range(0,len(data_with_labels)):

	X.append(data_with_labels[i][0])
	y.append(data_with_labels[i][1])


X= np.array(X)
y= np.array(y)

from sklearn.utils import shuffle
X,y= shuffle(X,y) #shuffle the data

from sklearn import preprocessing
X = preprocessing.normalize(X,norm='l2') #normalize the data


from sklearn.model_selection import train_test_split
# Split dataset into training set and test set
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


#Import Random Forest Model
from sklearn.ensemble import RandomForestClassifier
#Create a Gaussian Classifier
clf=RandomForestClassifier(n_estimators=100)
#Train the model using the training sets y_pred=clf.predict(X_test)
#clf.fit(X_train,y_train)
#y_pred=clf.predict(X_test)
clf.fit(X,y)



print("randomForest training finished-RNA+old_data-4")
#open all_dis_arrays.txt
file1 = open("/DATA/Cem_Internship/all_dis_arrays.txt", 'r') 
file2= open("/DATA/Cem_Internship/results/RandomForest_probs_RNA+olddata_network4.txt", "w+")

while True: 
	# Get next line from file 
	line = file1.readline() 
	  
	# if line is empty 
	# end of file is reached 
	if not line: 
	    break
	    
	    
	line = line.strip()
	line = line.split("*")
	
		
		
	x=str_to_list(line[2][1:-1])
	y=[]
	y.append(x)
		
	prob= clf.predict_proba(y)
		
		
		
	file2.writelines(str(line[0])) # add name of transcript
	file2.writelines(" ")
	file2.writelines(str(line[1])) #add index
	file2.writelines(" ")

	file2.writelines(str(prob)) #add probability
	file2.writelines("\n")




	    	  
file1.close()
file2.close()

















'''
X_test=[[0.0607, 0.0587, 0.0387, 0.0395, 0.0587, 0.1041, 0.1041, 0.1602, 0.2333, 0.1635, 0.1732, 0.1205, 0.0909, 0.0607, 0.0621, 0.0701, 0.1205, 0.1416, 0.1117, 0.1805, 0.2385, 0.1844, 0.2041, 0.282, 0.3668, 0.3359, 0.3456, 0.363, 0.282, 0.2865, 0.3491, 0.3885, 0.3806, 0.442]]
#0
X_test2=[[0.0425, 0.0252, 0.0405, 0.02, 0.0327, 0.0252, 0.0226, 0.0387, 0.0677, 0.0677, 0.0621, 0.0567, 0.0621, 0.0363, 0.0336, 0.016, 0.0144, 0.0097, 0.009, 0.0194, 0.0179, 0.0124, 0.0218, 0.0212, 0.0212, 0.0268, 0.0327, 0.0245, 0.0245, 0.0124, 0.0124, 0.0078, 0.0157, 0.0286]]
#1



y_pred1=clf.predict(X_test)
print("y_pred1 = ",y_pred1)
y_prob1= clf.predict_proba(X_test)
print("y_prob1 =", y_prob1)
print("\n")

y_pred2=clf.predict(X_test2)
print("y_pred2 = ",y_pred2)
y_prob2= clf.predict_proba(X_test2)
print("y_prob2 =", y_prob2)

#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
# Model Accuracy, how often is the classifier correct?
#print("Accuracy:",metrics.accuracy_score(y_test, y_pred1))

'''

