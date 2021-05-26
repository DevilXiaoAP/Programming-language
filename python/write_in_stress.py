#!/user/bin/python
# -* - coding:UTF-8 -*-
from odbAccess import *
import csv
from odbMaterial import *
from odbSection import *
from abaqusConstants import *
odb = openOdb(path='G:\Temp\Job-model-100_360-press-empty.odb')
fixSet = odb.rootAssembly.instances['PLATE-1']
step1 = odb.steps.values()[0]
sField = odb.steps.values()[-1].frames[-1].FieldOutput(name='S',
    description='Stress', type=TENSOR_3D_FULL,
    componentLabels=('S11', 'S22', 'S33',
    'S12','S13','S23'), validInvariants=(MISES,))

#generate an element set
list1 = range(1,21601,1)
tuple1 = tuple(list1)
elementLabelData = tuple1

#create a stress set
rows1 = open('integration_point.csv','r').readlines()
lines1 = [x.rstrip() for x in rows1]
lines1[0] = '-1.520E-01,4.470E-04,2.540E+02,-2.760E-04,1.140E-04,-4.930E-07'
data1 = []
[data1.append(eval(i)) for i in lines1]
stressData = tuple(data1)

#adddata to odb file
sField.addData(position=INTEGRATION_POINT, instance=fixSet,labels=elementLabelData,data=stressData)   
step1.setDefaultField(sField)

#save and close odb
odb.save()
odb.close()
