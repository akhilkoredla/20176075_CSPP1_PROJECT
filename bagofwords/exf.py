import os
def filein(s1):
	a=""
	for i in s1:	
		if 97<=ord(i)<=122 or 48<=ord(i)<=57 or ord(i)==95:
			a+=i
		else:
			a+=' '
	return a

def splitfile(l1):
	d={}
	for i in l1:
		if i not in d:
			d[i]=1
		else:
			d[i]+=1
	return d

def dotProductSum(d1,d2):
	sum=0
	for i in d1:
		for j in d2:
			if i==j:
				dot=d1[i]*d2[j]
				sum+=dot
	return sum

def freqsquare(k):
	z1=k.values()
	sum=0
	for i in z1:
		sum=sum+(i*i)
	s=sum**(0.5)
	return s

def bagofwords(file1,file2):
	z1=filein(s1)
	z2=filein(s2)
	d1=splitfile(z1).split()
	d2=splitfile(z2).split()
	dotsum=dotProductSum(d1,d2)
	f1=freqsquare(d1)
	f2=freqsquare(d2)
	similarity=((dotsum)/(f1*f2))*100
	print "Similarity between two given files is ",similarity,"%"

path="C:\Users\Akhil\Desktop\20176075_CSPP1_PROJECT/akhil"
list=os.listdir(path)
os.chdir(path)

for i in range(len(list)):
	for j in range(i+1,len(list)):
		if i==j:
			pass
		else:
			file1=open(list[i],"r").read().lower()
			file2=open(list[j],"r").read().lower()
			bagofwords(file1,file2)












file1.close()
file2.close()
