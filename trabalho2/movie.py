import csv
import matplotlib.pyplot as plt
import numpy as np
import re

movies_num_faces = {}
score_num_faces = {}
keys=[]

#leitura de arquivo
csvfile = open('dados/movie_metadata.csv','r')
reader = csv.reader(csvfile)

i=0
for row in reader:
  if i==0:
    pass
  else:
    key = row[15]
    keys.append(row[15])
    if key in movies_num_faces.keys():
      movies_num_faces[key] += 1.0
    else:
      movies_num_faces[key] = 1.0

    if key in score_num_faces.keys():
      score_num_faces[key] += float(row[25])
    else:
      score_num_faces[key] = float(row[25])
  i+=1

for key in score_num_faces.keys():
  print("Media dos filmes com "+key+" faces: "+str(score_num_faces[key]/movies_num_faces[key]))