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

    def get_salary(self):
        return self.__salary

p1 = Person("Jan", "Kowalski", 5000)
p1.set_name("Katarzyna")
print(p1.get_name())