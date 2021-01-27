import numpy as np
from scipy.stats import mode
from sklearn.metrics import accuracy_score




class KNN:
    def __init__(self, k):
        self.k = k
    
    def euclidean_distance(self, x1, x2):
        distance = np.linalg.norm(self.x1 - self.x2)
        return distance

    def fit(self, X_train, y_train):
        self.X_train = np.array(X_train)
        self.y_train = np.array(y_train)
        return self
    
    def predict(self, X_train, y_train, X_test, k):
        y_pred = []
        for i in X_test:
            dist = []

            for j in range (len(self.X_train)):
                distance = euclidean_distance(X_train[j, :], i)
                dist.append(distance)
            
            dist = np.array(dist)
            sorted_dist = np.argsort(dist)[:self.k]

            labels = y_train[sorted_dist]
            label = mode(labels)
            label = label.mode[0]
            y_pred.append(label)
        
        return y_pred

    def score(self, Y_test, Y_pred):
        return accuracy_score(y_test, y_pred)