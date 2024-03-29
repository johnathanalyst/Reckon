import numpy as np

def linear(X, W, b):
    return X.dot(W) + b

def sigmoid(Z):
    return 1/(1 + np.exp(-Z))

def dSigmoid(A):
    return np.multiply(A, (1 - A))

def relu(z):
    return np.max(0,z)

def conv1D(A, W):
    m, n, fn, fw = A.shape[0], A.shape[1], W.shape[0], W.shape[1]
    Z = np.zeros([m, (n-fw+1)*fn])
    for f in range(fn):
        for s in range((n-fw+1)*30):
            Z[:,s:s+fw] = np.sum(np.multiply(A[:, s:s+fw], W[f,:]))
    return Z

def softmax(Z):
    e = np.exp(Z)
    return e / np.sum(e)

def hoeffding(X,delta):
    min,max = np.amin(np.sum(X,axis=1)),np.amax(np.sum(X,axis=1))
    return np.sqrt(np.square(max-min)*np.log(2/delta)/(2*X.size))
