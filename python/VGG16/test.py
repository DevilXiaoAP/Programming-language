

rows1 = open('F:\\Study\\code\\python\\integration_point.csv','r').readlines()
lines1 = [x.rstrip() for x in rows1]
# lines1 = [x.rstrip(',') for x in lines1]
lines1[0] = '-1.520E-01,4.470E-04,2.540E+02,-2.760E-04,1.140E-04,-4.930E-07'
# print(rows1)
# print(lines1)
data1 = []
[data1.append(eval(i)) for i in lines1]
stressData = tuple(data1)
print(stressData)