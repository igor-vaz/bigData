import xgboost as xgb
import numpy as np
from pyswarm import pso
from sklearn.cross_validation import KFold
from sklearn.metrics import roc_auc_score

x_train =[]
y_train =[]

x_teste =[]
y_teste =[]

arg_file = open('args.csv','w')

def objective_function(args):
    global x_train
    global y_train
    res=[]
    kf = KFold(len(x_train), n_folds=10, shuffle=True)
    print args

    for arg in args:
        arg_file.write("\t"+str(arg))
        arg_file.flush()
    #TODO: colocar o resto dos parametros
    for train_index, test_index in kf:
        X, X_test = x_train[train_index], x_train[test_index]
        y, y_test = y_train[train_index], y_train[test_index]
        dtrain = xgb.DMatrix( X, label=y)
        param = {'bst:max_depth':args[2], 'bst:eta':args[0], 'silent':1, 'objective':'binary:logistic', 'nthread':4, 'eval_metric':'auc'}
        plst = param.items()
        num_round = int(args[6])
        bst = xgb.train( plst, dtrain, num_round)
        dteste = xgb.DMatrix(X_test)
        y_pred = bst.predict(dteste, ntree_limit=bst.best_ntree_limit)
        res.append(roc_auc_score(y_test,y_pred))
    mean = np.mean(res)
    arg_file.write("\t"+str(mean))
    arg_file.write("\n")
    arg_file.flush()
    return mean

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

#Parameters to optimize: 
    # eta range: [0,1]
    # gamma range: [0,10]
    # max_depth range: [1,10]
    # min_child_weight range: [0,10]
    # subsample range: (0,1]
    # colsample_bytree range: (0,1]
    # num_round sem range ,por opcao, [0,100]
    # scale_pos_weight sem range ,por opcao, [0,10]
    # max_delta_step range: [0,10]
# Lower-bound:
lb = [0,0,1,0,0,0,0,0,0]
# Upper-bound:
ub = [1,10,10,10,1,1,10,10,10]
pso(objective_function,lb,ub,swarmsize=100,omega=0.5,phip=0.5,phig=0.5,debug=True)
exit(0)
file = open('test_file.csv','r')
file = file.read()
lines = file.split("\n")

for line in lines[1:]:
    l = line.split(",")
    
    x_teste.append(l)

del x_teste[-1]

x_teste = np.array(x_teste, dtype='f')



output = open('output.csv','w')
for elem in y_pred:
    output.write(str(elem))
    output.write("\n")