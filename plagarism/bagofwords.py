file1=open("msd.txt")
a=file1.read()

file2=open("msdvks.txt")
b=file2.read()


l1=a.split(" ")
d1={}
for i in l1:
	if i not in d1:
		d1[i]=1
	else:
		d1[i]+=1

l2=b.split(" ")
d2={}
for j in l2:
	if j not in d2:
		d2[j]=1
	else:
		d2[j]+=1
# import collections
# d2=collections.Counter(l2)
# print d2 

dotsum=0
for i in d1:
	for j in d2:
		if i==j:
			dot=d1[i]*d2[j]
			dotsum+=dot

import math
z1=d1.values()
sumz1=0
for val1 in z1:
	square=(val1*val1)
	sumz1+=square
f1=math.sqrt(sumz1)
# f1=float((sumz1)**(1/2))


z2=d2.values()
sumz2=0
for val2 in z2:
	sq=(val2*val2)
	sumz2+=sq
f2=math.sqrt(sumz2)
# f2=float((sumz2)**(1/2))


similarity=((dotsum)/(f1*f2))*100
print "Similarity between two given files is ",similarity,"%"

file1.close()
file2.close()
