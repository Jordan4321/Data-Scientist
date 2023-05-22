import numpy as np

# %% Od drugiego wiersza tablicy A przestaw losowo wiersze w tablicy.
A = np.array([['id', 'price'],
              ['001', 14.99],
              ['002', 4.99],
              ['003', 7.99],
              ['004', 2.49],
              ['005', 1.49]])
np.random.shuffle(A[1:,:])
print(A)

# %% Zwróć tablicę indeksów, które posortują tablicę A rosnąco.
A = np.array([0.2, 0.15, 0.1, 0.3, 0.2, 0.05])
B = np.argsort(A)
B

# %% Zaokrąglij wartości tej tablicy do trzeciego miejsca po przecinku.
A = np.random.randn(10, 8)
B = np.round(A, decimals=3)
B

# %% Wyznacz pierwiastki wielomianu:
#  W(x)=4x**2+5x+1
W = np.array([4, 15, 1])
A = np.roots(W)
print(A)
# Dokonaj sprawdzenia:
B = np.polyval(W, -1)
print(B)

# %% Wyznacz pierwiastki wielomianów:
# Q(x)=2x3**3+4x2**2−5x+1 
# R(x)=2x3**3−5x+1
Q = np.array([2,4,-5,1])
R = np.array([2,0,-5,1])
A = np.roots(Q)
B = np.roots(R)
print(A)
print(B)

# %% Podane są wielomiany:
W = np.array([4, 5, 1])
Q = np.array([2, 4, -5, 1])
# dodaj wielomian Q i W
Z = np.polyadd(W,Q)
print(Z)
# odejmij od W wielomian Q
Z = np.polysub(W,Q)
print(Z)
# pomnóż W i Q
Z = np.polymul(W,Q)
print(Z)
# W + 2*Q
Y = np.polymul(Q,Q)
Z = np.polyadd(W,Y)  # lub  np.polyadd(W,2*Q)
print(Z)

# %% Użyj funkcji znaku (sign function) dla tablicy A.
A = np.array([[-4, 3, 0, 1, -5],
              [6, -4, -2, 1, 3]])
B = np.sign(A)
print(B)

# %% Wykorzystując funkcję np.arange() wygeneruj poniższą tablicę:
# array(['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04',
#        '2021-01-05', '2021-01-06', '2021-01-07', '2021-01-08',
#        '2021-01-09', '2021-01-10', '2021-01-11', '2021-01-12',
#        '2021-01-13', '2021-01-14', '2021-01-15', '2021-01-16',
#        '2021-01-17', '2021-01-18', '2021-01-19', '2021-01-20',
#        '2021-01-21', '2021-01-22', '2021-01-23', '2021-01-24',
#        '2021-01-25', '2021-01-26', '2021-01-27', '2021-01-28',
#        '2021-01-29', '2021-01-30', '2021-01-31'], dtype='datetime64[D]')
from datetime import datetime, timedelta
A = np.arange(datetime(2021,1,1), datetime(2021,2,1), timedelta(days=1), dtype='datetime64[D]')
print(A)
# %%  Wykorzystując funkcję np.arange() wygeneruj poniższą tablicę:
# array([['2021-01', '2021-02', '2021-03'],
#        ['2021-04', '2021-05', '2021-06'],
#        ['2021-07', '2021-08', '2021-09'],
#        ['2021-10', '2021-11', '2021-12']], dtype='datetime64[M]')
from datetime import datetime, timedelta
A = np.arange(datetime(2021,1,1), datetime(2022,1,1), dtype='datetime64[M]')
print(A)

# %%
A = np.datetime64('today')
print(A) 









