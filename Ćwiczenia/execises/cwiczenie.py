
kids = ['Mateusz', "Łukasz", 'Emilka']


def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function('Mateusz', "Łukasz", 'Emilka')
