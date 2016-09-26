import matplotlib.pyplot as plt
import numpy as np
import re

dataA =[]
dataB =[]
oneType = 0
twoTypes = 0

#leitura de arquivo
arqA = open('amostra_A_click.csv','r')
arqA = arqA.read()
linesA = arqA.split("\n")

arqB = open('amostra_B_click.csv','r')
arqB = arqB.read()
linesB = arqB.split("\n")

for lines in lines[1:]:
  dataA.append(linesA.split(","))
  dataB.append(linesB.split(","))

print(data[0])