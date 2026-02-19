import math
pi = math.pi
promien = int(input("Podaj promien: "))
pole = math.floor((pi * promien)**2)

def licz_pole():
    if promien > 0:
        print(f"Pole kola wynosi: {pole} ")
    else:
        exit()


licz_pole()