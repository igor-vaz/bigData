from scipy.stats import spearmanr
from sys import path
path.append('staticsCodes/')
import chisquared
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

sum_sample = sum(sample)
sum_pop = sum(pop)

print("Media de tempo da amostra: "+str(sum_sample/float(len(sample))))
print("Media de tempo da populacao: "+str(sum_pop/float(len(pop))))

# resSample = spearmanr(sample)
# resPop = spearmanr(pop)
# print(res)

c = chisquared.chi(len(sample), 0.05, sample)
c.run()

c2 = chisquared.chi(len(pop), 0.05, pop)
c2.run()