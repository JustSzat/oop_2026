class Student:
    def __init__(self, name, surname, oceny):
        self.__name = name
        self.__surname = surname
        self.__oceny = oceny

    def get_name(self):
        print(f"Imie: {self.__name}")

    def set_name(self, name):
        self.__name = name
        print(f"Imie: {name}")


    def get_surname(self):
        print(f"Nazwisko: {self.__surname}")

    def set_surname(self, surname):
        self.__surname = surname
        print(f"Nazwisko: {surname}")

    def get_oceny(self):
        print(f"Oceny: {self.__oceny}")

    def set_nadpisz_oceny(self, oceny):
        self.__oceny = oceny
        print(f"Oceny: {oceny}")

    def dodaj_ocene(self, ocena):
        self.__oceny.append(ocena)
        print(f"Oceny: {self.__oceny}")


justyna = Student("Justyna", "Szatkowska", [5, 5, 4, 3])
tomasz = Student("Tomasz", "Kowalski", [ 3, 4, 3, 3])
janina = Student("Janina", "Nowak", [5, 5, 5, 4])


tomasz.get_oceny()
tomasz.dodaj_ocene(5)