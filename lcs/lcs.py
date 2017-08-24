import os
print(list[0])

# f1="my name is "
# f2="name is "

l1=f1.split(" ")
len1=0
for i in l1:
	len1+=len(i)

l2=f2.split(" ")
len2=0
for j in l2:
	len2+=len(j)


c=0
for i in range(len(l1)):
	for j in range(len(l2)):
		l=[]
		while i<len(l1) and j<len(l2) and l1[i]==l2[j]:
			l.append(l1[i])
			i=i+1
			j=j+1
		if len(l)!=0:
			l="".join(l).strip()
			if len(l)>c:
				c=len(l)

print c,"is length of lcs"
z=c*200
similarity=(float(z)/(len1+len2))
print similarity,"% match found"

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
			l2=lsc(file1,file2)
			l1.append(l2)
	print list[i],l1		