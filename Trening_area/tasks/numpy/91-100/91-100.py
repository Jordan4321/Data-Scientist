import numpy as np

# %% Zbuduj z danych tablicę numpy i nazwij ją wig_games.

wig_games_raw = """Profil	Czas	Kurs	Zmiana	Zmiana %	Odn.	Otw.	Min.	Max.	Wolumen	Obrót	Udział
11B (11BIT)	17 kwi 17:01	391.00	+8.00	(+2.09%)	383.00	383.50	383.00	394.00	12 784	4 994 874	19.034%
CDR (CDPROJEKT)	17 kwi 17:01	339.50	+5.30	(+1.59%)	334.20	338.30	337.00	344.20	233 059	79 245 368	39.618%
CIG (CIGAMES)	17 kwi 17:03	0.742	-0.012	(-1.59%)	0.754	0.772	0.730	0.772	1 311 078	971 459	1.855%
PLW (PLAYWAY)	17 kwi 17:03	387.50	+18.00	(+4.87%)	369.50	374.00	373.00	388.00	33 206	12 661 786	10.638%
TEN (TSGAMES)	17 kwi 17:02	349.50	+22.50	(+6.88%)	327.00	332.00	330.00	353.50	39 793	13 697 060	28.855%"""

wig_games = wig_games_raw.splitlines()
wig_games = [line.split('\t') for line in wig_games]
wig_games = np.array(wig_games, dtype=str)
wig_games = np.char.replace(wig_games, ' ', '')
wig_games

# %% Z tablicy wig_games z poprzedniego ćwiczenia usuń kolumny:Zmiana, Zmiana%,
#    Odn, Wolumen.

wig_games = np.delete(wig_games, [3,4,5,9], axis=1)
wig_games

# %% Tablicę z poprzedniego ćwiczenia wig_games zapisz do pliku wig_games.csv.
# import pandas as pd
# df = pd.DataFrame(wig_games)
# df.to_csv('wig_games.csv')
np.savetxt(fname='wig_games.csv', X=wig_games, fmt='%s', delimiter=',')

# %% Wczytaj do zmiennej wig_games_new zawartość pliku wig_games.csv.
wig_games_new = np.loadtxt(fname='wig_games.csv', delimiter=',',dtype=str)
wig_games_new
# import pandas as pd
# wig_games_new = pd.read_csv('wig_games.csv', sep=',', header=None)
# print(wig_games_new)

# %% Utwórz tablicę o nazwie playway i przypisz do niej poniższe dane.
# Usuń kolumnę o nazwie 'Data'. Do zmiennej playway_values przypisz tylko 
# warotści kolumn bez nagłówków. Skonwertuj tak otrzymaną tablicę na typ danych float.
playway_raw = """Data,Otwarcie,Najwyzszy,Najnizszy,Zamkniecie,Wolumen
2020-03-02,305,324.5,283.5,310,64081
2020-03-03,325.5,340.5,320,340.5,55496
2020-03-04,324,340.5,315,330,36152
2020-03-05,344,344,310,315,35992
2020-03-06,306.5,307,291,305,32539
2020-03-09,274,291,250,258,79402
2020-03-10,278,284.5,256,264,35700
2020-03-11,270,270,238.5,245,60445
2020-03-12,218,228,196,197,94031
2020-03-13,210,229,198.8,211,100412
2020-03-16,205,248,197.8,240.5,50659
2020-03-17,245,269,232.5,264,99480
2020-03-18,264,280,251,270,70136
2020-03-19,267,280,267,279.5,30732
2020-03-20,297.5,307,280,280.5,43426
2020-03-23,274,289,258,285,37098
2020-03-24,305,309,296.5,309,31939
2020-03-25,313,330,295,304,46724
2020-03-26,300,309,295.5,300,27213
2020-03-27,302,306.5,290,296,13466
2020-03-30,299,300,287,300,10316
2020-03-31,302.5,309,302,306.5,15698"""
np.set_printoptions(linewidth=160, suppress=True)
playway = playway_raw.splitlines()
playway = [i.split(',') for i in playway]
playway = np.array(playway, dtype=str)

playway = np.delete(playway, [0], axis=1)
playway = np.delete(playway, [0], axis=0)
playway = playway.astype(float)
playway

# %%  Dla tablicy playway_values z poprzedniego ćwiczenia policz wartość średnią 
#     dla każdej kolumny. Wynik zaokrąglij do 2 miejsca po przecinku.
playway_values = np.mean(playway, axis=0).round(2)
playway_values 
# policz wartość minimalną dla każdej kolumny. Wynik zaokrąglij do 2 miejsca po przecinku.
playway_values = np.min(playway, axis=0).round(2)
playway_values 
# policz wartość maksymalną dla każdej kolumny. Wynik zaokrąglij do 2 miejsca po przecinku.
playway_values = np.max(playway, axis=0).round(2)
playway_values
# Policz różnicę pomiędzy wartością maksymalną i minimalną dla każdej kolumny.
playway_values = np.max(playway, axis=0).round(2) - np.min(playway, axis=0).round(2)
playway_values

# %% Wykorzystując tablicę playway oblicz nową kolumnę będącą różnicą 
#    ceny najwyższej i najniższej.
max_playway = playway[:,[1]]
min_playway = playway[:,[2]]
dif_playway = max_playway - min_playway
playway_values1 = np.concatenate((playway, dif_playway), axis=1)
print(playway_values1)

# %% Z tablicy playway wytnij wiersze, dla których cena zamknięcia wynosi powyżej 300.
playway_close = np.where(np.any(playway[:,[3]] > 300, axis = 1))
playway[playway_close]

# %% Z tablicy playway wytnij 10 pierwszych wierszy z najwyższą wartością 
#    wolumenu posortowane malejąco.
max_10_vol = playway[playway[0:10, 4].argsort()[::-1]]
max_10_vol

# %% Do tablicy playway dodaj 7 kolumnę, która będzie zwracać 1 w przypadku,
#    gdy cena zamknięcia jest wyższa niż cena otwarcia oraz 0 przeciwnie.
open_playway = playway[:,[0]]
close_playway = playway[:,[3]]
dif_playway = close_playway - open_playway
dif_playway = np.where(dif_playway <= 0, dif_playway,True)
dif_playway = np.where(dif_playway > 0, dif_playway,False)
playway_values2 = np.concatenate((playway_values1, dif_playway), axis=1)
print(playway_values2)



