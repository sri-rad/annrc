from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import TanhLayer
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

ds=SupervisedDataSet(4,1)
f=open('/home/rsrihari/Documents/softcomp/sample2.csv')
lines=f.readlines()
for line in lines:
	line=line.split(',')
	ds.addSample(line[:4],line[-3:-2])
len(ds)

net=buildNetwork(4,3,1,bias=True,hiddenclass=TanhLayer)
trainer=BackpropTrainer(net, ds)
iters=50
for it in range(iters):
	print it
	trainer.train()

for line in lines:
	line=line.split(',')
	print net.activate(line[:4]), line[-3:-2]



