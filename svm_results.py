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




len34=0
notlen34=0
for i in range(0,len(data_bump)):
	if len(data_bump[i][0])==34:
		len34=len34+1
	else:
		notlen34=notlen34+1



print("len34= ", len34)
print("notlen34 = ", notlen34)




len34=0
notlen34=0
for i in range(0,len(data_notbump)):
	if len(data_notbump[i][0])==34:
		len34=len34+1
	else:
		notlen34=notlen34+1



print("len34= ", len34)
print("notlen34 = ", notlen34)





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



from sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30, random_state=0)

from sklearn import preprocessing
#X_train_normalized = preprocessing.normalize(X_train,norm='l1')
#X_test_normalized = preprocessing.normalize(X_test,norm='l1')

#X_train= preprocessing.scale(X_train)
#X_test= preprocessing.scale(X_test)
#X_train,y_train= shuffle(X_train,y_train) #shuffle the data
#X_test,y_test= shuffle(X_test,y_test) #shuffle the data



from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.model_selection import cross_val_score

from sklearn.calibration import CalibratedClassifierCV

#model = SVC(kernel='linear', C=1, probability=True)
model = LinearSVC()
model = CalibratedClassifierCV(model) 

model.fit(X, y)


#pred_class = model.predict(X_test)
#probability = model.predict_proba(X_test)

print("svm training finished   RNA+old  data-4")

#open all_dis_arrays.txt
file1 = open("/DATA/Cem_Internship/all_dis_arrays.txt", 'r') 
file2= open("/DATA/Cem_Internship/results/svm_probs_RNA+olddata_network4.txt", "w+")

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
		
	prob= model.predict_proba(y)
		
		
		
	file2.writelines(str(line[0])) # add name of transcript
	file2.writelines(" ")
	file2.writelines(str(line[1])) #add index
	file2.writelines(" ")

	file2.writelines(str(prob)) #add probability
	file2.writelines("\n")




	    	  
file1.close()
file2.close()




'''
print("pred_class = ",pred_class)
print("probability = ",probability)
sifir=0; bir=0
for i in range(0, len(pred_class)):
	if pred_class[i]==0:
		sifir=sifir+1
	else:
		bir=bir+1

print("bir= ",bir)
print("sifir=", sifir)

from sklearn.metrics import classification_report, confusion_matrix,accuracy_score

print("------------")
print( accuracy_score(y_test,pred_class))
print("------------")

dogri=0
yanlis=0
for i in range(0, len(probability)):
	if(probability[i][0]> probability[i][1]):
		if pred_class[i]==0:
			dogri=dogri+1
		else:
			yanlis=yanlis+1
	else:
		if pred_class[i]==1:
			dogri=dogri+1
		else:
			yanlis=yanlis+1

print(len(probability))
print("dogri = ",dogri)
print("yanlis = ",yanlis)
print((dogri)*1.0 / len(probability))

#clf = SVC(kernel='linear', C=1)
#scores = cross_val_score(clf, X_normalized, y, cv=5) #5-fold cross-validation
#print(scores)
#clf.probability=True
#clf.fit(X, y)

'''













'''
y_pred=clf.predict(X_test)
y_dec = clf.decision_function(X_test)
y_prob = clf.predict_proba(X_test)
print("y_pred = ", y_pred)
print("y_dec = ", y_dec)
print("y_prob = ", y_prob)
print("\n")

p = np.array(clf.decision_function(X)) # decision is a voting function
print("p = ",p)
prob = np.exp(p)/np.sum(np.exp(p),axis=1)


print("\n")
'''



