import matplotlib.pyplot as plt
import numpy as np


#leitura de arquivo
def readFile(file):
  data =[]
  lines = file.split("\n")

  for lines in lines[1:]:
    data.append(lines.split(";"))
  return data

def sum(_list):
  res = 0.0
  for l in _list:
    res += float(l[1])
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


# print(len(sample))
# print(sample)
# print(len(pop))
# print(pop[-1])

