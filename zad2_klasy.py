class Pracownik:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position

    def przedstaw_sie(self):
        print(f"Czesc, nazywam sie {self.name} {self.surname} i pracuje na stanowisku {self.position}")

class Informatyk(Pracownik):
    def programuj(self, jezyk):
        self.jezyk = jezyk
        print(f"Programuje w {self.jezyk}")


p1 = Informatyk("Jan", "Kowalski", "programista")
p1.programuj("Python")