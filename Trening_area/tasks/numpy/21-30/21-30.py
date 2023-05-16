import numpy as np

#%% Wygeneruj poniższą tablicę numpy. Zapisz tablicę do pliku bianarnego 
# o nazwie 'array.npy' i następnie wczytaj z powrotem ten plik do innej zmiennej.
# array([[ 0,  1,  2,  3],
#       [ 4,  5,  6,  7],
#       [ 8,  9, 10, 11]])
A = np.arange(start=0, stop=12, dtype=int).reshape(3,4)
print(A)
np.save('array.npy', A)
np.load('array.npy')

# %% Wygeneruj ponizszą tablicę numpy, zapisz tablicę do pliku tekstowego o nazwie 'array.txt' 
# z dokładnością do drugiego miejsca po przecinku i następnie wczytaj z powrotem ten plik do innej zmiennej.
#array([[ 0,  1,  2,  3],
#       [ 4,  5,  6,  7],
#       [ 8,  9, 10, 11]])
A = np.arange(12).reshape(3,4)
np.savetxt('array.txt', A, fmt='%0.2f')
np.loadtxt('array.txt')

# %% Wygeneruj i przekształć poniższą tablicę numpy na listę.
# array([[ 0,  1,  2,  3],
#       [ 4,  5,  6,  7],
#       [ 8,  9, 10, 11]])
A = np.arange(12).reshape(3,4)
B = A.tolist()
print(B)

# %% powyższą tablicę, używając operatora wycinania przekształcić w:
# tablice ze zamianą wierszy (pierwszy z ostatnim)
# tablice z zamianą kolumn (odwrócona kolejność)
# tablice z zamianą wierszy i kolumn (odwrócone kolejności)
A = np.arange(12).reshape(3,4)
B = A[::-1]
print(B)
C = A[:,::-1]
print(C)
# D = B[:,::-1]
# print(D)
D = A[::-1,::-1]
print(D)

# %% Podaną poniżej tablicę numpy:
# array([[1., 1., 1., 1.],
#         [1., 1., 1., 1.],
#         [1., 1., 1., 1.],
#         [1., 1., 1., 1.]])
# Przekształć na tablicę:
#     array([[0., 0., 0., 0., 0., 0.],
#            [0., 1., 1., 1., 1., 0.],
#            [0., 1., 1., 1., 1., 0.],
#            [0., 1., 1., 1., 1., 0.],
#            [0., 1., 1., 1., 1., 0.],
#            [0., 0., 0., 0., 0., 0.]])
A = np.ones((4,4),dtype=float)
B = np.pad(A, 1)
print(B)
# %% Podaną poniżej tablicę numpy:
# array([[0, 0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0, 0],
#    [0, 0, 0, 0, 0, 0]])
# Przekształć na tablicę:
# array([[10,  0, 10,  0, 10,  0],
#        [ 5,  0,  5,  0,  5,  0],
#        [10,  0, 10,  0, 10,  0],
#        [ 5,  0,  5,  0,  5,  0],
#        [10,  0, 10,  0, 10,  0],
#        [ 5,  0,  5,  0,  5,  0]])
A = np.zeros((6,6),dtype=int)
A[::2,::2] = 10
A[1::2,::2] = 5
print(A)

# %% Połącz podane poniżej tablice  A  oraz  B  w jedną.
A = np.arange(12).reshape(-1, 4)
B = np.array([[4, 3, 7, 2],
             [0, 5, 2, 6]])

C = np.append([A],[B],axis=1)
print(C)

# %% Z podanych poniżej tablic  A  i  B  wydobądź elementy wspólne (przecięcie) tablic.
A = np.arange(8).reshape(-1, 4)
B = np.array([[9, 10, 11, 3],
              [2, 8, 0, 9]]) 

C = np.intersect1d(A,B)
print(C)

# %% Podana jest poniższa tablica numpy A. Znajdź unikalne wartości tej tablicy.
A = np.array([[5, 1, 2, 1, 2],
              [9, 1, 9, 7, 5],
              [4, 1, 5, 7, 9]])
B = np.unique(A)
print(B)

# %% Podana jest poniższa tablica,Zwróć indeksy na których stoją maksymalne wartości dla danego wiersza.
A = np.array([[0.4, 0.3, 0.3],
              [0.1, 0.1, 0.8],
              [0.2, 0.5, 0.3]])
B = np.argmax(A, axis=1)
print(B)