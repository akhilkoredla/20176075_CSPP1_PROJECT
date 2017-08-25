import os

class Bag(object):

	def filein(self,l):
		a=""
		for i in l:	
			if 97<=ord(i)<=122 or 48<=ord(i)<=57 or ord(i)==95:
				a+=i
			else:
				a+=' '
		return a
	def splitfile(self,l1):
		d={}
		for i in l1:
			if i not in d:
				d[i]=1
			else:
				d[i]+=1
		return d
	def dotProductSum(self,d1,d2):
		sum=0
		for i in d1:
			for j in d2:
				if i==j:
					dot=d1[i]*d2[j]
					sum+=dot
		return sum
	def freqsquare(self,k):
		z1=k.values()
		sum=0
		for i in z1:
			sum=sum+(i*i)
		s=sum**(0.5)
		return s

	def bagofwords(self,s1,s2):
		z1=b.filein(s1).split()
		z2=b.filein(s2).split()
		d1=b.splitfile(z1)
		d2=b.splitfile(z2)
		dotsum=b.dotProductSum(d1,d2)
		f1=b.freqsquare(d1)
		f2=b.reqsquare(d2)
		similarity=((dotsum)/(f1*f2))*100
		return similarity

b=Bag()

path="C:/Users/Akhil/Desktop/20176075_CSPP1_PROJECT/bagofwords/bag"
list=os.listdir(path)
os.chdir(path)
l=['     ']
for i in range(len(list)):
	l.append(list[i])
print l
for i in range(len(list)):
	l1=[]
	for j in range(0,len(list)):		
		if i==j:
			l1.append(0.0)
		else:
			file1=open(list[i],"r").read().lower()
			file2=open(list[j],"r").read().lower()
			l2=b.bagofwords(file1,file2)
			l1.append(l2)
	print list[i],l1		