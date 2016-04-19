from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import SigmoidLayer
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
import matplotlib.pyplot as plt
import numpy as np


ds=SupervisedDataSet(1,1)
f=open('/home/rsrihari/Documents/softcomp/samplelowpass.csv')
lines=f.readlines()
for line in lines:
	line=line.split(',')
	inn=float(line[0])
	out=float(line[1])
	ds.appendLinked([inn],[out])

net=buildNetwork(1,50,1,hiddenclass=SigmoidLayer)
print net
trainer=BackpropTrainer(net, ds)
#trainer.trainUntilConvergence()
iters=100
ypred=[]
yact=[]

for line in lines:
	line=line.split(',')
	inn=float(line[0])
	out=net.activate([inn])[0]
	print out, line[1]
	ypred.append(out)
	yact.append(float(line[1]))

plt.plot(ypred)
plt.plot(yact)
