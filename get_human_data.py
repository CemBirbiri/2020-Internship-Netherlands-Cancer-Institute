import math
import random

def get_ids_and_transcripts(filename):
	file1 = open(filename, 'r') 
	ids=[]
	transcripts=[]

	while True: 
	    # Get next line from file 
	    line = file1.readline() 
	  
	    # if line is empty 
	    # end of file is reached 
	    if not line: 
	        break
	    
	    #print(line.strip())
	    line = line.strip()
	    
	    if line[0]==">":
	    	line= line[1:]
	    	id_list=line.split("|")
	    	ids.append(id_list[0])
	    else:
	    	transcripts.append(line)	
	  
	file1.close()

	whole_thing=[]
	len_lists=len(ids)

	for i in range(0,len_lists):
		temp=[]
		temp.append(ids[i])
		temp.append(transcripts[i])
		whole_thing.append(temp)

	return whole_thing



def get_bum_regions(filename):
	file1 = open(filename, 'r') 
	bump_regions=[]
	while True: 
	    # Get next line from file 
	    line = file1.readline() 
	  
	    # if line is empty 
	    # end of file is reached 
	    if not line: 
	        break
	    
	    line = line.strip()
	    line1 = line.split()

	    #print("line1 = ",line1)
	    if is_in(line1[0], bump_regions) == 1:
	    	for i in range(0, len(bump_regions)):
	    		if(line1[0] == bump_regions[i][0]):
		    		coords=[]
	    			coords.append(line1[1])
	    			coords.append(line1[2])
	    			bump_regions[i].append(coords)
	    			
	    else:
			coords=[]
			coords.append(line1[1])
			coords.append(line1[2])
			temp=[]
			temp.append(line1[0])
			temp.append(coords)
			bump_regions.append(temp)
			

	file1.close()
	return bump_regions

def get_transcript(bump_region, id_trans):
	transcript= id_trans[1]
	#print("len_trasn",len(transcript))
	left_number= int(bump_region[1])
	right_number = int(bump_region[2])
	#print("left , right",left_number,right_number)
	middle= transcript[left_number:right_number+1] 
	#print(len(middle))
	if( left_number == 50):
		left= transcript[0:left_number]
	elif left_number > 50: 
		left = transcript[left_number-50: left_number]
	else:
		return []

	if( len(transcript)- right_number ==50):
		right= transcript[right_number+1: len(transcript)+1]
	elif ( len(transcript)- right_number > 50):
		right = transcript[right_number+1: right_number+51]
	else:
		return []

	temp=[]
	temp.append(bump_region[0])
	temp.append(left+middle+right)

	return temp

def get_disordered_arrays_which_has_bumbs(bump_regions, disordered_filename):
	file1 = open(disordered_filename, 'r') 
	disordered=[]
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
	dis=[]
	for i in range(0,len(bump_regions)):
		for j in range(0, len(disordered)):
			if(bump_regions[i][0]==disordered[j][0]):
				dis.append(disordered[j])

	return dis

def get_transcript_lens(bump_regions,ids_transcripts):
	lens=[]
	for i in range(0, len(bump_regions)):
		for j in range(0, len(ids_transcripts)):
			if(bump_regions[i][0]==ids_transcripts[j][0]):
				
				lens.append(len(ids_transcripts[j][1]))
	return lens
def eliminate_bumps(bump_regions, transcript_lens):
	
	new_bump_regions=[]
	for i in range(0,len(bump_regions)):
		temp=[]
		temp.append(bump_regions[i][0])
		for j in range(1, len(bump_regions[i])):
			if int(bump_regions[i][j][0])>=50 and (transcript_lens[i]-int(bump_regions[i][j][1])>=50):
			#if int(bump_regions[i][j][0])>=50 :
				temp.append(bump_regions[i][j])
		new_bump_regions.append(temp)
	return new_bump_regions
				
