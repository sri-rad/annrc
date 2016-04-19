import numpy as np
import matplotlib.pyplot as plt

def voltageC(vin, R, C, f):
	if(f==0): return vin
	w=np.pi*2*f
	xc=1/(C*w)
	mul=xc/np.sqrt(R*R+xc*xc)
	return vin*mul

def phaseC(R,C,w):
	return np.arctan(-1*R*w*C)

fwrite=open('samplelowpass.csv','w')


fs=list(np.linspace(0,10000, 50))
vin=10
R=4700
C=0.000000047

for f in fs:
	k=voltageC(vin, R,C,f)
	print k
	fwrite.write(str(f/10000)+','+str(k/10)+',\n')

fwrite.close()



