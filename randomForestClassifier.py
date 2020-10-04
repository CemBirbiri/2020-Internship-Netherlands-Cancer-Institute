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


def get_data_not_bumps(filename1):

	data=[]
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



bumps_path="/DATA/Cem_Internship/RNAproject/RNA_disorderedness_arrays_bumps1.txt"  

data_bump=[]
data_bump = get_data_bumps(bumps_path, data_bump)
print(" LEN- BUMPS == ", len(data_bump))

#######################################################################

not_bumps_path="/DATA/Cem_Internship/RNAproject/RNA_disorderedness_arrays_not_bumps1.txt"
data_notbump=[]
data_notbump = get_data_not_bumps(not_bumps_path) 

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
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)




#Import Random Forest Model
from sklearn.ensemble import RandomForestClassifier
#Create a Gaussian Classifier
clf=RandomForestClassifier(n_estimators=100)
#Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)


#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
