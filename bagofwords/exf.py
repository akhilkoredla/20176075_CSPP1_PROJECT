import os
def filein(l):
	a=""
	for i in l:	
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

def bagofwords(s1,s2):
	z1=filein(s1).split()
	z2=filein(s2).split()
	d1=splitfile(z1)
	d2=splitfile(z2)
	dotsum=dotProductSum(d1,d2)
	f1=freqsquare(d1)
	f2=freqsquare(d2)
	similarity=((dotsum)/(f1*f2))*100
	print "Similarity between two given files"+" "+list[i]+" & "+list[j]+" is "+str(similarity)+"%"

path="C:/Users/Akhil/Desktop/20176075_CSPP1_PROJECT/bagofwords/bag"
list=os.listdir(path)
os.chdir(path)
for i in range(len(list)):
	for j in range(i+1,len(list)):
		if i!=j:
			file1=open(list[i],"r").read().lower()
			file2=open(list[j],"r").read().lower()
			bagofwords(file1,file2)