def extend_bump_regions100(bump_regions):
	new_bump_regions=[]
	for i in range(0,len(bump_regions)):
		temp=[]
		temp.append(bump_regions[i][0]) #add name
		for j in range(1, len(bump_regions[i])):
			r=(100-(int(bump_regions[i][j][1])-int(bump_regions[i][j][0])))/2
			#r=(62-(int(bump_regions[i][j][1])-int(bump_regions[i][j][0])))/2
			left= int(bump_regions[i][j][0]) -r
			right =int(bump_regions[i][j][1])+r
			tmp=[]
			tmp.append(left)
			tmp.append(right)
			temp.append(tmp)

			
		new_bump_regions.append(temp)
	return new_bump_regions
def get_disordered_lens(disordered_arrays_bumpli):
	dis=[]
	for i in range(0,len(disordered_arrays_bumpli)):
		dis.append((len(disordered_arrays_bumpli[i])-1)*3)
	return dis

def is_in(entsxx, bump_regions):
	if(bump_regions==[]):
		return 0
	else:
		for i in range(0, len(bump_regions)):
			if(entsxx == bump_regions[i][0]):
				return 1
		return 0
def is_inn(listt, j):
	if(listt==[]):
		return 0
	else:
		for i in range(0, len(listt)):
			if(j == listt[i]):
				return 1
		return 0

def make_float(array):
	a=[]
	for i in range(0, len(array)):
		a.append(float(array[i]))
	return a

def non_overlapping_notbumps( l, lenn):
	
		for i in range(1,len(l)):
			#if l[i]-l[i-1]<34 or l[-1]+34 >= lenn:
			if l[i]-l[i-1]<34:
				return 0
		return 1

def find_nb(disorder_len, disordered_array,  num_bumps, bump_region):
	end= bump_region[-1][1]
	end= int(end/3.0)
	#disordered_array= disordered_array[end:]
	disordered_array= disordered_array[end:-17]
	not_bump_arrays=[]
	sinirlar=[]



	ii=0
	flag=1
	while flag==1 :
		l= [random.randint(0,len(disordered_array)-34) for i in range(0, num_bumps)]#choose # of bumps here
		l=sorted(l)
		if non_overlapping_notbumps(l, len(disordered_array)) ==1:

			flag=0
		ii=ii+1
		if ii==500:
			break


	for j in range(0, len(l)):
		not_bump_arrays.append( disordered_array[l[j]: l[j]+34])
		temp=[]
		#temp.append( (l[j] + end)*3)
		#temp.append( (l[j] + 34 +end)*3)
		temp.append( (l[j] + end))
		temp.append( (l[j] + 34 +end))
		sinirlar.append(temp)
		#sinirlar.append(end)


	return not_bump_arrays, sinirlar

	'''
	#threshold sectigimiz fonksiyon
	end= bump_region[-1][1]
	end= int(end/3.0)
	#disordered_array= disordered_array[end:]
	disordered_array= disordered_array[end:-17]
	not_bump_arrays=[]
	for j in range(0, len(disordered_array)-34+1):
		array= disordered_array[j:j+34]
		array= make_float(array)
		if max(array)/min(array) <= 2.2: #determine threshold here!!!!!!!
			not_bump_arrays.append(array)
	return not_bump_arrays
	'''


def find_not_bump_regions(bump_regions, disorder_len, disordered_arrays_bumpli):
		
	not_bump=[]
	number_of_bumps=[]
	for i in range(0, len(bump_regions)):
		number_of_bumps.append(len(bump_regions[i])-1)

	
	for i in range(0, len(bump_regions)):
		if len(bump_regions[i])>1:
			temp=[]
			temp.append(bump_regions[i][0]) #add name
			#temp.append(number_of_bumps[i]) #add number of bumps
			x, sinirlar= find_nb(disorder_len[i], disordered_arrays_bumpli[i][1:],number_of_bumps[i] , bump_regions[i])
			temp.append(sinirlar)
			temp.append(x )
			not_bump.append(temp)
	return not_bump

def check(array):
	array= make_float(array)
	if max(array)/min(array) < 3:
		return 0
	return 1

def get_dis_coordinates_bumps(disordered_arrays_bumpli,bump_regions100):
	dis_coords_bump=[]

	for i in range(0, len(bump_regions100)):
		temp=[]
		temp.append(bump_regions100[i][0])
		for j in range(1,len(bump_regions100[i])):
			left = int(math.floor(bump_regions100[i][j][0] / 3.0 ))
			right = int(math.ceil( bump_regions100[i][j][1] / 3.0 ))
			'''
			array = disordered_arrays_bumpli[i][left+1:right+1]
			if check(array)!=0:
				temp.append(array)
			'''
			temp.append( disordered_arrays_bumpli[i][left+1:right+1])
			
		dis_coords_bump.append(temp)

	return dis_coords_bump
