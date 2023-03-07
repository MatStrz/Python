
liczby = [1, 2, 3, 4, 5, 6]

potegiDwojki = []
for element in liczby:
    potegiDwojki.append(element**2)

liczbyParzyste = []
for element in liczby:
    if element % 2 == 0:
        liczbyParzyste.append(element)

potegiDwojki1 = [element**6
                 for element in range(50)]
print(potegiDwojki1)

liczbyParzyste1 = [element
                   for element in liczby
                   if element % 2 == 0]
print(liczbyParzyste1)


"""
numbersGenerator = (element**2
                    for element in range(100)
                    )
for item in numbersGenerator:
    print(item)
"""

numbers = [1, 2, 3, 4, 5, 6]


multiplicationNumbers = {
    number: number * number
    for number in numbers}
