import csv

dataA =[]
dataB =[]

def readFile(file):
  read=[]
  csvfile = open(file,'r')
  reader = csv.reader(csvfile,  delimiter=';')

  for row in reader:
      read.append(row)

  return read

dataA = readFile('dados/amostra_A_click.csv')
dataB = readFile('dados/amostra_B_click.csv')
