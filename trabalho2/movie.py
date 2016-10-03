import csv
from scipy.stats import spearmanr

X =[]
Y =[]
count = 0
#leitura de arquivo
csvfile = open('dados/movie_metadata.csv','r')
reader = csv.reader(csvfile)

i=0
for row in reader:
  if i==0:
    pass
  else:
    if row[15]=='':
      count+=1
    else:
      Y.append(row[15]) #num_faces
      X.append(row[25]) #imdb_score
  i+=1

print count

res = spearmanr(X,Y)
print res 
#(-0.087125663312467294, 6.0391525040632296e-10)
# rho negativo e p-valor mto pequeno -> x aumenta, y diminui
# No caso nota aumenta com poucas faces