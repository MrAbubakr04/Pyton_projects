import numpy as np 

# numpy.linalg
# numpy.random
# numpy.fft

A = np.array([[1,2,3],[4,5,6]])

B = A.copy()

C = np.zeros((2,3))
print(C)

D = np.ones((3,2))
print(D)

modified_A = np.zeros_like(A)
print(modified_A)

E = np.eye(3)
print(E)

From = 2.5
To = 7
Step = 0.5

P = np.arange(From, To, Step)
print(P)

p_1 = np.arange(5)#арифмет прогрессия 0-4 с шагом 1
print(p_1)

p_2 = np.arange(5,10)
print(p_2)

Z = np.zeros((2,3),'int')
print(Z)

Y = np.ones((3,3),'complex')
print(Y)

X = np.ones((3,2))

modified_X = X.astype('str')
print(modified_X)

print(A[1,1])#вывод элемента по индексу
print(A[1][1])
print(A[1])#вывод строки по индексу 
print(A[1,:])#вывод с 1 элемента до конца
print(A[:,1])#вывод с конца до 1
arr = np.arange(5)
print(arr)
print(arr[0:4:2])#вывод элементов в массиве с какого 0, <4,шаг: 2

