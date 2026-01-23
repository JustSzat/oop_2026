class Student:
    def __init__(self, name, surname, oceny):
        self.__namename = name
        self.__surname = surname
        self.__oceny = oceny

    def get_name(self):
        print(f"Imie: {self.__namename}")

    def get_surname(self):
        print(f"Nazwisko: {self.__surname}")

    def get_oceny(self):
        print(f"Oceny: {self.__oceny}")



justyna = ("Justyna", "Szatkowska", [5, 5, 4, 3])
tomasz = ("Tomasz", "Kowalski", [ 3, 4, 3, 3])
janina = ("Janina", "Nowak", [5, 5, 5, 4])