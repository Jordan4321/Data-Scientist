import numpy as np

# %% Podana jest poniższa tablica A o kształcie (2, 3).
A = np.array([[4, 2, 1],
              [6, 4, 2]])
print(A.shape)
# %%
B = np.expand_dims(A, axis=0)
print(B)
print(B.shape)
# %%
C = np.expand_dims(A, axis=2)
print(C)
print(C.shape)

# %% Wygeneruj trójwymiarową tablicę o nazwie image i kształcie (200, 300, 3) 
# wypełnioną wartościami losowymi od 0 do 255 włącznie i typie danych np.uint8.
image = np.random.randint(255, size=(200,200, 3), dtype=np.uint8)
print(image)

# %% Tablica image z poprzedniego zadania jest kształtu (200, 300, 3).
# 1. Rozszerz tablicę image o jeden wymiar (dodaj nowy wymiar na początku). 
#    kształt wyjściowej tablicy: (1, 200, 300, 3).
# 2. Rozszerz tablicę image o jeden wymiar (dodaj nowy wymiar na końcu).  
#    kształt wyjściowej tablicy: (200, 300, 3, 1).
image = np.random.randint(low=0, high=256, size=(200, 300, 3), dtype=np.uint8)
print(image.shape)
# %%
A = np.expand_dims(image, axis=0)
print(A.shape)
# %%
B = np.expand_dims(image, axis=-1)
print(B.shape)

# %% Podane są dwie losowo wygenerowane tablice image1 oraz image2.
# Każdą z tych tablic rozszerz dodając jeden wymiar na początku i następnie 
# połącz tak otrzymane tablice w jedną o nazwie images. 
# kształt tablicy wynikowej: (2, 200, 300, 3).

image1 = np.random.randint(low=0, high=256, size=(200, 300, 3), dtype=np.uint8)
image2 = np.random.randint(low=0, high=256, size=(200, 300, 3), dtype=np.uint8)
image1 = np.random.randint(low=0, high=256, size=(200, 300, 3), dtype=np.uint8)
image2 = np.random.randint(low=0, high=256, size=(200, 300, 3), dtype=np.uint8)
A = np.expand_dims(image1, axis=0)
B = np.expand_dims(image2, axis=0)
images = np.concatenate((A,B), axis=0)
print(images.shape)

# %% Z tablicy images z poprzedniego zadania wytnij dla pierwszego obrazu dziesięć 
# pierwszych wierszy i dziesięć pierwszych kolumn z kanału trzeciego (indeks 2).
A = images[0, 0:10, 0:10, 2]
print(A)

# %% Z tablicy images z Ćwiczenia 44 wytnij dla drugiego obrazu sto pierwszych wierszy 
# i sto pierwszych kolumn z kanału pierwszego (indeks 0) 
# i wyświetl za pomocą funkcji cv2_imshow.
B = images[1, 0:100, 0:100, 0]
print(B)

# %% Dla obrazu pierwszego z tablicy images przypisz dla pikseli z indeksem  
# [50:150,100:200]  wartość 0 i następnie wyświetl tak otrzymany obraz.
images[0, 50:150, 100:200,] = [0]
cv2_imshow(images[0])
# %% Dla obrazu drugiego z tablicy images przypisz dla pikseli z indeksem  
# [100:150,:150]  wartość 255 i następnie wyświetl tak otrzymany obraz.
images[0, 100:150, :150,] = [255]
cv2_imshow(images[0])

# %% Podana jest poniższa tablica  A  o kształcie (1, 2, 3).
# Usuń zbędny pierwszy wymiar i otrzymaj tablicę o kształcie (2, 3).
A = np.array([[[1, 2, 3],
               [6, 3, 2]]])
B = np.squeeze(A, axis=0)
print(B.shape)
# %% Usuń zbędny pierwszy wymiar i otrzymaj tablicę o kształcie (4,).
A = np.array([[0.4],
              [0.9],
              [0.5],
              [0.6]])
B = np.squeeze(A, axis=-1)
print(B.shape)
# %% Z tablicy images wycięto pierwszy obraz w poniższy sposób:
# Wykorzystując wiedzę z poprzednich ćwiczeń usuń zbędny pierwszy wymiar 
# otrzymanej tablicy image1.
image1 = images[:1]
image1.shape
A = np.squeeze(image1, axis=0)
print(A.shape)