def make_str(l):
	l1=[]
	for i in range(0,len(l)):
		l1.append(str(l[i]))

	return l1

ids_transcripts=[]
#ids_transcripts = get_ids_and_transcripts("/home/azh2/Desktop/gencode.txt")
#ids_transcripts = get_ids_and_transcripts("/DATA/Cem_Internship/gencode.v19.pc_transcripts.txt")

bump_regions=[]
bump_regions=get_bum_regions("/DATA/Cem_Internship/DISORDER_PROJECT/5951_W_minus_bumps_30each.bed")
#bump_regions=get_bum_regions("/home/azh2/Desktop/bumps.bed")

print("** len(bump_regions)=", len(bump_regions))


disordered_arrays_bumpli=[]
#disordered_filename= "/home/azh2/Desktop/disorder.txt"
disordered_filename= "/DATA/Cem_Internship/DISORDER_PROJECT/disorder_pg_mod.txt"
#disordered_filename= "/DATA/Cem_Internship/test_codon.txt"
disordered_arrays_bumpli = get_disordered_arrays_which_has_bumbs(bump_regions,disordered_filename)
print("dab->", disordered_arrays_bumpli[0])
print("len(dab) = ", len(disordered_arrays_bumpli))
print("\n")

#transcript_lens= get_transcript_lens(bump_regions,ids_transcripts)
disorder_len= get_disordered_lens(disordered_arrays_bumpli)

print("len(bump_regions) =",len(bump_regions))
print("len(disorder_len) =",len(disorder_len))


bump_regions = eliminate_bumps(bump_regions, disorder_len)

#save this
bump_regions100=[]
bump_regions100= extend_bump_regions100(bump_regions)
print("br100->", bump_regions100[0])
print("\n")


'''
file1= open("bump_regions.txt", "w+")
for i in range(0, len(bump_regions100)):
	for j in range(0, len(bump_regions100[i])):
		file1.writelines(str(bump_regions100[i][j]))
		file1.writelines(" ")
		
	file1.writelines("\n")

file1.close()



file1= open("disordered_arrays_bumpli.txt", "w+")
for i in range(0, len(disordered_arrays_bumpli)):
	
	file1.writelines(str(disordered_arrays_bumpli[i]))		
	file1.writelines("\n")

file1.close()

'''
file1= open("bump_regions_divided_by_3.txt", "w+")
for i in range(0, len(bump_regions100)):
	for j in range(1, len(bump_regions100[i])):
		file1.writelines(str(bump_regions100[i][0]))
		file1.writelines("   ")
		file1.writelines(str(int( bump_regions100[i][j][0] /3.0 )))
		file1.writelines("   ")
		file1.writelines(str(int( bump_regions100[i][j][1] / 3.0)) )
		file1.writelines("\n")


file1.close()

	
			
	





'''

#save this
#not_bumps_regions= find_not_bump_regions(bump_regions100, disorder_len)
not_bumps_regions= find_not_bump_regions(bump_regions100, disorder_len,disordered_arrays_bumpli)

print("nbr->", not_bumps_regions[0])

print("\n")

file1= open("not-bump_regions_divided_by_3.txt", "w+")
for i in range(0, len(not_bumps_regions)):
	for j in range(0, len(not_bumps_regions[i][1])):

		file1.writelines(str(not_bumps_regions[i][0])) #add name
		file1.writelines("   ")
		file1.writelines(str(not_bumps_regions[i][1][j][0]))
		file1.writelines("   ")
		file1.writelines(str(not_bumps_regions[i][1][j][1]))
		file1.writelines("\n")


file1.close()



error=0
for i in range(0, len(not_bumps_regions)):
	if not_bumps_regions[i][1] > len(not_bumps_regions[i][2]):
		error = error +1
print("error = ", error)
print("\n")

'''

