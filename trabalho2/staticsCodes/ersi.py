import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
from sklearn.svm import SVC

class PLA:
    def fit(self, X, y):
        X = np.array(X)
        self.w = np.random.normal(0,1,len(X[0]))
        self.b = 0
        cont = True
        iterations = 0
        while(cont):
            cont = False
            for i in xrange(len(X)):
                iterations += 1
                if np.dot(X[i],self.w) + self.b < 0:
                    ypred = -1
                else:
                    ypred = 1
                if (ypred != y[i]):
                    self.w = self.w + y[i]*X[i]
                    self.b = self.b + y[i]
                    cont = True
                    break
        print "iterations: ", iterations
        return self.w, self.b

    def predict(self, X):
        X = np.array(X)
        y = []
        for i in xrange(len(X)):
            coef = np.dot(X[i], self.w) + self.b
            ypred = abs(coef)/coef
            y.append(int(ypred))
        return y

class PerceptronGD:
    def __init__(self, tol, eta):
        self.tol = tol
        self.eta = eta
    def fit(self, X, y):
        ws = [] #apenas para guardar todos os planos criados
        bs = [] #apenas para guardar todos os planos criados
        X = np.array(X)
        self.w = np.random.normal(0,1,len(X[0]))
        self.b = 0
        delta_error = 1000
        err_before = 0
        while(delta_error > self.tol):
            err_actual = 0
            delta_w = 0
            for i in xrange(len(X)):
                coef = np.dot(self.w,X[i]) + self.b
                ypred = np.tanh(coef)
                sech = self.sech(coef)
                err = y[i] - ypred
                delta_w += X[i] * (-2) * err * sech**2
                err_actual += err**2
            self.w = self.w - self.eta*delta_w
            self.b -= (-2) * err * sech**2
            delta_error = abs(err_before - err_actual)
            err_before = err_actual
            #guardando os planos criados
            ws.append(self.w)
            bs.append(self.b)
        return ws, bs
    
    def sech(self, x):
        return 1.0/np.cosh(x)

    def predict(self, X):
        X = np.array(X)
        y = []
        for i in xrange(len(X)):
            coef = np.dot(X[i], self.w) + self.b
            ypred = abs(coef)/coef
            y.append(int(ypred))
        return y

def generate_linear_data(w,b,n):
    dim = len(w)
    y = []
    X = []
    for i in xrange(n):
        x = np.random.uniform(-10,10,dim)
        if(np.dot(w,x) + b > 5):
            y.append(1)
            X.append(x)
        elif(np.dot(w,x) + b < -5):
            y.append(-1)
            X.append(x)
    return np.array(X),y

def generate_nonlinear_data(w,b,n,noise):
    dim = len(w)
    y = []
    X = []
    for i in xrange(n):
        x = np.random.uniform(-10,10,dim)
        if(np.dot(w,x) + b > 5):
            y.append(1)
            X.append(x)
        elif(np.dot(w,x) + b < -5):
            y.append(-1)
            X.append(x)
    
    positions = random.sample(range(len(y)),int(len(y)*noise))
    for pos in positions:
        y[pos] = y[pos] * (-1)

    return np.array(X),y

def generate_rbf_data(point, n):
    dim = len(point)
    y = []
    X = []
    for i in xrange(n):
        x = np.random.uniform(-10,10,dim)
        xy_dist = (point[0] - x[0])**2 + (point[1] - x[1])**2
        xy_dist = xy_dist**0.5
        if(xy_dist > 5):
            y.append(1)
            X.append(x)
        elif(xy_dist < 3):
            y.append(-1)
            X.append(x)
    return np.array(X),y

def plot_points(X,y):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    X1 = []
    X2 = []
    for i in xrange(len(y)):
        if (y[i] == -1):
            X1.append(X[i])
        else:
            X2.append(X[i])
    X1 = np.array(X1)
    X2 = np.array(X2)
    ax.scatter(X1[:,0], X1[:,1], X1[:,2], c='blue', marker='^')
    ax.scatter(X2[:,0], X2[:,1], X2[:,2], c='red', marker='o')

def plot_plane_and_points(X,y,w,b):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    X1 = []
    X2 = []
    for i in xrange(len(y)):
        if (y[i] == -1):
            X1.append(X[i])
        else:
            X2.append(X[i])
    X1 = np.array(X1)
    X2 = np.array(X2)
    ax.scatter(X1[:,0], X1[:,1], X1[:,2], c='blue', marker='^')
    ax.scatter(X2[:,0], X2[:,1], X2[:,2], c='red', marker='o')
    # create x,y
    xx, yy = np.meshgrid(np.arange(-15,15), np.arange(-15,15))
    # calculate corresponding z
    z = (-w[0] * xx - w[1] * yy - b) * 1. /w[2]
    # plot the surface
    # plt3d = fig.gca(projection='3d')
    ax.plot_surface(xx, yy, z,alpha=0.3, color="green")    

if __name__ == '__main__':
    data = generate_linear_data(np.array([1,2,3]),0,1000)
    data = generate_nonlinear_data(np.array([1,2,3]),0,1000, .02)
    data = generate_rbf_data([0,0,0],1000)
    plot_points(data[0], data[1])
    plt.show()
    # cls = PerceptronGD(0.01, 0.001)
    # cls = PLA()
    cls = SVC()
    cls.fit(data[0], data[1])
    data_test = generate_rbf_data([0,0,0],5000)
    labels = cls.predict(data_test[0])
    plot_points(data_test[0], labels)

    # w,b = cls.fit(data[0], data[1])
    # print len(w)
    # plot_plane_and_points(data[0], data[1],w[-1],b[-1])
    plt.show()