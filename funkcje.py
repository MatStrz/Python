"""
    Funkcja - to blok kodu do którego można odwołać się
              w każdej chwili, aby otrzymać pożądany przez nas wynik.

    definition


    def nazwa_funkcji():
       instrukcja1
       instrukcja2

    nazwa_funkcji()

"""
"""
def wiadomosc_powitalna(imie):
    print("Cześć,",imie,"miło mi powitać Cię w moim programie!")


imiona = ["Arku", "Wiolu", "Bartku"]

for imie in imiona:
    wiadomosc_powitalna(imie)
"""
"""

a = int(input("a"))
b = int(input("podaj bok b"))

def pole_prostokąta(c, d):
    return c * d

print(6 * pole_prostokąta(a, b))
"""
"""
def pole_prostokąta(a, b):
    return a * b

def pole_kwadratu(a):
    return a * a

def pole_trojkata(a, h):
    return (a * h) /2

def pole_trapezu(a, b, h):
    return (a + b) * h / 2

def pole_kola(r):
    return (r**2 * 3.14)

from enum import IntEnum

Menu_Figury = IntEnum('Menu_Figury', 'Prostokąt Kwadrat Trójkąt Trapez Koło Zakończ')

while True:
    print("Program liczący powierzchnię")
    print("1- Pole prostokąta")
    print("2- Pole kwadratu")
    print("3- Pole trójkoąta")
    print("4- Pole trapezu")
    print("5- Pole koła")
    print("6- zakończ")

    wybor = int((input("co chcesz policzyć?")))

    if wybor == Menu_Figury.Prostokąt:
        a = int(input("podaj długość boku a:"))
        b = int(input("podaj długość boku b:"))
        print(" Pole twojego prostokąta =", pole_prostokąta(a, b))
    elif wybor == Menu_Figury.Kwadrat:
        a = int(input("podaj długość boku a:"))
        print("Pole Twojego kwadratu =", pole_kwadratu(a))
    elif wybor == Menu_Figury.Trójkąt:
        a = int(input("Podaj długość podstawy:"))
        h = int(input("Podaj długość wysokośći:"))
        print("Pole Twojego trójkąta =", pole_trojkata(a, h))
    elif wybor == Menu_Figury.Trapez:
        a = int(input("Podaj długość podstawy - a:"))
        b = int(input("Podaj długość podstawy - b:"))
        h = int(input("Podaj długość wysokości:"))
        print("Pole Twojego trapezu =", pole_trapezu(a, b, h))
    elif wybor == Menu_Figury.Koło:
        r = int(input("Podaj długość promienia - r:"))
        print("Pole Twojego koła =", pole_kola(r))
    elif wybor == Menu_Figury.Zakończ:
        break
    else:
        print("niepoprawny wybór")

"""

Menu_DniTygodnia = IntEnum(
    'Menu_DniTygodnia', 'Poniedziałek, Wtorek, Środa, Czwartek, Piątek, Sobota, Niedziela')

Menu_DniTygodnia.Poniedziałek
