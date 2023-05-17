import numpy as np

# %% Połącz dwie tablice
A = np.array([[3, 4, 5],
              [8, 3, 1]])
B = np.array([[0, 5, 2],
              [4, 2, 1]])
C = np.concatenate((A, B), axis=0)
print(C)
D = np.concatenate((A, B), axis=1)
print(D)

# %% Podana jest tablica zawierająca dane data oraz tablica 
# zawierająca docelową klasę dla danego wiersza target:
data = np.array([[4.3, 4.2],
                 [3.1, 3.6]])
target = np.array([[0],
                   [1]])
C = np.concatenate((data, target),axis=1)
print(C)

# %% Przekształć każdą z tych tablic w kolumnę i sklej w jedną dużą tablicę.
feature1 = np.array([1.6, 0.9, 2.2])
feature2 = np.array([0.4, 1.3, 3.2])
feature3 = np.array([1.4, 0.3, 1.2])

A = np.column_stack((feature1,feature2,feature3))
print(A)

# %% Podziel tablicę na 3 części tak aby pierwsze dwie kolumny stanowiły pierwszą tablicę A1 
# cztery kolejne drugą tablicę  A2  oraz dwie ostatnie trzecią tablicę A3
A = np.array([[0, 0, 4, 6, 2, 4, 1, 1],
              [0, 0, 6, 2, 2, 4, 1, 1],
              [0, 0, 1, 3, 5, 5, 1, 1],
              [0, 0, 3, 1, 5, 4, 1, 1],
              [0, 0, 2, 6, 1, 3, 1, 1]])
A1, A2, A3 = np.split(A, [2,6], axis=1)
print(A1)
print(A2)
print(A3)

# %% Wyznacz łączną liczbę elementów niezerowych dla tej tablicy.
A = np.random.randint(low=0, high=2, size=(10, 6))
B = np.count_nonzero(A)
print(B)
# %% Wyznacz łączną liczbę elementów niezerowych dla każdego wiersza tej tablicy.
A = np.random.randint(low=0, high=2, size=(10, 6))
B = np.count_nonzero(A, axis=0)
print(B)

# %% Ustaw odopowiednią opcję biblioteki numpy pozwalającą drukować tablice 
# z określoną precyzją. Ustaw jej wartość na 4.
np.set_printoptions(precision=4)
A = np.random.randn(10, 4)
A
# %% Ustaw wartość precyzji na 8. Następnie ustaw odopowiednią opcję biblioteki 
# numpy pozwalającą stłumić notację wykładniczą.
np.set_printoptions(precision=8, suppress=True)
A = np.array([1.2e-6, 1.7e-7])
A

# %% Usuń trzecią kolumnę z tablicy
A = np.array([[-0.55692881, -0.66003196,  0.70856031],
              [ 0.22378737, -0.19796576, -0.16889332],
              [ 0.26062786,  0.29865445, -0.92259267],
              [-2.40317659,  1.79961876, -1.96495796],
              [ 0.13051561, -1.7085185 ,  0.54885043],
              [ 1.77268727,  0.38751181, -0.05141955],
              [-1.80858596, -0.45075211,  0.15332866],
              [ 1.94218961, -1.93679529, -1.83350954]])
B = np.delete(A, 2, axis=1)
print(B)

# %% Policz normę wektora  v.
v = np.array([3, 4, -2])
A = np.linalg.norm(v)
print(A)

# %% Ustaw odopowiednią opcję biblioteki numpy pozwalającą drukować 10 skrajnych elementów
np.set_printoptions(edgeitems=10)
A = np.random.randint(10, size=(100, 30))
print(A)

