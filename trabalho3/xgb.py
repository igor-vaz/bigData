import xgboost as xgb
import numpy as np

x_train =[]
y_train =[]

x_teste =[]
y_teste =[]

#leitura de arquivo
file = open('train_file.csv','r')
file = file.read()
lines = file.split("\n")

for line in lines[1:]:
	l = line.split(",")
	y_train.append(l[-1])
	del l[-1]
	x_train.append(l)

del y_train[-1]

del x_train[-1]

y_train = np.array(y_train, dtype='f')
x_train = np.array(x_train, dtype='f')

#x_teste, y_teste = read_file('teste_file.csv')

file = open('test_file.csv','r')
file = file.read()
lines = file.split("\n")

for line in lines[1:]:
	l = line.split(",")
	
	x_teste.append(l)

del x_teste[-1]


x_teste = np.array(x_teste, dtype='f')
# print x_teste[0]
# print x_train[0]
# exit(0)

dtrain = xgb.DMatrix( x_train, label=y_train)
param = {'bst:max_depth':2, 'bst:eta':1, 'silent':1, 'objective':'binary:logistic', 'nthread':4, 'eval_metric':'auc'}
evallist  = [(dtrain,'train')]
plst = param.items()
num_round = 10
bst = xgb.train( plst, dtrain, num_round, evallist )
dteste = xgb.DMatrix( x_teste)
y_pred = bst.predict(dteste, ntree_limit=bst.best_ntree_limit)
print y_pred

output = open('output.csv','w')
for elem in y_pred:
	output.write(str(elem))
	output.write("\n")