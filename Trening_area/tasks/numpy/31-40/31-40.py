import numpy as np

# %% Wykonaj dwa sortowania podanej poniżej tablicy, wierzowo oraz kolumnowo (oba rosnąco):
    
A = np.array([[4.99, 3.49, 9.99],
              [1.99, 9.99, 4.99],
              [14.99, 2.39, 7.29]])
B = np.sort(A, axis=1)
print(B)
C = np.sort(A, axis=0)
print(C)

# %% Wytnij wszystkie elementy tablicy  A  o wartości wyższej niż 8.
A = np.array([[4.99, 3.49, 9.99],
              [1.99, 9.99, 4.99],
              [14.99, 2.39, 7.29]])
B = A[(A>8)]
print(B)

# %% Zastąp elementy powyżej wartości 10 wartością stałą 10 (obcięcie wartości do 10).
A = np.array([[4.99, 3.49, 9.99],
              [1.99, 9.99, 14.99],
              [14.99, 2.39, 7.29]])
B = np.where(A<10,A,10)
print(B)

# %% Poniższą dwuwymiarową tablicę  A  przedstaw w postaci 'wypłaszczonej' jednowymiarowej tablicy.
A = np.array([[4.99, 3.49, 9.99],
              [1.99, 9.99, 14.99],
              [14.99, 2.39, 7.29]])
B = np.ravel(A)
print(B)

# %% Zbuduj tablicę o identycznym kształcie i typie danych jak tablica A oraz wypełnij ją stałą wartością 0.0.
A = np.array([[4.99, 3.49, 9.99],
              [1.99, 9.99, 14.99],
              [14.99, 2.39, 7.29]])
B = np.zeros_like(A)
print(B)

# %% Zbuduj tablicę o identycznym kształcie i typie danych jak tablica A oraz wypełnij ją stałą wartością 9.99.
A = np.array([[4.99, 3.49, 9.99],
              [1.99, 9.99, 14.99],
              [14.99, 2.39, 7.29]])
B = np.full_like(A, 9.99)
print(B)

# %% Zbuduj tablicę dwuwymiarową (macierz kwadratową dolną trójkątną) podnaną poniżej:
# array([[1., 0., 0., 0., 0.],
#        [1., 1., 0., 0., 0.],
#        [1., 1., 1., 0., 0.],
#        [1., 1., 1., 1., 0.],
#        [1., 1., 1., 1., 1.]])
B = np.tri(N=5,M=5, k=0)
print(B)

# %% Stwórz dowolną tablicę 3-wymiarową o kształcie (2,3,4).
a = np.array([[[1., 2., 3., 4.],
               [1., 2., 3., 4.],
               [1., 2., 3., 4.]],

              [[5., 6., 7., 8.],
               [5., 6., 7., 8.],
               [5., 6., 7., 8.]]])
res = a.T.reshape((-1,2))
print(res)

# %% Wygeneruj dwuwymiarową tablicę o kształcie (200, 300) wypełnioną wartościami 
# losowymi od 0 do 255 włacznie i typie danych np.uint8 i przypisz do zmiennej image.
image = np.random.randint(255, size=(200, 300), dtype=np.uint8)
print(image)

# %% Tablicę image z poprzedniego zadania posortuj wzdłuż wiersza rosnąco. 
# Następnie dzięki funkcji cv2_imshow() wyświetl otrzymany obraz.
image = np.random.randint(255, size=(200, 300), dtype=np.uint8)
B = np.sort(image, axis=1)
print(B)
# %% 
from google.colab.patches import cv2_imshow

cv2_imshow(B)
# %% Tablicę image z poprzedniego zadania posortuj wzdłuż kolumny rosnąco. 
# Następnie dzięki funkcji cv2_imshow() wyświetl otrzymany obraz.
image = np.random.randint(255, size=(200, 300), dtype=np.uint8)
C = np.sort(image, axis=0)
print(C)
# %%
from google.colab.patches import cv2_imshow

cv2_imshow(C)