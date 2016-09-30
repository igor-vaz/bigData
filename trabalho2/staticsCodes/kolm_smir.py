import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def plot_normal_acc():
	# Create some test data
	dx = .01
	X  = np.arange(-2,2,dx)
	Y  = np.exp(-X**2)

	# Normalize the data to a proper PDF
	Y /= (dx*Y).sum()

	# Compute the CDF
	CY = np.cumsum(Y*dx)
	plt.plot(X,CY,'r--')

N = 100

taxa = 1.0/N

data = np.random.normal(0,1,N)
data = sorted(data)

acumulated = []
dn = []

for i in xrange(len(data)):
	acumulated.append((i + 1)*taxa)
	prob = stats.norm.cdf(data[i])
	dn.append(abs(prob - acumulated[i]))
	print prob,'\t', acumulated[i],'\t', dn[i]

estat = max(dn)*np.sqrt(N)
print "estatistica de teste: ", estat

if(estat > 1.36):
	print "Rejeita Hipotese Nula"
else:
	print "Nao Rejeita Hipotese Nula"

plt.step(data,acumulated)
plot_normal_acc()
plt.show()