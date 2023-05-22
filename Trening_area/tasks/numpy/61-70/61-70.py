import numpy as np

# %% Wyznacz tablicę składającą się ze średnich arytmetycznych tablic A i B 
# odpowiadających im elementów.
A = np.array([[3, 4, 9, 2],
              [5, 3, 2, 5]])
B = np.array([[4, 3, 2, 5],
              [6, 3, 1, 6]])
C = (A+B)/2
C

# %% Pomnóż tablice przez siebie - element po elemencie (element-wise).
A = np.array([[3, 4, 9, 2],
              [5, 3, 2, 5]])
B = np.array([[4, 3, 2, 5],
              [6, 3, 1, 6]])
C = A*B # lub np.multiply(A,B)
C

# %% Wyznacz pierwiastek z każdego elementu tablicy A.
A = np.array([[3, 4, 9, 2],
              [5, 3, 2, 5]])
B = np.sqrt(A)
B

# %% Sprawdź działanie jedynki trygonometrycznej na tablicy A i następnie 
# porównaj wynik z tablicą B.
A = np.linspace(0, np.pi / 2, 20)
print(A)
B = np.full(shape=(20,), fill_value=1, dtype='float')
print(B)
C = np.sin(A) ** 2 + np.cos(A) **2 # lub np.power(np.sin(A), 2) + np.power(np.cos(A), 2)
print(C)
D = np.allclose(C,B)
print(D)

# %% Dokonaj mnożenia macierzowego tablic A i B.
# A- macierz wymiaru (3,2) 
# B- macierz wymiaru (2,3)
A = np.array([[2, 3],
              [-4, 2],
              [5, 0]])
B = np.array([[4, 3, 2],
              [-1, 0, 2]])
C = np.dot(A,B)  # lub A.dot(B)
C

# %% Wyznacz wyznacznik macierzy A.
A = np.array([[-2, 0, 4],
              [5, 2, -1],
              [-4, 2, 4]])
B = np.linalg.det(A)
B

# %% Wyzancz wartości własne i odpowiadające im wektory własne macierzy A.
np.set_printoptions(suppress=True, precision=4)
A = np.array([[5, 8, 16],
              [4, 1, 8],
              [-4, 4, -11]])
B = np.linalg.eig(A)
B

# %% Wyznacz ślad macierzy kwadratowej A (suma elementów na głównej przekątnej)
# Dokonaj transpozycji macierzy A
A = np.array([[5, 8, 16],
              [4, 1, 8],
              [-4, 4, -11]])
B = np.trace(A)
print(B)
C = np.transpose(A)
print(C)

# %% Przekształć tablicę  B  tak, aby można było dokonać mnożenia macierzowego 
# A*B. Wykonaj to mnożenie.
A = np.array([[2, 0],
              [4, 2],
              [5, 3],
              [4, 2]])
B = np.array([[4, 0, 2, 1, 1, 0, 2, 9]])
C = B[:,:4]
D = B[:,4:]
E = np.array([C,D])
print(A)
print(A.shape)
print(E)
print(E.shape)
F = E.reshape(E.shape[0],(E.shape[1]*E.shape[2]))
print(F)
print(F.shape)
G = np.dot(A,F)
print(G)   # lub np.dot(A, B.reshape(2,-1))