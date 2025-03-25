# Zadanie 2

class Student:
    def __init__(self, imie, numer_albumu):
        self.imie = imie
        self.numer_albumu = numer_albumu

# Tworzenie 3 różnych obiektów klasy Student
student1 = Student("Anna", "12345")
student2 = Student("Jan", "67890")
student3 = Student("Kasia", "11223")

# Wypisanie informacji o obiektach
print(student1.imie, student1.numer_albumu)
print(student2.imie, student2.numer_albumu)
print(student3.imie, student3.numer_albumu)

# Zadanie 3

class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

class Student(Osoba):
    def __init__(self, imie, nazwisko, numer_albumu):
        super().__init__(imie, nazwisko)
        self.numer_albumu = numer_albumu

# Tworzenie 3 różnych obiektów klasy Student
student1 = Student("Anna", "Kowalska", "12345")
student2 = Student("Jan", "Nowak", "67890")
student3 = Student("Kasia", "Wiśniewska", "11223")

# Wypisanie informacji o obiektach
print(student1.imie, student1.nazwisko, student1.numer_albumu)
print(student2.imie, student2.nazwisko, student2.numer_albumu)
print(student3.imie, student3.nazwisko, student3.numer_albumu)

# Zadanie 4

class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko


class Student(Osoba):
    def __init__(self, imie, nazwisko, numer_albumu):
        super().__init__(imie, nazwisko)
        self.numer_albumu = numer_albumu

    def przedstaw_sie(self):
        print(f"Cześć, nazywam się {self.imie} {self.nazwisko} i mój numer albumu to {self.numer_albumu}")


# Tworzenie 3 różnych obiektów klasy Student
student1 = Student("Anna", "Kowalska", "12345")
student2 = Student("Jan", "Nowak", "67890")
student3 = Student("Kasia", "Wiśniewska", "11223")

# Wywołanie metody przedstaw_sie dla każdego obiektu
student1.przedstaw_sie()
student2.przedstaw_sie()
student3.przedstaw_sie()

# Zadanie 5

class Liczba:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Liczba):
            return Liczba(self.value**2 + 2*self.value*other.value + other.value)
        return NotImplemented

    def __repr__(self):
        return f'Liczba({self.value})'

# Testowanie klasy Liczba
x = Liczba(3)
y = Liczba(4)
z = x + y

print(z)

# Zadanie 6

class Dog:
    count = 0  # to jest zmienna klasowa
    dogs = []  # to jest zmienna klasowa

    def __init__(self, name):
        self.name = name  # self.name to zmienna instancyjna
        Dog.count += 1
        Dog.dogs.append(self)

    def bark(self, n):  # to jest metoda instancyjna
        print("{} says: {}".format(self.name, "woof! " * n))

    @staticmethod
    def show_dogs():
        print(f"Liczba piesków: {Dog.count}")
        for dog in Dog.dogs:
            print(dog.name)

# Tworzenie 2 różnych obiektów klasy Dog
dog1 = Dog("Burek")
dog2 = Dog("Azor")

# Wywołanie metody bark dla każdego obiektu
dog1.bark(3)
dog2.bark(2)

# Wywołanie metody statycznej show_dogs
Dog.show_dogs()