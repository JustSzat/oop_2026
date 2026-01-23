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

    def set_oceny(self, oceny):
        self.__oceny = oceny
        print(f"Oceny: {oceny}")



justyna = Student("Justyna", "Szatkowska", [5, 5, 4, 3])
tomasz = Student("Tomasz", "Kowalski", [ 3, 4, 3, 3])
janina = Student("Janina", "Nowak", [5, 5, 5, 4])

justyna.get_name()
justyna.set_name("Janina")

tomasz.set_name("Jacek")
janina.get_oceny()
janina.set_oceny([3, 3, 3, 3])