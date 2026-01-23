class Pracownik:
    def __init__(self, name, surname, position, pensja):
        self.name = name
        self.surname = surname
        self.position = position
        self.pensja = pensja

    def przedstaw_sie(self):
        print(f"Czesc, nazywam sie {self.name} {self.surname} i pracuje na stanowisku {self.position}")

class Informatyk(Pracownik):
    def programuj(self, jezyk):
        self.jezyk = jezyk
        print(f"Programuje w {self.jezyk}")

class Ksiegowy(Pracownik):
    def licz_roczna_pensja(self, osoba):
        osoba.pensja *= 12
        print(f"Roczna pensja {osoba.name} wynosi {osoba.pensja}")


p1 = Informatyk("Jan", "Kowalski", "programista", 7000)
p1.programuj("JAVA")
p2 = Ksiegowy("Ryszard", "Mazurek", "Ksiegowy", 6000)
p2.licz_roczna_pensja(p1)
p3 = Pracownik("Janina", "Kwiatkowska", "Dyrektor", 12000)
p2.licz_roczna_pensja(p3)
