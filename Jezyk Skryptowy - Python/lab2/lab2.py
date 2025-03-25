# Zadanie 2

import random

def lotto():
    return random.sample(range(1, 50), 6)

wynik_lotto = lotto()
print("Wylosowane liczby Lotto:", wynik_lotto)

# Zadanie 3

def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    if b != 0:
        return a / b
    else:
        return "Nie można dzielić przez zero!"

while True:
    print("Wybierz działanie:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Wyjście")

    wybor = input("Twój wybór (wpisz numer): ")

    if wybor in ('1', '2', '3', '4'):
        liczba1 = float(input("Podaj pierwszą liczbę: "))
        liczba2 = float(input("Podaj drugą liczbę: "))

        if wybor == '1':
            print("Wynik dodawania:", dodawanie(liczba1, liczba2))
        elif wybor == '2':
            print("Wynik odejmowania:", odejmowanie(liczba1, liczba2))
        elif wybor == '3':
            print("Wynik mnożenia:", mnozenie(liczba1, liczba2))
        elif wybor == '4':
            print("Wynik dzielenia:", dzielenie(liczba1, liczba2))
    elif wybor == '5':
        print("Do widzenia!")
        break
    else:
        print("Niepoprawny wybór. Spróbuj ponownie.")

    # Zadanie 4
        
    import math

def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    if b != 0:
        return a / b
    else:
        return "Nie można dzielić przez zero!"
    
def pole_kola(promien):
    return math.pi * promien ** 2

def obwod_kola(promien):
    return 2 * math.pi * promien

while True:
    print("Wybierz działanie:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Oblicz pole koła")
    print("6. Oblicz obwód koła")
    print("7. Wyjście")

    wybor = input("Twój wybór (wpisz numer): ")

    if wybor in ('1', '2', '3', '4'):
        liczba1 = float(input("Podaj pierwszą liczbę: "))
        liczba2 = float(input("Podaj drugą liczbę: "))

        if wybor == '1':
            print("Wynik dodawania:", dodawanie(liczba1, liczba2))
        elif wybor == '2':
            print("Wynik odejmowania:", odejmowanie(liczba1, liczba2))
        elif wybor == '3':
            print("Wynik mnożenia:", mnozenie(liczba1, liczba2))
        elif wybor == '4':
            print("Wynik dzielenia:", dzielenie(liczba1, liczba2))
    elif wybor == '5':
        promien = float(input("Podaj promień koła: "))
        print("Pole koła:", pole_kola(promien))
    elif wybor == '6':
        promien = float(input("Podaj promień koła: "))
        print("Obwód koła:", obwod_kola(promien))
    elif wybor == '7':
        print("Do widzenia!")
        break
    else:
        print("Niepoprawny wybór. Spróbuj ponownie.")

    # Zadanie 5
        
        
def suma_lista(lista):        
    return sum(lista)

def odczytaj_z_pliku(nazwa_pliku):
    with open(nazwa_pliku, 'r') as plik:
        liczby = [int(line.strip()) for line in plik]
    return liczby

liczby_z_pliku = odczytaj_z_pliku("liczby.txt")
suma = suma_lista(liczby_z_pliku)
print("Suma liczb z pliku:", suma)

    # Zadanie 6

import math

def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    if b != 0:
        return a / b
    else:
        return "Nie można dzielić przez zero!"
    
def pole_kola(promien):
    return math.pi * promien ** 2

def obwod_kola(promien):
    return 2 * math.pi * promien

def zapisz_do_pliku(operacja, liczba1, liczba2, wynik):
    with open("historia.txt", "a") as file:
        file.write(f"{liczba1} {operacja} {liczba2} = {wynik}\n")

while True:
    print("Wybierz działanie:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Oblicz pole koła")
    print("6. Oblicz obwód koła")
    print("7. Wyjście")

    wybor = input("Twój wybór (wpisz numer): ")

    if wybor in ('1', '2', '3', '4'):
        liczba1 = float(input("Podaj pierwszą liczbę: "))
        liczba2 = float(input("Podaj drugą liczbę: "))

        if wybor == '1':
            wynik = dodawanie(liczba1, liczba2)
            print("Wynik dodawania:", wynik)
            zapisz_do_pliku("+", liczba1, liczba2, wynik)
        elif wybor == '2':
            wynik = odejmowanie(liczba1, liczba2)
            print("Wynik odejmowania:", wynik)
            zapisz_do_pliku("-", liczba1, liczba2, wynik)
        elif wybor == '3':
            wynik = mnozenie(liczba1, liczba2)
            print("Wynik mnożenia:", wynik)
            zapisz_do_pliku("*", liczba1, liczba2, wynik)
        elif wybor == '4':
            wynik = dzielenie(liczba1, liczba2)
            print("Wynik dzielenia:", wynik)
            zapisz_do_pliku("/", liczba1, liczba2, wynik)
    elif wybor == '5':
        promien = float(input("Podaj promień koła: "))
        wynik = pole_kola(promien)
        print("Pole koła:", wynik)
        zapisz_do_pliku("pole koła", promien, None, wynik)
    elif wybor == '6':
        promien = float(input("Podaj promień koła: "))
        wynik = obwod_kola(promien)
        print("Obwód koła:", wynik)
        zapisz_do_pliku("obwód koła", promien, None, wynik)
    elif wybor == '7':
        print("Do widzenia!")
        break
    else:
        print("Niepoprawny wybór. Spróbuj ponownie.")

    # Zadanie 7
        
    import math

def rozwiazanie_kwadratowe(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        with open("result.txt", "w") as plik:
            plik.write(f"x1 = {x1}, x2 = {x2}")
    elif delta == 0:
        x = -b / (2 * a)
        with open("result.txt", "w") as plik:
            plik.write(f"x = {x}")
    else:
        with open("result.txt", "w") as plik:
            plik.write("Brak rozwiązań")

rozwiazanie_kwadratowe(1, -3, 2)