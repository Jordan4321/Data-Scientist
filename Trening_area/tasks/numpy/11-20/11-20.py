import numpy as np

# %% Zbuduj jednowymiarową tablicę numpy liczb dwucyfrowych.
print(np.arange(10,100, dtype=int))

# %% Zbuduj tablice od 10-99 z dziewięcioma listami (zawierającymi po 10 elementów)
print(np.arange(10,100).reshape(9,10))

# %% Zbuduj tablicę dwuwymiarową (macierz jednostkową) o kształcie 6x6 mającą na 
# przekątnej jedynki oraz poza same zera. Użyj typu danych int.
print(np.eye(6, dtype=int))

# %% Ustaw ziarno losowe na wartość 10. Następnie zbuduj jednowymiarową tablicę 
# składającą się z 30 pseudolosowo wygenerowanych wartości z rozkładu jednostajnego nad przedziałem [0,1).
np.random.seed(10)
A = np.random.rand(30)
print(np.array(A))

# %% Ustaw ziarno losowe na wartość 20. 
# Następnie zbuduj dwuwymiarową tablicę o kształcie (10, 4) 
# wartości pseudolosowo wygenerowanych ze standardowego rozkładu normalego N(0,1).
np.random.seed(20)
A = np.random.randn((10),4)
print(A)
# %%Ustaw ziarno losowe na wartość 30. 
# Następnie zbuduj dwuwymiarową tablicę o kształcie (10, 4) 
# wartości pseudolosowo wygenerowanych z rozkładu normalego  N(100,5) .
# μ=100 
# σ2=5
np.random.seed(30)
mu = 100
sigma = np.sqrt(5)
A = sigma * np.random.randn((10),4) + mu
print(A)

# %% Iterując po tablicy numpy  A  element po elemencie (element-wise) wydrukuj każdy element tablicy do konsoli.
A = np.array([[1, 4, 3],
              [5, 2, 6]])
for i in np.nditer(A):
    print(i, end='')

# %% Utwórz jednowymiarową tablicę numpy (wektor) składający się z 11 równo 
# rozmieszczonych punktów z przedziału [0,1].
A = np.linspace(0,1.1, num=11)
print(A)

# %% Ustaw ziarno losowe na wartość 42. Wygeneruj tablicę jednowymiarową (wektor) 
# zawierający możliwy wynik losowania w grę Duży Lotek.
np.random.seed(42)
A = 0
B = []
for i in range(6):
    A += np.random.randint(1,50, dtype=int)
    B.append(A)
    A = 0
    
print(B)

# %% Zbuduj dwuwymiarową tablicę numpy rozmiaru 6x6:
#array([[0, 0, 0, 0, 0, 0],
#       [0, 1, 0, 0, 0, 0],
#       [0, 0, 2, 0, 0, 0],
#       [0, 0, 0, 3, 0, 0],
#       [0, 0, 0, 0, 4, 0],
#       [0, 0, 0, 0, 0, 5]])
A = np.diag([0,1,2,3,4,5])
print(A)
B = np.diag(np.arange(6))
print(B)
