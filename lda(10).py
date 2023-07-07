import numpy as np
class LDA:

    def __init__(self, n):
        self.n = n
        self.ld = None

    def fit(self, X, y):
        features = X.shape[1]
        labels = np.unique(y)
        mean = np.mean(X, axis=0)
        SW = np.zeros((features, features))
        SB = np.zeros((features, features))
        for c in labels:
            X_c = X[y == c]
            mean_c = np.mean(X_c, axis=0)
            SW += (X_c - mean_c).T.dot((X_c - mean_c))
            n_c = X_c.shape[0]
            mean_diff = (mean_c - mean).reshape(features, 1)
            SB += n_c * (mean_diff).dot(mean_diff.T)


        A = np.linalg.inv(SW).dot(SB)
        eval, evec = np.linalg.eig(A)
        evec = evec.T
        idxs = np.argsort(abs(eval))[::-1]
        eval = eval[idxs]
        evec = evec[idxs]
        self.ld = evec[0:self.n]

    def transform(self, X):
        # project data
        return np.dot(X, self.ld.T)

import matplotlib.pyplot as plt
from sklearn import datasets
data=datasets.load_iris()
X=data.data
y=data.target
lda=LDA(2)
lda.fit(X,y)
X_projected = lda.transform(X)
print(X.shape)
print(X_projected.shape)
x1=X_projected[:,0]
x2=X_projected[:,1]
plt.scatter(x1,x2,c=y,cmap="viridis")
plt.xlabel("Principal component 1")
plt.ylabel("Principal component 2")
# plt.colorbar()
plt.show()
