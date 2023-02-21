file = open("liczby.txt")
wiersz = int(file.readline())

wynik = []

def czypierwsza(n):
    d = 2
    while d*d <= n:
        if n % d == 0:
            return False
            break
        d += 1
        if n < 2:
            return False
            break
        else:
            return True
            break



for wiersz in file:
    if czypierwsza(int(wiersz)) == True and int(wiersz) > 100 and int(wiersz) < 5000:
        wiersz = int(wiersz)
        wynik.append(wiersz)



print(wynik)
