"""
    wyrażenie słownikowe
"""

names = {"Arkadiusz", "Wioletta", "Karol", "Bartłomiej", "Jakub", "Ania"}

numbers = [1, 2, 3, 4, 5, 6]

celcius = {'t1': -20, 't2': -15, 't3': 0, 't4': 12, 't5': 24}

fahrenheit = {
    wartosc : celcius[wartosc] * 1.8 +32
    for wartosc in celcius
    if celcius[wartosc] > -5
    if celcius[wartosc] < 20
    }
    
    

"""namesLength = {
    name : len(name)
    for name in names
    if name.startswith("A")
}

multipliedNumbers = {
    number : number*number
    for number in range(1, 70)
}

fahrenheit = {
    key: celcius * 1.8 + 32
    for key, celcius in celcius.items()
    if celcius > -5
    if celcius < 20    
}

"""
liczby = (
    value
    for value in range(2, 471)
    if value % 7 == 0 and value % 5 != 0
        )

for value in liczby:
    print(value)

