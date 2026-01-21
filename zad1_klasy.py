class Person:
    def __init__(self, name, surname, salary):
        self.__name = name
        self.__surname = surname
        self.__salary = salary

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
        if self.__name == "":
             print("Uzupelnij imie")


    def get_surname(self):
        return self.__surname

    def set_surname(self, surname):
        self.__surname = surname
        self.__surname = surname.upper()
        if self.__surname == "":
            print("Uzupelnij nazwisko")

    def get_salary(self):
        return self.__salary



    def set_salary(self, salary):
        self.__salary = salary
        if self.__salary == 4900:
            print("- minimalne wynagrodzenie")
        elif self.__salary > 4901 and self.__salary < 12000:
            print(" -srednie wynagrodzenie w firmie")
        else:
            print(" - najwyzszy poziom wynagrodzen")






p1 = Person("Jan", "Kowalski", 8888)
p2 = Person("Weronika", "Kowal", 12000)
p3 = Person("Emil", "Nowak", 4900)
p1.set_name("Katarzyna")
p1.set_surname("Jackowska")

print(p1.get_name())
print(p1.get_surname())

p3.set_salary(12001)
print(p3.get_name())
print(p3.get_surname())
print(p3.get_salary())