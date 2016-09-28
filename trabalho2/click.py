import csv
import matplotlib.pyplot as plt
import numpy as np
import re

dataA =[]
dataB =[]

csvfile = open('dados/amostra_A_click.csv','r')
reader = csv.reader(csvfile,  delimiter=';')

for row in reader:
    print(row)