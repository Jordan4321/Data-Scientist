import numpy as np

# %% Wygeneruj wyszstkie daty poniedziałków ze stycznia i lutego 2020 
# roku jako tablicę numpy.
from datetime import datetime
A = np.arange(datetime(2020,1,6),datetime(2020,3,1),7, dtype='datetime64[D]')
print(A)

# %% Podane są dwie tablice A i B:
A = np.array(['001', '002', '003'], dtype=str)
B = np.array(['XC', 'YC', 'ZC'], dtype=str)
# Sklej je w jedną tak jak pokazano poniżej:
# array(['001XC', '002YC', '003ZC'], dtype='<U5')
C = np.char.add(A,B)
print(C)

# %% Dodaj '000' (3 zera) na początku każdego elementu tablicy.
A = np.array(['1', '2', '3'], dtype=str)
B = np.char.add('000', A)
print(B)
C = np.char.rjust(A, 4, fillchar="0")
print(C)
D = np.char.zfill(A, 4)
print(D)

# %% Podziel każdy element z powyższej tablicy względem spacji otrzymując listę wartości na każdym miejscu.
A = np.array([['PLW CDR 11B TEN', 'AMC LPP'],
              ['CDR PKO KGH', 'CCC QMK']], dtype=str)
B = np.char.split(A, ' ')
print(B)

# %% Zamień wszystkie znaki # na spacje i nastepnie usuń niepotrzebne spacje dookoła tekstu.
A = np.array([['#summer#time#mood'],
              ['#sport#time']])
B = np.char.replace(A, '#', ' ')
print(B)
C = np.char.strip(B, ' ')
print(C)

# %% Policz liczbę wystąpień słowa 'time' w każdym elemencie tablicy A.
A = np.array([['#summer#time#mood', '#vibe'],
              ['#sport#time', '#good#time'],
              ['#event#summer', '#fast#move']])
B = np.char.count(A, sub='time')
print(B)

# %% Instrument | Kod ISIN | Pakiet | Pakiet (PLN) | Udział w portfelu(%) | Udział w obrotach akcjami 
# i PDA na sesji (%) | Średni spread na sesji
# Podziel tekst na linie. Nastepnie każdą linię podziel względem znaku tabulacji 
# '\t' i zbuduj tablicę numpy (bez nagłówków) zawierajacą poniższe dane. 
text = """ALIOR	PLALIOR00045	88 860 000	1 386 216 000	0,891	2,16	14
CCC	PLCCC0000016	27 918 000	1 292 603 400	0,831	5,28	42
CDPROJEKT	PLOPTTC00011	67 348 000	22 864 646 000	14,702	7,39	7
CYFRPLSAT	PLCFRPT00013	275 301 000	6 854 994 900	4,408	1,17	14
DINOPL	PLDINPL00011	47 937 000	8 916 282 000	5,733	9,13	12
JSW	PLJSW0000015	52 636 000	716 902 320	0,461	1,51	24
KGHM	PLKGHM000017	136 410 000	9 881 540 400	6,354	4,78	8
LOTOS	PLLOTOS00025	86 543 000	5 609 717 260	3,607	2,91	16
LPP	PLLPP0000011	1 306 000	7 444 200 000	4,787	1,43	19
MBANK	PLBRE0000012	12 997 000	2 830 746 600	1,820	0,42	24
ORANGEPL	PLTLKPL00017	647 357 000	4 285 503 340	2,756	1,16	13
PEKAO	PLPEKAO00016	176 379 000	9 619 710 660	6,185	5,27	9
PGE	PLPGER000010	796 776 000	3 561 588 720	2,290	2,88	18
PGNIG	PLPGNIG00014	1 624 608 000	6 072 784 704	3,905	1,56	12
PKNORLEN	PLPKN0000018	289 049 000	17 701 360 760	11,382	12,44	8
PKOBP	PLPKO0000016	857 593 000	18 807 014 490	12,093	10,49	9
PLAY	LU1642887738	114 151 000	3 696 209 380	2,377	1,47	16
PZU	PLPZU0000011	568 305 000	17 515 160 100	11,262	6,64	6
SANPL	PLBZ00000044	33 207 000	5 213 499 000	3,352	1,91	18
TAURONPE	PLTAURN00011	1 043 590 000	1 252 308 000	0,805	1,21	33"""
lines = text.splitlines()
lines = [line.split('\t') for line in lines]
result = np.array(lines, dtype=str)
result

# %% Z tabilcy result z poprzedniego zadania usuń wszystkie spacje 
# w tekście oraz zamień wszystkie przecinki na kropki.
# Następnie wytnij 5 kolumnę 'Udział w portfelu(%)' 
# zamień jej typ na float i policz sumę dla tej kolumny. Sprawdź czy wynosi 100%.
A = np.char.replace(result, ' ', '')
A = np.char.replace(A, ',', '.')
print(A)
B = A[:,4:5]
C = B.astype(float)
D = np.sum(C)
print(D)
E = D == 100
print(E)

# %% Z tablicy result wytnij wszystkie wiersze o nazwie spółki zaczynającej 
# się literą P i przypisz do zmiennej stocks_startswith_P.
stock_startswith_P = result[np.char.startswith(result[:,0], 'P')]
stock_startswith_P

# %% Wykorzystując zmienną stocks_startswith_P policz łączny udział spółek, 
# których nazwa rozpoczyna się literą P. Wynik zaokrąglij do dwóch miejsc po przecinku.
P = stock_startswith_P[:,4]
P = np.char.replace(P,',','.')
P = P.astype(float)
print(P)
sum_P = np.sum(P)
sum_P = np.round(sum_P, decimals=2)
print(sum_P)