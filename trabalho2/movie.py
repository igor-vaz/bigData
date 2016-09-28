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
# print(movies_num_faces)
# print(score_num_faces)

for key in score_num_faces.keys():
  print("Media dos filmes com "+key+" faces: "+str(score_num_faces[key]/movies_num_faces[key]))

# arq = open('movie_metadata.csv','r')
# arq = arq.read()
# lines = arq.split("\n")

# for lines in lines[1:]:
#   data.append(lines.split(","))

# print(data[0])