#not_bumps_regions2=[] #get not_bumps equal to number of bumps
#for i in range(0, len(not_bumps_regions)):
	#temp=[]
	#temp.append(not_bumps_regions[i][0])
	#if not_bumps_regions[i][1]> len(not_bumps_regions[i][2]):
		#for j in range(0, len(not_bumps_regions[i][2])):
			#temp.append(not_bumps_regions[i][2][j])
	#else:
		#for j in range(0, not_bumps_regions[i][1]):
			#temp.append(not_bumps_regions[i][2][j])
	#not_bumps_regions2.append(temp)

#print("nbr2->", not_bumps_regions2[0])
#print("\n")	

'''

not_bumps_regions3=[] ##MAKE STRING
for i in range(0,len(not_bumps_regions)):
	temp=[]
	temp.append(not_bumps_regions[i][0]) #add name
	if not_bumps_regions[i][2] != []:
		for j in range(0,len(not_bumps_regions[i][2])):

			temp.append(make_str(not_bumps_regions[i][2][j]))
	not_bumps_regions3.append(temp)

#print("nbr3->", not_bumps_regions3[0])
#print("nbr3->", not_bumps_regions3[1])
#print("nbr3[2]->", not_bumps_regions3[2])
#print("nbr3->", not_bumps_regions3[3])
#print("\n")	

not_bumps_regions4=[]
for i in range(0,len(not_bumps_regions3)):
	if len(not_bumps_regions3[i])> 1:
		for j in range(1,len(not_bumps_regions3[i])):
			not_bumps_regions4.append(make_float(not_bumps_regions3[i][j]))
	

#print("nbr4 = ", not_bumps_regions4[0:2])


file1= open("disorderedness_arrays_not_bumps4.txt", "w+")
for i in range(0, len(not_bumps_regions4)):
	file1.writelines(str(not_bumps_regions4[i])	)
	file1.writelines("\n")

file1.close()

'''
'''
file1= open("disorderedness_arrays_not_bumps.txt", "w+")
for i in range(0, len(not_bumps_regions3)):
	for j in range(0, len(not_bumps_regions3[i])):
		file1.writelines(str(not_bumps_regions3[i][j]))
		if(j != len(not_bumps_regions3[i])-1):
			file1.writelines("*") #deliminator is *
		
	file1.writelines("\n")

file1.close()
'''




'''
#save this
diss_coords_bump=[]
diss_coords_bump=get_dis_coordinates_bumps(disordered_arrays_bumpli,bump_regions100)
print("diss_coords_bump->", diss_coords_bump[0])

dis_coords_bump=[]
for i in range(0, len(diss_coords_bump)):
	temp=[]
	temp.append(diss_coords_bump[i][0])
	for j in range(1, len(diss_coords_bump[i])):
		temp.append(make_float(diss_coords_bump[i][j]))
	dis_coords_bump.append(temp)


'''




'''

file1= open("disorderedness_arrays_bumps4.txt", "w+")
for i in range(0, len(dis_coords_bump)):
	for j in range(0, len(dis_coords_bump[i])):
		file1.writelines(str(dis_coords_bump[i][j]))
		if(j != len(dis_coords_bump[i])-1):
			file1.writelines("*") #deliminator is *
		
	file1.writelines("\n")

file1.close()
'''











'''
# Find the MAX disordered-level probability in the not_bump regions
def find_end(br):
	max=0
	for i in range(1, len(br)):
		if br[i][1]> max:
			max= br[i][1]
	return max

def find_max_in_nbs(bump_regions,disordered_arrays):
	maxs=[]
	
	for i in range(0, len(bump_regions)):
		#print("bump_regions[i][-1][1] = ",bump_regions[i][-1][1])
		if len(bump_regions[i]) != 1:
			end= find_end(bump_regions[i])
			
			end=end/3
			maxx=0.0
			for j in range( end, len(disordered_arrays[i])-17):
				if float(disordered_arrays[i][j])> maxx:
					maxx= disordered_arrays[i][j]
			maxs.append(maxx)
	return maxs


maxs= find_max_in_nbs(bump_regions100,disordered_arrays_bumpli)
print(maxs)
print("-----")
print(max(maxs))
'''
