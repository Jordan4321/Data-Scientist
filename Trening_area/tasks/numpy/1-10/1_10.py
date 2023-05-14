import numpy as np


# %% Sprawdź czy wszystkie elementy tablic  A,B,C  oraz  D  zwracają wartość logiczną True.
A = np.array([[3, 2, 1, 4],
              [5, 2, 1, 6]])

np.all(A)
#%%
B = np.array([[3, 2, 1, 4],
              [5, 2, 0, 6]])

np.all(B)
# %%
C = np.array([[True, False, False],
              [True, True, True]])

np.all(C)
# %%
D = np.array([0.1, 0.3])

np.all(D)
# %% Sprawdź czy wszystkie elementy tablic  A,B  oraz  C  zwracają wartość logiczną True wzdłuż osi z indeksem 1.

A = np.array([[3, 2, 1, 4],
              [5, 2, 1, 6]])
np.all(A, axis=1)
# %%
B = np.array([[3, 2, 1, 4],
              [5, 2, 0, 6]])
np.all(B, axis=1)
# %%
C = np.array([[True, False, False],
              [True, True, True]])
np.all(C, axis=1)
# %% Sprawdź czy jakikolwiek element tablic  A,B,C  oraz  D  odpowiednio, zwraca wartość logiczną True.
A = np.array([[0, 0, 0],
              [0, 0, 0]])
np.any(A)
# %%
B = np.array([[0, 0, 0],
              [0, 1, 0]])
np.any(B)
# %%
C = np.array([[False, False, False],
              [True, False, False]])
np.any(C)
# %%
D = np.array([[0.1, 0.0]])
np.any(D)
# %% Sprawdź czy jakikolwiek element tablic  A,B,C  oraz  D  odpowiednio, zwraca wartość logiczną True wzdłuż osi z indeksem 0.
A = np.array([[0, 0, 0],
              [0, 0, 0]])
np.any(A, axis=0)
# %%
B = np.array([[0, 0, 0],
              [0, 1, 0]])
np.any(B, axis=0)
# %%
C = np.array([[False, False, False],
              [True, False, False]])
np.any(C, axis=0)
# %%
D = np.array([[0.1, 0.0]])
np.any(D, axis=0)
# %% Sprawdź tablicę  A  pod kątem braków danych
A = np.array([[3, 2, 1, np.nan],
              [5, np.nan, 1, 6]])
print(np.isnan(A))
# %% Sprawdź, czy poniższe tablice  A  oraz  B  są równe pod względem elementów (element-wise) z ustalonym poziomem tolerancji. 
A = np.array([0.4, 0.5, 0.3])
B = np.array([0.39999999, 0.5000001, 0.3])

print(np.allclose(A,B))
# %% Sprawdź, czy poniższe tablice  A  oraz  B  są równe pod względem elementów (element-wise). Użyj operatora porównania ==.
A = np.array([0.4, 0.5, 0.3])
B = np.array([0.3999999999, 0.5000000001, 0.3])
C = (A == B)
print(C)
print(A == B)
# %% Sprawdź, dla których elementów (element-wise) poniższa tablica  A  ma większe wartości niż tablica B.
A = np.array([0.4, 0.5, 0.3, 0.9])
B = np.array([0.38, 0.51, 0.3, 0.91])
C = (A > B)
print(C)
np.greater(A, B)
# %% Stwórz tablicę numpy wymiaru 4x4 wypełnioną zerami. Ustal typ danych na int.
print(np.zeros((4,4), dtype=int))
# %% Stwórz tablicę numpy wymiaru 10x10 wypełnioną liczbą 255. Ustal typ danych na float.
print(np.ones((10, 10), dtype=float))
print(np.ones((10, 10), dtype=float) * 255)
print(np.full((10, 10), 255, dtype=float))
