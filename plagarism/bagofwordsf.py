def filein(s1,a):
	for i in s1:	
		if ord(i)>=48 and ord(i)<=57:
			a=a+i
		elif ord(i)>=97 and ord(i)<=122:
			a=a+i
		else:
			a=a+' '
	return a
file1=open("msd.txt")
s1=file1.read()
s1=s1.lower()
a=""
file2=open("msdvks.txt")
s2=file2.read()
s2=s2.lower()
z1=filein(s1,a)
z2=filein(s2,a)

def splitfile(l1):
	d={}
	for i in l1:
		if i not in d:
			d[i]=1
		else:
			d[i]+=1
	return d
l1=z1.split(" ")
l2=z2.split(" ")
d1=splitfile(l1)
d2=splitfile(l2)
# import collections
# d2=collections.Counter(l2)
# print d2 
def dotProductSum(d1,d2):
	sum=0
	for i in d1:
		for j in d2:
			if i==j:
				dot=d1[i]*d2[j]
				sum+=dot
	return sum
dotsum=dotProductSum(d1,d2)

def freqsquare(k):
	z1=k.values()
	sum=0
	for i in z1:
		sum=sum+(i*i)
	s=sum**(0.5)
	return s
f1=freqsquare(d1)
f2=freqsquare(d2)

similarity=((dotsum)/(f1*f2))*100
print "Similarity between two given files is ",similarity,"%"
file1.close()
file2.close()
