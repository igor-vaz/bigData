
file = open('args.csv','r')
data = []

for line in file:
    ll = line.split("\t")
    del ll[0]
    aux = []
    for l in ll:
        aux.append(l.split("\n")[0])
    # del aux[1]
    data.append(aux)

means=[]

for d in data:
    if len(d)!=10:
        pass
    else:
        means.append(float(d[-1]))

maxMean = max(means)
i = means.index(maxMean)
print i
print maxMean
print data[4][:9]