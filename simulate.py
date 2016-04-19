import numpy as np
import matplotlib.pyplot as plt

def voltageC(vin, R, C, w):
	deno=np.sqrt(1+(R*C*w)*(R*C*w))
	return vin/deno

def phaseC(R,C,w):
	return np.arctan(-1*R*w*C)

outs=[]

f=open('sample2.csv','w')
ws=list(np.linspace(0,1000, 5))
vins=list(np.linspace(0, 1000, 5))
Rs=list(np.linspace(0, 1000, 5))
Cs=list(np.linspace(0, 0.001, 5))

maxr=0
min=100000

for vin in vins:
	for R in Rs:
		for C in Cs:
			for w in ws:
				k=voltageC(vin, R,C,w)
				print k
				if(k>maxr): maxr=k
				f.write(str(vin/1000)+','+str(R/1000)+','+str(C*1000)+','+str(w/1000)+','+str(k/1000)+','+str(phaseC(R, C, w))+',\n')

f.close()



