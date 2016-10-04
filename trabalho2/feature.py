import numpy as np

#leitura de arquivo
def readFile(file):
  data =[]
  lines = file.split("\n")

  for lines in lines[1:]:
    aux = lines.split(";")
    del aux[0]
    data.append(aux)
  return data

def sum(_list):
  res = 0.0
  for l in _list:
    res += float(l[0])
  return res

file = open('dados/amostra_tempo.csv','r')
file = file.read()
sample = readFile(file)
del sample[len(sample)-1]

file = open('dados/populacao_tempo.csv','r')
file = file.read()
pop = readFile(file)
del pop[len(pop)-1]
pop = np.array(pop).astype(np.float)
stdPop = np.std(pop,dtype=np.float64)

print("Desvio padrao: "+str(stdPop))

err = stdPop/np.sqrt(len(pop))

print("Erro padrao: "+ str(err))

sum_sample = sum(sample)
meanSample = sum_sample/float(len(sample))
sum_pop = sum(pop)
meanPop = sum_pop/float(len(pop))

lowLimit = meanPop-1.96*err
highLimit = meanPop+1.96*err

print("Media de tempo da amostra: "+str(meanSample))
print("Media de tempo da populacao: "+str(meanPop))
print("Low Limit"+str(lowLimit))
print("High Limit"+str(highLimit))