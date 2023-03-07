

"""
for liczba in range(liczbaUzytkownika):
    suma = suma + liczba
    print(suma)
"""
import time


def sumaKolejnych(liczbaUzytkownika):
    suma = 0
    for wartosc in range(liczbaUzytkownika+1):
        suma = suma + wartosc
    return suma


def sumaKolejnych1(liczbaUzytkownika):
    return sum(liczba for liczba in range(1, liczbaUzytkownika+1))


def function_performance(func, arg):
    start = time.perf_counter()
    func(arg)
    end = time.perf_counter()
    return end - start


def show_message(message):
    print(message)


print(function_performance(sumaKolejnych, 500000000))


print(sumaKolejnych(50000000))
