import math
import numpy as np
import matplotlib.pyplot as plt

def gradDescent(grad, x, parameters, residual, lr):
    return np.matmul(-lr * grad(x, *parameters[0]), residual).transpose()

def gaussNewton(grad, x, parameters, residual, lr):
    J = grad(x, *parameters[0])
    a = np.linalg.inv(np.matmul(J, J.transpose()))
    return np.matmul(a, np.matmul(-J, residual)).transpose()

def LM(grad, x, parameters, residual, lr):
    J = grad(x, *parameters[0])
    a = np.matmul(J, J.transpose()) + lr * np.identity(np.shape(J)[0])
    return np.matmul(np.linalg.inv(a), np.matmul(-J, residual)).transpose()

def optimize(obj, grad, x, y, updateFunc=gradDescent, pltTitle='Gradient Descent', init=[1, 1, 1, 1, 1], lr=0.1, tolerance=1e-5, iterNum=500):
    parameters = np.reshape(init, (1, -1)).astype(np.float128)
    lastIter = iterNum
    lossHis = []

    for i in range(iterNum):
        residual = np.reshape(obj(x, *parameters[0]), (-1, 1)) - np.reshape(y, (-1, 1))
        lossHis.append(np.sum(abs(residual)))
        if np.max(abs(residual)) < tolerance:
            lastIter = i + 1
            break

        parameters += updateFunc(grad, x, parameters, residual, lr)

    plt.figure()
    plt.plot(range(lastIter), lossHis)
    plt.title('Loss vs Number of Iterations for ' + pltTitle)
    return parameters[0]

def grad(x, p1, p2, p3, p4, p5):
    Jp1 = np.ones(x.shape)
    Jp2 = np.power(x, 1)
    Jp3 = np.power(x, 2)
    Jp4 = np.power(x, 3)
    Jp5 = np.power(x, 4) 
    return np.vstack((Jp1, Jp2, Jp3, Jp4, Jp5))

def obj(x, p1, p2, p3, p4, p5):
    y = p5 * np.power(x, 4) + p4 * np.power(x, 3) + p3 * np.power(x, 2) + p2 * np.power(x, 1) + p1 * np.power(x, 0)
    return y

def gradNext(seq):
    x = np.array(range(1, len(seq) + 1))
    predsGD = obj(len(seq) + 1, *optimize(obj, grad, x, seq))
    predsGN = obj(len(seq) + 1, *optimize(obj, grad, x, seq, gaussNewton, 'Gauss-Newton'))
    predsLM = obj(len(seq) + 1, *optimize(obj, grad, x, seq, LM, 'LM'))

    return predsGN
