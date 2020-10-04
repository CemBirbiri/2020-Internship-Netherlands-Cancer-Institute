def get_whole_dis_arrays(disordered_filename):
	file1 = open(disordered_filename, 'r') 
	disordered=[]
	all_arrays=[]
	while True: 
	    # Get next line from file 
	    line = file1.readline() 	  
	    # if line is empty end of file is reached 
	    if not line: 
	        break
	    
	    line = line.strip()
	    line1 = line.split()
	    disordered.append(line1)

	    

	file1.close()
	for i in range(0, len(disordered)):
		for j in range(1, len(disordered[i])-34 , 5):
			temp=[]
			temp.append(disordered[i][0]) #add name
			temp.append([j-1,j+34-2])  #add index
			temp.append(disordered[i][j:j+34]) #add array
			all_arrays.append(temp)

			





	return all_arrays

def make_float(array):
	a=[]
	for i in range(0, len(array)):
		a.append(float(array[i]))
	return a

disordered_path= "/DATA/Cem_Internship/DISORDER_PROJECT/disorder_pg_mod.txt"
all_arrays = get_whole_dis_arrays(disordered_path)



file1= open("all_dis_arrays.txt", "w+")
for i in range(0, len(all_arrays)):
	file1.writelines(str(all_arrays[i][0]))
	file1.writelines("*")
	file1.writelines(str(all_arrays[i][1]))
	file1.writelines("*")

	float_list= make_float( all_arrays[i][2])

	file1.writelines(str(float_list))
	file1.writelines("\n")

file1.close()