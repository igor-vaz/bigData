from scipy.stats import chi2_contingency as chi2
import csv

X = []
Y = []

def count(file):
    count_yes = 0
    count_no = 0
    csvfile = open(file, 'rb') 
    reader = csv.reader(csvfile, delimiter=';')
    next(reader,None) # Pula a primeira linha
    for row in reader:
  if( row[1] == 'yes' ):
      count_yes += 1
  else:
      count_no += 1

A_yes,A_no = count("amostra_A_click.csv")
B_yes,B_no = count("amostra_B_click.csv")

M = [[A_yes,A_no],[B_yes,B_no]]

res = chi2(M)
print(res)