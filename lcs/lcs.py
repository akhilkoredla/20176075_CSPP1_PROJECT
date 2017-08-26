import os.path
class Lcs(object):
	def common_length(self,l1,l2):
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
		return c

	def lcs(self,file1,file2):
		l1=file1.split(" ")
		len1=0
		for i in l1:
			len1+=len(i)

		l2=file2.split(" ")
		len2=0
		for j in l2:
			len2+=len(j)

		a=lc.common_length(l1,l2)
		z=a*200
		similarity=(float(z)/(len1+len2))
		similarity=round(similarity,2)
		if file1==file2:
			similarity=0.0
		return str(similarity)
		


lc=Lcs()
path="C:/Users/Akhil/Desktop/20176075_CSPP1_PROJECT/lcs/lcstxt"
list=os.listdir(path)
os.chdir(path)
matrix=[]
submatrix=[]
submatrix.append('      ')
submatrix.extend(list)
matrix.append(submatrix)
for i in list:
	submatrix=[]
	submatrix.append(i)
	for j in list:
		file1=open(i,'r').read().lower()
		file2=open(j,'r').read().lower()
		x=lc.lcs(file1,file2)
		submatrix.append(x)
	matrix.append(submatrix)
for i in range(len(matrix)):
	if i==0:
		k='     '.join(matrix[i])
		print(k)
	else:
		k='        '.join(matrix[i])
		print(k)
