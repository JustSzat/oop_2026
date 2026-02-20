
i = int(input("Podaj liczbe, dla ktorej ma byc policzona silnia: "))

def licz_silnie():
    if i > 0:
        liczba = 1
        for s in range(1, i + 1):
            liczba *= s
        print(f"Silnia liczby {i} wynosi {liczba}")
    else:
        print("To nie jest liczba calkowita.")




licz_silnie()
