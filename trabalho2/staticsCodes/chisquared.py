import numpy as np
from scipy.stats import poisson, chi2

N = 150
alpha = 0.05

data = np.random.poisson(3, N) #gerando os dados
bins = np.histogram(data, np.arange(0,6)) #separando em intervalos
bins_prob = list(poisson.pmf(range(0,4), 3)) #verificando a probabilidade em cada intervalo

bins_prob.append(1 - np.sum(bins_prob)) #ultimo intervalo acumula para valores maiores
bins_prob = np.array(bins_prob) #juntando o ultimo intervalo

print bins_prob*N #valores espeardos : todos deveriam ser maiores que 5
print bins[0] #valores obtidos

exp = bins_prob*N
obs = bins[0]

stat_test = sum([((obs[i] - exp[i])**2)/exp[i] for i in xrange(len(exp))])
print stat_test

pvalue = 1 - chi2.cdf(stat_test, len(exp)) #1 - acumulada ate o ponto x2
print "p-value: ", pvalue

if pvalue > alpha:
	print "Nao Rejeita H0"
else:
	print "Rejeita H0"